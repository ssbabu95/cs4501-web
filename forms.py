from django import forms


class UserForm(forms.Form):
	Artist = 'Artist'
	Producer = 'Producer'
	General = 'General'
	User_Types = (
	(Artist, 'Artist'), (Producer, 'Producer'),(General, 'General'),
	)
	first_name = forms.CharField(max_length=25, label='First Name')
	last_name = forms.CharField(max_length=25, label='Last Name')
	username = forms.CharField(max_length=25, label='Username')
	password = forms.CharField(widget=forms.PasswordInput())
	type_of_user = forms.ChoiceField(choices = User_Types, label='Select user type') 
	
	
