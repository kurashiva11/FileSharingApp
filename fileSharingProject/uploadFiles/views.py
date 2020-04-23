from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import uploadFile

import os

# Create your views here.

def valid(post, files):
	try:
		print(post, '\n\n', files, type(post['give_access_to']))
		if post['filename'] == '' or post['filename']==None:
			return False;

		if post['give_access_to']=='' or post['give_access_to']==None:
			return False

		if post['tags']=='' or post['tags']==None:
			return False

		if len(files['file']) == 0:
			return False
	except MultiValueDictKeyError as e:
		return False
	return True


def getTags(s):
	arr = s.split(',')
	for ele in arr[:]:
		ele = ele.strip()
	return arr


def getaccessArray(s):
	ar = []
	if s == "All":
		ar.append('Students')
		ar.append('Lecturers')
		ar.append('HODS')
		ar.append('Principal')

	else:
		ar.append(s)

	return ar

def upload(request):

	if request.method == "POST":

		if valid(request.POST, request.FILES):
			# request.POST['tags'] += ', ' +  request.POST['filename']
			newfile = uploadFile(
				filename = request.POST['filename'],
				file = request.FILES['file'],

				give_access_to = getaccessArray(request.POST['give_access_to']),

				tags = getTags(request.POST['tags']),
				year = 1,
				semister = 1,
				subject = request.POST['subject'],
				lecturer_name = request.POST['lecturer'],
				user = request.user
				)

			newfile.save()
			messages.info(request, "file uploaded successfully.")

		else:
			messages.info(request, "something went wrong\nfile not uploaded")


	return redirect('/')