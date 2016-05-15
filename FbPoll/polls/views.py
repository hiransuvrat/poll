from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    questionList = Question.objects.all()
    template = loader.get_template('polls/index.html')
    context = {
        'questionList': questionList,
    }
    return HttpResponse(template.render(context, request))


def detail(request, questionId):
    return HttpResponse("You're looking at question %s." % questionId)

def results(request, questionId):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % questionId)

def vote(request, questionId):
    return HttpResponse("You're voting on question %s." % questionId)
