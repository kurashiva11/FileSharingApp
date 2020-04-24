from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import uploadFile

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create your views here.

def valid(post, files):
	try:
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
	arr = list(map(lambda tag: tag.strip(), arr))
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






@login_required(login_url='/authenticate')
def upload(request):

	if request.method == "POST":
		if valid(request.POST, request.FILES):
			newfile = uploadFile(
				file = request.FILES['file'],
				give_access_to = getaccessArray(request.POST['give_access_to']),
				tags = getTags(request.POST['tags']),
				year = int(request.POST['year']),
				semister = int(request.POST['sem']),
				lecturer_name = request.user.first_name,
				user = request.user
				)

			newfile.save()
			messages.info(request, "file uploaded successfully.")

		else:
			messages.info(request, "something went wrong\nfile not uploaded")


	return redirect('/')







@login_required(login_url='/authenticate')
def deleteFile(request):
	# print(BASE_DIR)
	if request.GET['filename'] != '':
		filtered_file = uploadFile.objects.filter(file=request.GET['filename'])

		for file in filtered_file:
			if file.user == request.user:

				filtered_file.delete()
				print(os.path.join(BASE_DIR, f"uploaded_media/{request.GET['filename']}"))

				if os.path.exists(f"uploaded_media/{request.GET['filename']}"):
					os.remove(f"uploaded_media/{request.GET['filename']}")
				else:
					messages.info(request, "The file deleted in DB, but still exists in File System of server.")
					print("The file deleted in DB, but still exists in File System of server.")
					return redirect('/')

				messages.info(request, "file deleted successfully.")
				return redirect('/')
		else:																					# only executes when file not deleted.
			messages.info(request, "Your not uploaded this file\nYou cant delete the file.")
			return redirect('/')

	else:
		messages.inf(request, "sorry something went wrong.\nfile name is empty.")
		return redirect('/')

	return redirect('/')