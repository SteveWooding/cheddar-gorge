# Generated by Django 2.0.4 on 2018-04-19 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordrelaygame', '0002_auto_20180419_1512'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ['id']},
        ),
    ]