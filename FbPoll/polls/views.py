from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from .models import Choice, Question

def index(request):
    questionList = Question.objects.all()
    #template = loader.get_template('polls/index.html')
    context = {
        'questionList': questionList,
    }
    return render(request, 'polls/index.html', context)

def detail(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    try:
        selectedChoice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        #TODO: do increament in db rather than saving
        selectedChoice.votes += 1
        selectedChoice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))