# Generated by Django 4.1.2 on 2022-10-21 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comunidad',
            name='category',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='category',
        ),
        migrations.AlterField(
            model_name='empresa',
            name='category',
            field=models.CharField(blank=True, choices=[('Empresa', 'Empresa'), ('Fundacion', 'Fundacion'), ('Organizacion', 'Organizacion'), ('Universidad', 'Universidad')], default='Empresa', max_length=50, null=True),
        ),
    ]
