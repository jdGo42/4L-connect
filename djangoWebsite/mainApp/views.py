from django.shortcuts import render
from django.http import HttpRequest

def home(request: HttpRequest):
	return render(request, 'mainApp/home.html')

def camera(request: HttpRequest):
	return render(request, 'mainApp/camera.html')
