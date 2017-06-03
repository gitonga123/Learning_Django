from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.


def home(request):
	title="NWL | %s" %("HOME")

	if request.method == "POST":
		print request.POST
		
	form = SignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		print instance.email
		print instance.timestamp

	if request.user.is_authenticated():
		user_logged = "Welcome %s" %(request.user)
	else:
		user_logged = "Welcome Guest User"

	context = {
		"template_title" :  title,
		"headline" : user_logged,
		"form" : form,
	}
	return render(request,"home.html",context)