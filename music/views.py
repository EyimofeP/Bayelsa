from django.views import generic
from .models import Album

class IndexView(generic.ListView):
	template_name = "music/index.html"
	context_object_name = "albums"

	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model = Album
	template_name = "music/detail.html"
	context_object_name = "album"





























































































































"""
from django.shortcuts import get_object_or_404, render

from .models import Album, Song

#Music HomePage
def index(request):
	albums = Album.objects.all()
	frontend = {
		"albums" : albums,
	}
	return render(request,"music/index.html",frontend)

#Detail Page
def detail(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	frontend = {
		"album" : album,
	}
	return render(request,"music/detail.html",frontend)
"""