# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from qa.models import Question, Answer, User

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader
from django.core.paginator import Paginator, EmptyPage

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def index(request, *args, **kwargs):
	
	page_num = request.GET.get('page')
	
	try:
		page_num = 1 if page_num is None else int(page_num)
	except ValueError:
		page_num = 1
	
	limit = 10
	
	new_qs = Question.objects.new()
	paginator = Paginator(new_qs, limit)
	paginator.baseurl = "/?page=" # get url ('index_url_name'), or smth like that?
	
	try:
		page = paginator.page(page_num)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	
	return render(request, 'qa/index.html',
	{'questions': page.object_list, 'paginator': paginator, 'page_number': page_num})
	


def popular(request, *args, **kwargs):
	
	page_num = request.GET.get('page')
	
	try:
		page_num = 1 if page_num is None else int(page_num)
	except ValueError:
		page_num = 1
	
	limit = 10
	
	popular_qs = Question.objects.popular()
	paginator = Paginator(popular_qs, limit)
	paginator.baseurl = "/popular/?page="
	
	try:
		page = paginator.page(page_num)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	
	return render(request, 'qa/popular.html',
	{'questions': page.object_list, 'paginator': paginator, 'page_number': page_num})
	

def question_page(request, *args, **kwargs):

	try:
		qid = int(kwargs['qid'])
	except (ValueError, KeyError):
		raise Http404("Invalid question request")
	
	q = get_object_or_404(Question, pk=qid)
	answers = q.answer_set.all()
	return(render(request, 'qa/question.html', {'question': q, 'answers': answers}))
	
	#return HttpResponse(text)

