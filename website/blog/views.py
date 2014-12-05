#coding=utf-8
from django.shortcuts import render_to_response, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import Http404


def post_all(request):
	"""列出所有已经发布的文章"""
	posts = Article.objects.annotate(num_comment=Count('comment')).filter(
            published_date__isnull=False).prefetch_related(
            'category').prefetch_related('tags').order_by('-published_date')
	return render_to_response('post_list.html',{'posts':posts})

def post_list_by_tag(request, tag):
    """根据标签列出已发布文章"""
    posts = Article.objects.annotate(num_comment=Count('comment')).filter(
        published_date__isnull=False, tags__name=tag).prefetch_related(
        'category').prefetch_related('tags').order_by('-published_date')
    return render_to_response('post_list.html',
                  {'posts': posts, 'list_header': '文章标签 \'{}\''.format(tag)})

def post_list_by_category(request, cg):
    """根据目录列表已发布文章"""
    posts = Article.objects.annotate(num_comment=Count('comment')).filter(
        published_date__isnull=False, category__name=cg).prefetch_related(
        'category').prefetch_related('tags').order_by('-published_date')
    return render_to_response('post_list.html',
                  {'posts': posts, 'list_header': '\'{}\' 分类的存档'.format(cg)})


def post_detail(request, pk):
	post = get_object_or_404(Article, pk = pk)
	if post.published_date:
		post.click += 1
		post.save()
	return render_to_response('post_detail.html',{'post': post})

		
