# Generated by Django 2.0.6 on 2018-06-05 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='model_pic',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]