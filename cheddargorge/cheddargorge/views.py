from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView

from . import forms


class SignUpView(CreateView):
    """View to process user sign-up."""
    form_class = forms.UserCreateForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        form.save()

        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        login(self.request, user)

        return redirect('wordrelaygame:home')


class DeleteAccountView(LoginRequiredMixin, View):
    """View to delete a user's own account."""
    template_name = 'registration/delete.html'

    def get(self, request, *args, **kwargs):
        """Return the account deletion comfirmation page."""
        return render(request, self.template_name)

    def post(self, request):
        """Delete the user's account, log them out and display a message."""
        self.request.user.delete()
        logout(request)
        messages.info(request, 'Your account has been successfully deleted.')

        return redirect('wordrelaygame:home')
