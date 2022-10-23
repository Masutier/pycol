# Generated by Django 4.1.2 on 2022-10-18 14:32

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0002_alter_profile_facebook_alter_profile_github_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='pythonistas/default.png', force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[300, 300], upload_to='pythonistas'),
        ),
    ]