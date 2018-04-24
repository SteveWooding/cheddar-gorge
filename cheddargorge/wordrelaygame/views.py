"""Views for the wordrelaygame app."""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import View, DetailView

from .forms import WordForm
from .models import Story

class HomeView(DetailView):
    """Main view that displays the current story & information about the game.

    Shows the current story and information about the game. If there is a user
    logged in and it is their turn, it show a form to add a word to the story.
    """
    context_object_name = 'latest_story'
    model = Story
    template_name = 'wordrelaygame/home.html'

    def get_object(self, queryset=None):
        try:
            latest_story = Story.objects.latest('date_created')
        except Story.DoesNotExist:
            return None
        else:
            return latest_story

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Only pass the form to the context if the current user is different
        # to the user that wrote the last word of the story.
        try:
            latest_word_auth_id = (self.object.words.order_by('-id')[0].
                                   author.id)
        except IndexError:
            latest_word_auth_id = None

        if(kwargs.get('current_user_id') != latest_word_auth_id or
           latest_word_auth_id is None):
            context['form'] = WordForm()
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()  # pylint: disable=locally-disabled, W0201
        if request.user.is_authenticated:
            current_user_id = request.user.id
        else:
            current_user_id = None
        context = self.get_context_data(object=self.object,
                                        current_user_id=current_user_id)
        return self.render_to_response(context)



class AddWordView(LoginRequiredMixin, View):
    """Add a word to the latest story."""
    http_method_names = ['post']

    def post(self, request):
        """Handles the POST request to add a word to the latest story."""
        try:
            latest_story = Story.objects.latest('date_created')
        except Story.DoesNotExist:
            messages.error(request, 'You need to create a story to add a word.')
            return redirect('wordrelaygame:home')

        # Check the author of the previous word is different to the current
        # logged in user.
        try:
            latest_word_auth_id = (latest_story.words.order_by('-id')[0].
                                   author.id)
        except IndexError:
            latest_word_auth_id = None

        if latest_word_auth_id == self.request.user.id:
            messages.error(request, 'You added the last word. ' +
                           'Someone else needs to add a word next.')
            return redirect('wordrelaygame:home')

        # If the form is valid, save the new word
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            word.story = latest_story
            word.author = self.request.user
            word.save()
            return redirect('wordrelaygame:home')

        return render(request, 'wordrelaygame/home.html', {'form': form})
