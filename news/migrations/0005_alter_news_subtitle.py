# Generated by Django 4.1.5 on 2023-01-24 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_news_author_alter_news_news_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='subtitle',
            field=models.TextField(),
        ),
    ]
