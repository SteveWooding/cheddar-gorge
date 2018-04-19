"""Django models for the wordreplaygame app."""
from django.db import models
from django.utils import timezone

class Story(models.Model):
    """Model for a story object.

    A story is a collection of at least 64 words.
    """
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Story #' + str(self.id)


class Word(models.Model):
    """Model for a word object.

    A word object forms part of a story and belongs to a certain user.
    """
    content = models.CharField(max_length=64)
    story = models.ForeignKey(Story, on_delete=models.CASCADE,
                              related_name='words')
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL,
                               blank=True, null=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['id']
