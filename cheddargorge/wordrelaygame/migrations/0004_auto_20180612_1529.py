# Generated by Django 2.0.5 on 2018-06-12 15:29

from django.conf import settings
from django.db import migrations, models
import wordrelaygame.models


class Migration(migrations.Migration):

    dependencies = [
        ('wordrelaygame', '0003_auto_20180419_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(wordrelaygame.models.get_sentinel_user), to=settings.AUTH_USER_MODEL),
        ),
    ]
