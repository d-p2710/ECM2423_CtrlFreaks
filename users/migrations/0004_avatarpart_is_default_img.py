# Generated by Django 5.0.1 on 2024-02-28 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_avatarpart_remove_profile_avatar_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatarpart',
            name='is_default_img',
            field=models.BooleanField(default=False, verbose_name='Default (image is default selection for this avatar part)'),
        ),
    ]