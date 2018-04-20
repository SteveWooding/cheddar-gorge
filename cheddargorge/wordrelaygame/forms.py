"""Defines forms for the wordrelaygame app."""
from django import forms
from django.core.validators import RegexValidator

from .models import Word


class WordForm(forms.ModelForm):
    """Form for added a new word to a story."""

    def __init__(self, *args, **kwargs):
        super(WordForm, self).__init__(*args, **kwargs)
        self.fields['content'].validators.append(
            RegexValidator(regex=r'^[A-Za-z]+\.?\,?$'))

    class Meta:
        model = Word
        fields = ['content',]
        labels = {'content': 'Next word?'}
        help_texts = {'content': ('Enter a single word only. ' +
                                  'You can add a fullstop or comma.')}
