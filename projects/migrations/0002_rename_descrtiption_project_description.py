# Generated by Django 5.0.6 on 2024-05-18 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='descrtiption',
            new_name='description',
        ),
    ]
