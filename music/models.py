from django.db import models

# Album DB Table
class Album(models.Model):
	artist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=500)
	genre = models.CharField(max_length= 100)
	album_logo = models.CharField(max_length= 1000)

	def __str__(self): #Creating Object name
		return f"{self.album_title} - {self.artist}"

# Song DB Table
class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE) #Linking song db to album db
	file_type = models.CharField(max_length=10)
	song_title = models.CharField(max_length=250)

	def __str__(self):
		return f"{self.song_title} - {self.album}"