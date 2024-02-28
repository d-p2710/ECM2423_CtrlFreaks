# Generated by Django 5.0.1 on 2024-02-28 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_points_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvatarPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('part_type', models.CharField(choices=[('colour', 'Colour'), ('mouth', 'Mouth'), ('eyes', 'Eyes'), ('headwear', 'Headwear'), ('accessory', 'Accessory')], max_length=200)),
                ('img_file', models.ImageField(upload_to='profile_images')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('accessory', models.ForeignKey(limit_choices_to={'part_type': 'accessory'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.avatarpart')),
                ('colour', models.ForeignKey(limit_choices_to={'part_type': 'colour'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.avatarpart')),
                ('eyes', models.ForeignKey(limit_choices_to={'part_type': 'eyes'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.avatarpart')),
                ('headwear', models.ForeignKey(limit_choices_to={'part_type': 'headwear'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.avatarpart')),
                ('mouth', models.ForeignKey(limit_choices_to={'part_type': 'mouth'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.avatarpart')),
            ],
        ),
    ]