from __future__ import unicode_literals

from django.db import models


class Question(models.Model):
	questiontext = models.CharField(max_length=200)
	name=models.CharField(max_length=200)

	def __str__(self):
		return self.questiontext

class choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)


	def __str__(self):
		return self.choice_text
