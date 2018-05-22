"""Defines forms for the wordrelaygame app."""
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from .models import Word
from .bannedwords import banned_word_list

VALID_WORD_REGEX = r"^[A-Za-z']+\.?,?\??$"


def validate_not_banned_word(value):
    """Validate that the new word is not or does not contain a banned word."""
    for word in banned_word_list:
        if word in value:
            raise ValidationError('Sorry. That word is or contains a banned ' +
                                  'word. Please try another word.')


class WordForm(forms.ModelForm):
    """Form for added a new word to a story."""

    def __init__(self, *args, **kwargs):
        super(WordForm, self).__init__(*args, **kwargs)
        self.fields['content'].validators.extend((
            RegexValidator(regex=VALID_WORD_REGEX),
            validate_not_banned_word))

    class Meta:
        model = Word
        fields = ['content',]
        labels = {'content': 'Next word?'}
        help_texts = {'content': ('Enter a single word only (apostrophes are '
                                  'allowed). You can add a fullstop, comma '
                                  'or question mark at the end.')}
        widgets = {
            'content': forms.TextInput(attrs={'pattern': VALID_WORD_REGEX})
            }
