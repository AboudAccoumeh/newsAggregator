# Generated by Django 4.1.5 on 2023-02-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_cms_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cms',
            name='logo',
            field=models.ImageField(upload_to='static/svg/'),
        ),
    ]
