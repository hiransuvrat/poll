from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question

def index(request):
    questionList = Question.objects.all()
    #template = loader.get_template('polls/index.html')
    context = {
        'questionList': questionList,
    }
    return render(request, 'polls/index.html', context)

def detail(request, questionId):
    try:
        question = Question.objects.get(pk=questionId)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, questionId):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % questionId)

def vote(request, questionId):
    return HttpResponse("You're voting on question %s." % questionId)
