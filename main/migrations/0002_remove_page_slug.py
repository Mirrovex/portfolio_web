# Generated by Django 5.0.6 on 2024-05-20 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='slug',
        ),
    ]
