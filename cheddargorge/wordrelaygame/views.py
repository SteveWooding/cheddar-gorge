"""Views for the wordrelayapp."""
from django.views.generic import View, DetailView

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


class AddWordView(View):
    """Add a word to the latest story."""
    http_method_names = ['post']

    def post(self, request):
        """Handles the POST request to add a word to the latest story."""
        pass
