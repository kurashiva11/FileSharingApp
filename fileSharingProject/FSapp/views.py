from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from uploadFiles.models import uploadFile
from django.contrib.auth.decorators import login_required

import os
# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def sendFiles(filtered_files):
	filtered_img_paths = []
	filtered_vid_paths = []
	filtered_pdf_paths = []
	filtered_word_paths = []
	filtered_ppt_paths = []
	filtered_txt_paths = []
	filtered_unkown_paths = []
	
	for file in filtered_files:
		file_extention = str(file.file).split('.')[-1].strip()
		print(file_extention, end=' <=> ')
		
		if file_extention in ['jpg', 'jpeg', 'png', 'gif', 'JPG', 'JPEG', 'PNG', 'GIF']:
			print(file.file, "added to pic")
			filtered_img_paths.append(file.file)

		elif file_extention in ['mpg', 'mov', 'mp4', 'avi', 'webm', 'ogg', 'MPG', 'MOV', 'MP4', 'AVI', 'WEBM', 'OGG']:
			print(file.file, "added to vid")
			filtered_vid_paths.append(file.file)
		
		elif file_extention in ['pdf', 'PDF']:
			print(file.file, "added to pdf")
			filtered_pdf_paths.append(file.file)
		
		elif file_extention in ['doc', 'docx', 'dot', 'DOC', 'DOCX', 'DOT']:
			print(file.file, "added to word")
			filtered_word_paths.append(file.file)
		
		elif file_extention in ['ppt', 'pptx', 'PPT', 'PPTX']:
			print(file.file, "added to ppt")
			filtered_ppt_paths.append(file.file)
		
		elif file_extention == ['txt', 'TXT']:
			print(file.file, "added to txt")
			filtered_txt_paths.append(file.file)
		
		else:
			print(file.file, "added to unkoun")
			filtered_unkown_paths.append(file.file)


	print('\n\n')
	return {
		'imgs': filtered_img_paths,
		'vids': filtered_vid_paths,
		'pdfs': filtered_pdf_paths,
		'words': filtered_word_paths,
		'ppts': filtered_ppt_paths,
		'txts': filtered_txt_paths,
		'unkowns': filtered_unkown_paths
		}




def fshome(request):
	if request.user.is_authenticated:
		# print("user = ", user.id)
		user = User.objects.get(username=request.user)
		folder_name = 'user_' + str(user.id)
		print('\n\n\n', BASE_DIR, "   <=>  ", os.path.join(f'{BASE_DIR}/uploaded_media/', folder_name), '\n\n\n')
		# os.system(f'cd {BASE_DIR}/uploaded_media/{folder_name} && dir')
		
		filtered_files = uploadFile.objects.filter(user=user)
		return render(request, "index.html", sendFiles(filtered_files))

	return redirect('/authenticate')





@login_required(login_url='/authenticate')
def search(request):
	query = {}

	for i in request.META["QUERY_STRING"].split("&"):
		query[i.split("=")[0]] = i.split("=")[1]
	
	try:
		lecturer_name = query['lecturer_name']
		tags = query['tags']
		year = query['year']
		sem = query['sem']
		print(lecturer_name, tags, year, sem, len(tags))
		if lecturer_name != '':
			filtered_files = uploadFile.objects.filter(lecturer_name=lecturer_name)
			
			return render(request, "index.html", sendFiles(filtered_files))

		elif tags != '':
			tags = tags.split(',')
			tags = list(map(lambda tag: tag.strip(), tags))

			filtered_files = uploadFile.objects.filter(tags=tags)
			
			return render(request, "index.html", sendFiles(filtered_files))

		else:
			filtered_files = uploadFile.objects.filter(year=year).filter(semister=sem)
			
			return render(request, "index.html", sendFiles(filtered_files))

		return redirect('/')

	except Exception as e:
		return HttpResponse("some unkown error occuered.")
	
