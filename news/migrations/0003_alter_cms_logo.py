# Generated by Django 4.1.5 on 2023-01-31 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_author_newssource_subscription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cms',
            name='logo',
            field=models.ImageField(upload_to='svgs/'),
        ),
    ]
