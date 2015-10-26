from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import urllib.request
import urllib.parse
import json
from django.http import HttpResponse
from http import cookies

from cs4501.forms import UserForm
from cs4501.forms import LoginForm
from cs4501.forms import ListingForm
#import service api error codes, if any

def render_home(request):
	req = urllib.request.Request('http://exp-api:8000/home')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return render(request, 'home.html')

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
			post_data = {'username':username, 'password': password, 'first_name': first_name, 'last_name': last_name, 'type_of_user': 'general'}
			post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
			req = urllib.request.Request('http://exp-api:8000/createuser', data=post_encoded, method='POST')
			resp_json = urllib.request.urlopen(req).read().decode('utf-8')		
				

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
			resp.set_cookie("auth", resp['authenticator']) #attempt to retrive authenticator
		else:
			print(form.errors)
	else:		
		form = LoginForm()
		
	return render(request, 'login.html', {'form': form})

def log_out(request):
	req = urllib.request.Request('http://exp-api:8000/logout', data=post_encoded, method='POST')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	resp.delete_cookie("auth", resp['authenticator'])
	return render(request, 'logout.html')
	# more stuff here

def profile(request):
	return render(request, 'profile.html')
	# more stuff here

def createListing(request):
	auth = request.COOKIES.get('auth')

	form = ListingForm()
	if request.method == 'POST':
		form = ListingForm(data=request.POST)

	if not auth:
    	#print(account_form.errors)
    	return HttpResponseRedirect(reverse("login") + "?next=" + reverse("create_listing")

	
	if request.method == 'GET':
    	return render("create_listing.html", {'form': form})
    f = ListingForm(request.POST)
    req = urllib.request.Request('http://exp-api:8000/createlisting', data=post_encoded, method='POST')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
    if resp and not resp['ok']:
        if resp['error'] == exp_srvc_errors.E_UNKNOWN_AUTH:
            # exp service reports invalid authenticator -- treat like user not logged in
            return HttpResponseRedirect(reverse("login") + "?next=" + reverse("create_listing")
     #...
     return render("create_listing_success.html")



    
