from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib.sessions.models import Session

from register.models import Users

def index(request):
	if request.method=="GET":
		template=loader.get_template('login/index.html')
		return HttpResponse(template.render(request))
	if request.method=="POST":
		 q=Users.objects.filter(username=request.POST['name'])
		 request.session['username'] = request.POST['name']
		 if len(q)==0:
			 request.session['username'] = request.POST['name']
			 return HttpResponse('check username again')
		 else:
			 return HttpResponse('suceess')
			  
# Create your views here.
