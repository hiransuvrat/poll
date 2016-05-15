from django.http import HttpResponse, Http404
from .models import Question
from django.shortcuts import get_object_or_404, render

def index(request):
    questionList = Question.objects.all()
    #template = loader.get_template('polls/index.html')
    context = {
        'questionList': questionList,
    }
    return render(request, 'polls/index.html', context)

'''
def detail(request, questionId):
    try:
        question = Question.objects.get(pk=questionId)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
'''

def detail(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, questionId):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % questionId)

def vote(request, questionId):
    return HttpResponse("You're voting on question %s." % questionId)
