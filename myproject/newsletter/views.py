from django.conf import settings
from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from django.core.mail import send_mail

# Create your views here.


def home(request):
	title="NWL | %s" %("HOME")

	if request.method == "POST":
		print request.POST
		
	form = SignUpForm(request.POST or None)
	if request.user.is_authenticated():
		user_logged = "Welcome %s" %(request.user)
	else:
		user_logged = "Welcome Guest User"
	context = {
		"template_title" :  title,
		"headline" : user_logged,
		"form" : form,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New Full Name"

		instance.full_name = full_name
		instance.save()
		context = {
			"template_title" :  title,
			"headline" : "Thank you. Danke Amour",
			"form" : "",
		}

	return render(request,"home.html",context)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key in form.cleaned_data:
		# 	print key,"=>",form.cleaned_data[key]
		email = form.cleaned_data.get("email")
		message = form.cleaned_data.get("message")
		full_name = form.cleaned_data.get("full_name")
		subject = 'Site Contact Form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email,email],
		contact_message = "%s: %s via %s" %(full_name, message, email)
		send_mail(
			subject,
			contact_message,
			from_email,
			[from_email,email],
			fail_silently=True,
			)
		# print email,message,full_name
	context = {
		"form": form
	}
	return render(request,"base.html", context)