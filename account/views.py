from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
	return render(request, 'account/dashboard.html',{'section': 'dashboard'})

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
