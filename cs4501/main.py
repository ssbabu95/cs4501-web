from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


def render_home(request):
	return render(request, 'home.html');
