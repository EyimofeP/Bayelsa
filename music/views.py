from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView 

from .models import Album, Song
from .forms import UserForm

class IndexView(generic.ListView):
	template_name = "music/index.html"
	context_object_name = "albums"

	def get_queryset(self):
		return Album.objects.all()

class SongView(generic.ListView):
	template_name = "music/song-index.html"
	context_object_name = "song"

	def get_queryset(self):
		return Song.objects.order_by("-album")

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

"""
class SongUpdate(UpdateView):
	model = Song
	fields = ['album','song_title', 'file_type']
"""

#for to create User
class UserFormView(View):
	form_class = UserForm
	template_name = "music/registration_form.html"

	#Display Blank Form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {"form" : form})

	# Process Form Data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)
			
			#Cleaning data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#Authenticate User
			user = authenticate(username=username, password = password)

			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect("music:index")

		return render(request, self.template_name, {"form" : form})

#Search
def search(request):
	query = Album.objects.all()
	song_query =Song.objects.all()

	if "keyword" in request.GET:
		keyword = request.GET['keyword']
		if keyword:
			query = query.filter(album_title__icontains=keyword) or query.filter(artist__icontains=keyword)
			song_query = song_query.filter(song_title__icontains=keyword)

	frontend = {
		"albums" : query,
		"song" : song_query,
		"keyword" : keyword,
	}
	return render(request, "music/search.html", frontend)














