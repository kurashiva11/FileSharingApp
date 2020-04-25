from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def authhome(request):
	return render(request, "authenticate.html")


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.info(request, "user does not exists, please register or may be password wrong")
			return redirect('/authenticate')

	else:
		messages.info(request, "its a get method, unable to login")
		return redirect('/authenticate')

	return HttpResponse(request, "Some error Occured while logging you in.")





def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		email = request.POST['email']
		password = request.POST['password']
		repassword = request.POST['repassword']

		if username==None or username=="" or firstname==None or firstname=="" or lastname==None or lastname=="" or email==None or email=="":
			messages.info(request, "fields can't be empty")
			return redirect('/authenticate')

		if lastname not in ['Students', 'Lecturers', 'HODS', 'Principals']:
			messages.info(request, "you must be either of them.\nPrincipal, HOD, Lecturer, Student")
			return redirect('/authenticate')

		if password == repassword:

			try:
				user = User.objects.get(username=username)

				if user is not None:
					messages.info(request, 'user already exists')
					return redirect('/authenticate')

			except User.DoesNotExist:
				user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
				user.save()
				auth.login(request, user)
				return redirect('/') # render(request, 'notes.html', {"name": firstname, "files": []})

		else:
			messages.info(request, "password not matching")
			return redirect('/authenticate')

	else:
		messages.info(request, "its a get method, unable to register")
		return redirect('/authenticate')


@login_required(login_url=r'^/authenticate/')
def signout(request):
	auth.logout(request)
	return redirect('/authenticate')