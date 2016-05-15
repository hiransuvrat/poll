from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, questionId):
    return HttpResponse("You're looking at question %s." % questionId)

def results(request, questionId):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % questionId)

def vote(request, questionId):
    return HttpResponse("You're voting on question %s." % questionId)
