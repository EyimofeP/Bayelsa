# Generated by Django 3.0.3 on 2020-06-14 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_remove_song_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(upload_to=''),
        ),
    ]
