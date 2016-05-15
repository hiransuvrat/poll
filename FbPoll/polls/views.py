from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

def index(request):
    questionList = Question.objects.all()
    #template = loader.get_template('polls/index.html')
    context = {
        'questionList': questionList,
    }
    return render(request, 'polls/index.html', context)


def detail(request, questionId):
    return HttpResponse("You're looking at question %s." % questionId)

def results(request, questionId):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % questionId)

def vote(request, questionId):
    return HttpResponse("You're voting on question %s." % questionId)
