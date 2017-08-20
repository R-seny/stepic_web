# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, connection

# Create your models here.

from django.contrib.auth.models import User # Import the standard user model

class QuestionManager(models.Manager):
	def new(self):
		return self.all().order_by('-id')
		
	def popular(self):
		return self.all().order_by('-rating')
		#with connection.cursor() as cursor:
		#	cursor.execute("""
		#	SELECT q.id COUNT(*) AS numlikes
		#	FROM qa_question_like_user
		#	GROUP BY q.id
		#	ORDER BY numlikes
		#	""")

class Question(models.Model):
	
	objects = QuestionManager()
	
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	
	author = models.ForeignKey(User, null=True)
	likes = models.ManyToManyField(User, related_name='question_like_user')

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, null=True)
	author = models.ForeignKey(User, null=True)
