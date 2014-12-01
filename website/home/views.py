#coding=utf-8
from django.shortcuts import render_to_response

def index_to_home(request):
	"""跳转到首页去"""
	return render_to_response('home.html')


