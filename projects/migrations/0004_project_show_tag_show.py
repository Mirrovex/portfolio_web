# Generated by Django 5.0.6 on 2024-05-20 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_tag_icon_tag_style_alter_projectimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]