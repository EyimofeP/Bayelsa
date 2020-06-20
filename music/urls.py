from django.urls import path
from . import views

app_name = "music"

urlpatterns = [
	#/music/
	path("", views.IndexView.as_view(), name="index"),
	#music/51/
	path("<pk>/", views.DetailView.as_view(), name="detail"),
	#music/album/add
	path("album/add/", views.AlbumCreate.as_view(), name="album-add"),
	#music/album/2
	path("album/<pk>/", views.AlbumUpdate.as_view(), name="album-edit"),
	#music/album/2/delete/
	path("album/<pk>/delete/", views.AlbumDelete.as_view(), name="album-delete"),
	#music/album/song/add
	path("album/song/add/", views.SongCreate.as_view(), name="song-add"),
	#music/album/2
	#path("album/<pk>/song/edit/", views.SongUpdate.as_view(), name="song-edit"),
	#music/album/2/delete/
	#path("album/<pk>/song/delete/", views.SongDelete.as_view(), name="song-delete"),
	path("register/", views.UserFormView.as_view(), name="register"),
	#Search
	path("search", views.search, name="search"),
	#Song Index
	path("songs/", views.songs, name="song-index"),
] 
