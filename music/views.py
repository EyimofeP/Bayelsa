from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy

from .models import Album, Song

class IndexView(generic.ListView):
	template_name = "music/index.html"
	context_object_name = "albums"

	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model = Album
	template_name = "music/detail.html"
	context_object_name = "album"

class AlbumCreate(CreateView):
	model = Album
	fields = "__all__"

class AlbumUpdate(UpdateView):
	model = Album
	fields = "__all__"

class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy("music:index")

class SongCreate(CreateView):
	model = Song
	fields = ['album','song_title', 'file_type']

class SongUpdate(UpdateView):
	model = Song
	fields = ['album','song_title', 'file_type']
