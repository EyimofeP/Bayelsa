from django.urls import path
from . import views

urlpatterns = [
	#domain.com/music
	path("", views.index, name="index"),
] 