#coding=utf-8
from django.shortcuts import render_to_response, get_object_or_404
from .models import *


def post_all(request):
	"""列出所有已经发布的文章"""
	posts = Article.objects.filter(published_date__isnull = False)
	return render_to_response('post_list.html',{'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Article, pk = pk)
	if post.published_date:
		post.click += 1
		post.save()
	return render_to_response('post_detail.html',{'post': post})
		
