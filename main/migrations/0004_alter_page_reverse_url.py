# Generated by Django 5.0.6 on 2024-05-20 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='reverse_url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
