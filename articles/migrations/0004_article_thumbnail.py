# Generated by Django 5.1.7 on 2025-04-03 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_remove_article_thumbnail_alter_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
