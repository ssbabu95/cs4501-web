from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import urllib.request
import urllib.parse
import json

from cs4501.forms import UserForm
from cs4501.forms import LoginForm
from cs4501.forms import ListingForm

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

def login(request):
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(data=request.POST)

	else:
		form = LoginForm()
	return render(request, 'login.html', {'form': form})

def log_out(request):
	return render(request, 'logout.html')
	# more stuff here
def profile(request):
	return render(request, 'profile.html')
	# more stuff here

def createListing(request):
	form = ListingForm()
	if request.method == 'POST':
		form = ListingForm(data=request.POST)

	else:
		form = ListingForm()
	return render(request, 'create_listing.html', {'form': form})


