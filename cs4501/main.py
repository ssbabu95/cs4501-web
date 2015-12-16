from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render # get_object_or_405
import urllib.request
import urllib.parse
import json
from django import template
from http import cookies
from django.core.urlresolvers import reverse, reverse_lazy, NoReverseMatch

from cs4501.forms import UserForm
from cs4501.forms import LoginForm
from cs4501.forms import ListingForm
from cs4501.forms import SearchForm
#import service api error codes, if any

from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.http import HttpRequest
from django.utils.cache import get_cache_key
from django.core.cache.utils import make_template_fragment_key

from django.conf import settings
register = template.Library()
@register.filter
def getunder(d, k):
    return d.get(k, None)
@cache_page(60*5)
def home(request):
	req = urllib.request.Request('http://exp-api:8000/home')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return render(request, 'home.html', resp["resp"])
@cache_page(60*5)
def item_det(request, listing_id):
	req = urllib.request.Request('http://exp-api:8000/listing/' + listing_id)
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return render(request, 'det.html', resp["resp"])
@cache_page(60*30)
def about(request):
	return render(request,'about.html')
@cache_page(60*2)
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
@cache_page(60*2)
def login(request):
	auth = request.COOKIES.get('auth')
	if auth:
		return HttpResponseRedirect('/profile')
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
@cache_page(60*5)
def logoutsuccess(request):
	return render(request, 'logout.html')

def profile(request):
	auth = request.COOKIES.get('auth')
	if not auth:
		return HttpResponseRedirect('/login')

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
	
@cache_page(60*2)
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
			expire_view_cache(request, 'home')	
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
	for res in resp['hits']['hits']:
                res['source'] = res.pop('_source')

	return render(request, "searchresults.html", {'hits': resp['hits']['hits']})

def expire_view_cache(request, view_name, args=[], namespace=None, key_prefix=None, method="GET"):
     request.method = method
     request.path = reverse(view_name, args=args)
     key = get_cache_key(request, key_prefix=key_prefix)
     if key:
         if cache.get(key):
             cache.delete(key)
         return True
     return False

