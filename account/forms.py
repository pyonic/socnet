from django import forms
from django.contrib.auth.models import User
class LoginForm(forms.Form):
	username = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control'}))
class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget = forms.PasswordInput())
	password2 = forms.CharField(label='Repeat password', widget = forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'first_name','email',)

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Passwords does not match')
		return cd['password2']


