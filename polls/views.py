from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Question,choice


def index(request):
	if request.method=='GET':
		template=loader.get_template('polls/index.html')
		return HttpResponse(template.render(request))
	if request.method=='POST':
		name=request.POST['name']
		choice1=request.POST['c1']
		choice2=request.POST['c2']
		choice3=request.POST['c3']
		q=Question(questiontext=name)
		q.save()
		q.choice_set.create(choice_text=choice1, votes=0)
		q.choice_set.create(choice_text=choice2, votes=0)
		q.choice_set.create(choice_text=choice3, votes=0)
		return HttpResponse('data addition was sucessful')  	
		

def detail(request,question_id):
	if request.method=='GET':
		q=get_object_or_404(Question, pk=question_id)
		return render(request, 'polls/base.html', {'question': q})
	if request.method=='POST':
		option=request.POST['myradio']
		q=get_object_or_404(Question,pk=question_id)
		q.question_text="adit"
		for x in q.choice_set.all():
			if x.choice_text == option:
				x.votes=x.votes+1
				x.save()
		q.save()   
		q=get_object_or_404(Question,pk=question_id)   
		return render(request, 'polls/base.html', {'question': q})	                

	




# Create your views here.
