from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CreateUserForm(forms.Form): 

	username = forms.CharField(required=True) 
	password = forms.CharField(required=True, widget=forms.PasswordInput)
	vegetarian = forms.BooleanField(required=False)
	email = forms.EmailField(required=True)

class AddRestForm(forms.Form):
	
	restName = forms.CharField(required=True)
	restUserRate = forms.IntegerField(required=True, max_value=5)


class ProfileForm(forms.Form):
	
	#restName = forms.CharField(required=True)
	#restUserRate = forms.IntegerField(required=True)
	#ifDelete = forms.BooleanField()
	OpId = forms.IntegerField()
	updateRate = forms.IntegerField()
