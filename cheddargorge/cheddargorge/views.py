from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
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
