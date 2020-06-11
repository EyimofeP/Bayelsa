from django.shortcuts import get_object_or_404, render

from .models import Album

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


