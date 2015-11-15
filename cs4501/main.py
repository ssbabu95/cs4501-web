from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import urllib.request
import urllib.parse
import json
from django import template
from http import cookies
from django.core.urlresolvers import reverse

from cs4501.forms import UserForm
from cs4501.forms import LoginForm
from cs4501.forms import ListingForm
from cs4501.forms import SearchForm
#import service api error codes, if any
register = template.Library()
@register.filter
def getunder(d, k):
    return d.get(k, None)

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
	if request.method == 'POST':
		account_form = UserForm(request.POST)
		if account_form.is_valid():
			first_name = account_form.cleaned_data['first_name']
			last_name = account_form.cleaned_data['last_name']
			username = account_form.cleaned_data['username']
			password = account_form.cleaned_data['password']
			post_data = {'username': username, 'password': password, 'first_name': first_name, 'last_name': last_name, 'type_of_user': 'general'}
			post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
			req = urllib.request.Request('http://exp-api:8000/createuser', data=post_encoded, method='POST')
			resp_json = urllib.request.urlopen(req).read().decode('utf-8')
			resp = json.loads(resp_json)	
			return render(request, 'home.html')	

		else:
			print(account_form.errors)
	else:
		account_form = UserForm()	
	
	return render(request,'createUser.html', {'account_form': account_form})

def login(request):
	if request.method == 'POST':
		form = LoginForm(data=request.POST)
		if form.is_valid():
			username=form.cleaned_data['uname']
			password=form.cleaned_data['pword']				
			post_data = {'username': username, 'password': password}
			post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
			req = urllib.request.Request('http://exp-api:8000/login', data=post_encoded, method='POST')
			resp_json = urllib.request.urlopen(req).read().decode('utf-8')
			resp = json.loads(resp_json)
			if not resp or 'error' in resp:
				return render(request, 'login.html')
			authenticator = {'auth': resp['authenticator'], 'user_id': resp['user_id']}
			response = HttpResponseRedirect('/profile')
			response.set_cookie("auth", json.dumps(authenticator))
			return response
		else:
			print(form.errors)
	else:		
		form = LoginForm()
		
	return render(request, 'login.html', {'form': form})

def log_out(request):
	auth = request.COOKIES.get('auth')
	jsona = json.loads(auth)	
	post_data = {'u_id': jsona['user_id']}
	post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
	req = urllib.request.Request('http://exp-api:8000/logout', data=post_encoded, method='POST')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	response = HttpResponseRedirect('/logoutsuccess')
	response.set_cookie("auth", '', expires=-1)
	return response
	# more stuff here

def logoutsuccess(request):
	return render(request, 'logout.html')

def profile(request):
	form = SearchForm()
	if request.method == 'POST':
		form = SearchForm(data=request.POST)
		if form.is_valid():
			searchinput=form.cleaned_data['search_input']
			post_data = {'searchinput': searchinput}
			post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
			req = urllib.request.Request('http://exp-api:8000/search', data=post_encoded, method='POST')
			resp_json = urllib.request.urlopen(req).read().decode('utf-8')
			resp = json.loads(resp_json)
	else:
		print(form.errors)
	if request.method == 'GET': 
		return render(request, "profile.html", {'form': form})
	return render(request, "profile.html")
	

def createListing(request):
	form = ListingForm()
	auth = request.COOKIES.get('auth')
	if not auth:
		return HttpResponseRedirect('/home')
	if request.method == 'POST':
		form = ListingForm(data=request.POST)
		if form.is_valid():
			title=form.cleaned_data['title']
			description=form.cleaned_data['description']	
			jsona = json.loads(auth)	
			post_data = {'title': title, 'description': description, 'creator': jsona['user_id'], 'available': True, 'u_id': jsona['user_id']}
			post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
			req = urllib.request.Request('http://exp-api:8000/createlisting', data=post_encoded, method='POST')
			
			resp_json = urllib.request.urlopen(req).read().decode('utf-8')
			resp = json.loads(resp_json)

			response = HttpResponseRedirect('/create_listing_success/')
			return response
		else:
			print(form.errors)

	if request.method == 'GET':
    		return render(request, "create_listing.html", {'form': form})
    #f = ListingForm(request.POST)
	return render(request, "create_listing_success.html")

def createListingSuccess(request):
	return render(request, "create_listing_success.html")

def searchresults(request):
	post_data = {'searchinput': request.POST.get('search_input')}
	post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
	req = urllib.request.Request('http://exp-api:8000/search', data=post_encoded, method='POST')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	#return JsonResponse(resp['hits']['hits'], safe=False)


	return render(request, "searchresults.html", {'hits': resp['hits']['hits']})
