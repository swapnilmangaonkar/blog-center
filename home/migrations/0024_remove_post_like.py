# Generated by Django 2.0.6 on 2018-06-12 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_post_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
    ]
