from django.shortcuts import render

# Create your views here.


def home(request):
	title="NWL | %s" %("HOME")
	if request.user.is_authenticated():
		user_logged = "Welcome %s" %(request.user)
	else:
		user_logged = "Welcome Guest User"

	context = {
		"template_title" :  title,
		"headline" : user_logged,
	}
	return render(request,"home.html",context)