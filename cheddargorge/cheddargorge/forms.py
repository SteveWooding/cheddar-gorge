"""Forms for user creation."""
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    """Customise the user creation form."""
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()
        widgets = {
            'email': forms.TextInput(
                attrs={'placeholder': 'name@example.com'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = ('Email Address (optional - for password '
                                      'reset only)')
