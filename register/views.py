from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader

from .models import Users


def index(request):
	if request.method=='GET':
	    template=loader.get_template('register/index.html')
	    return HttpResponse(template.render(request))
	if request.method=='POST':
	    name=request.POST['name']
	    password=request.POST['password']
	    q=Users(name,password)
	    q.save()
        return HttpResponseRedirect('/login/')   
    


# Create your views here.
