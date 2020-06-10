from django.shortcuts import render
from django.http import HttpResponse

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
	return HttpResponse(f"<h1>Details for Album id:{album_id} </h1>")


