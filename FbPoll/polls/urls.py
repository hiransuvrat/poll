from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<questionId>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<questionId>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<questionId>[0-9]+)/vote/$', views.vote, name='vote'),
]
