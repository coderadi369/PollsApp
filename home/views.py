from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader
from django.template import Library
from django.contrib.sessions.models import Session


from polls.models import Question,choice


def index(request):
	latest_question_list = Question.objects.all()
    #latest_question_list={'id':1}
	context={'latestquestion':latest_question_list}
	return render(request,'home/index.html',context)


# Create your views here.
