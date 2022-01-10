from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

@login_required
def dashboard(request):
	return render(request, 'account/dashboard.html',{'section': 'dashboard'})
def register(request):
	if request.method == "POST":
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			#Creating new user bot not saving yet
			new_user = user_form.save(commit = False)
			#Setting crypted password
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			return render(request, 'account/register_done.html', {'new_user': new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request, 'account/register.html', {'user_form': user_form})
def user_login(request):
	if request.method == "POST": #Если мы получили POST запрос
		form = LoginForm(request.POST) # Формируем форму и передаем туда POSt данные
		if form.is_valid(): # Check if form is valid
			cd = form.cleaned_data #Get clear data from post request
			#Authenticate user, check if he exists, Model object or None will return
			user = authenticate(request, username = cd['username'], password = cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('Succes login!')
				else:
					return HttpResponse('Account is not active!')
			else:
				return HttpResponse('Invalid Login or password!')
	else:
		form = LoginForm()
	return render(request, 'account/login.html', {'form': form})
