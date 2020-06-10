from django.db import models

# Album
class Album(models.Model):
	artist = models.Charfield(max_length=250)
	album_title = models.Charfield(max_length=500)
	genre = models.Charfield(max_length= 100)
	album_logo = models.Charfield(max_length= 1000)