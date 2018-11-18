from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
#from django.conf import settings
from django.core.files.storage import FileSystemStorage
from PIL import Image
import random
import os
from datetime import datetime
from accounts.models import Activity_Log
from django.contrib.auth.decorators import login_required

class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

@login_required
def simple_upload(request):
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		request.session['username'] = str(request.user)
		uname = request.session['username']
		request.session['imgtime'] = str(datetime.utcnow())
		dt = request.session['imgtime']
		try:
			im = Image.open(script_dir + uploaded_file_url)
			img1 = image_resize(uploaded_file_url, script_dir)
			resized_image_url = fs.url(img1) + ".jpg"
			d = Activity_Log(username = uname, date_time = dt, activity = 'Uploaded Image')
			d.save()
			return render(request, 'simple_upload.html', {
			'uploaded_file_url': uploaded_file_url,
			'resized_image_url': resized_image_url
			})
		except IOError:
			d = Activity_Log(username = uname, date_time = dt, activity = 'Uploaded Corrupted File')
			d.save()
			os.remove(script_dir + uploaded_file_url)
			return render(request, 'image_error.html')	
	return render(request, 'simple_upload.html')

# Function to resize the image (from Assignment 1) 
def image_resize(flink, script):

	img = Image.open(script + flink)

	# Initializing parameters for resized image.
	new_width = 0
	new_height = 0
	x = random.randint(0,999999)
	print(x)

	# Get parameter values of input image
	width, height = img.size

	# Get parameter values of resized image.
	if width >= 500 or height >= 500:
	    new_width = int(width/2)
	    new_height = new_width
	elif width < 500 or height < 500:
	    new_width = int(width*2)
	    new_height = new_width

	# Resize input image using obtained parameter values using LANCZOS filter.
	img1 = img.resize((new_width, new_height), Image.LANCZOS)
	exte = "new_img" + str(x)
	ext = ".jpg"
	print(exte)

	# Save the new image on the working folder.

	img1.save(script + '/media/' + exte + ext)

	return exte


def model_form_upload(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = DocumentForm()
	return render(request, 'core/model_form_upload.html', {
		'form': form
	})
