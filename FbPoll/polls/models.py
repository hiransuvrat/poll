from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
	questionTxt = models.CharField(max_length=200)
	pubDate = models.DateTimeField('date published')

	def __str__(self):
	    return self.questionTxt

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	votes = models.IntegerField(default=0)
	choiceTxt = models.CharField(max_length=50, default='Yes')

	def __str__(self):
	    return self.choiceTxt
