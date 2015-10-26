
from django import forms


class UserForm(forms.Form):
	Artist = 'Artist'
	Producer = 'Producer'
	General = 'General'
	User_Types = (
	(Artist, 'Artist'), (Producer, 'Producer'),(General, 'General'),	)
	first_name = forms.CharField(max_length=25, label='First Name')
	last_name = forms.CharField(max_length=25, label='Last Name')
	username = forms.CharField(max_length=25, label='Username')
	password = forms.CharField(widget=forms.PasswordInput())
	type_of_user = forms.ChoiceField(choices = User_Types, label='Select user type') 

class LoginForm(forms.Form):
	uname = forms.CharField(label='Username', max_length=25)
	pword = forms.CharField(label='Password', max_length=25, widget=forms.PasswordInput)

class ListingForm(forms.Form):
	title = forms.CharField(label='Title', max_length=16)
	description = forms.CharField()#(blank=True=)