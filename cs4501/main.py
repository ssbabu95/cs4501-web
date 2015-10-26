fromm django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import urllib.request
import urllib.parse
import json

from cs4501.forms import UserForm

def render_home(request):
	req = urllib.request.Request('http://exp-api:8000/home')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return render(request, 'home.html', resp["resp"])

def item_det(request, listing_id):
	req = urllib.request.Request('http://exp-api:8000/listing/' + listing_id)
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return render(request, 'det.html', resp["resp"])
def about(request):
	return render(request,'about.html')
def create_user(request):
	account_form = UserForm()
	if request.method == 'POST':
		account_form = UserForm(data=request.POST)		 
	
	else:
		account_form = UserForm()		
	return render(request,'createUser.html', {'account_form': account_form})

