# Generated by Django 5.0.3 on 2024-03-13 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_crosswordquestion"),
    ]

    operations = [
        migrations.RenameField(
            model_name="crosswordquestion",
            old_name="Hint",
            new_name="hint",
        ),
    ]
