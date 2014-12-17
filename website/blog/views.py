#coding=utf-8
from django.shortcuts import render_to_response, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import Http404
from .forms import ArticleForm, CommentForm
from django.template import RequestContext
from django.shortcuts import redirect


def post_all(request):
	"""列出所有已经发布的文章"""
	posts = Article.objects.annotate(num_comment=Count('comment')).filter(
            published_date__isnull=False).prefetch_related(
            'category').prefetch_related('tags').order_by('-published_date')
	return render_to_response('post_list.html',{'posts':posts},context_instance=RequestContext(request))

def post_list_by_tag(request, tag):
    """根据标签列出已发布文章"""
    posts = Article.objects.annotate(num_comment=Count('comment')).filter(
        published_date__isnull=False, tags__name=tag).prefetch_related(
        'category').prefetch_related('tags').order_by('-published_date')
    return render_to_response('post_list.html',
                  {'posts': posts, 'list_header': '文章标签 \'{}\''.format(tag)},context_instance=RequestContext(request))

def post_list_by_category(request, cg):
    """根据目录列表已发布文章"""
    posts = Article.objects.annotate(num_comment=Count('comment')).filter(
        published_date__isnull=False, category__name=cg).prefetch_related(
        'category').prefetch_related('tags').order_by('-published_date')
    return render_to_response('post_list.html',
                  {'posts': posts, 'list_header': '\'{}\' 分类的存档'.format(cg)},context_instance=RequestContext(request))


def post_detail(request, pk):
	post = get_object_or_404(Article, pk = pk)
	if post.published_date:
		post.click += 1
		post.save()
	return render_to_response('post_detail.html',{'post': post},context_instance=RequestContext(request))


def add_comment(request, pk):
    """添加评论"""
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post_id = pk
        comment.save()

    post = get_object_or_404(Article, pk = pk)
    return render_to_response('post_detail.html',{'post': post},context_instance=RequestContext(request))


def post_new(request):
    """新建文章"""
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # 开始处理标签
            ptags = request.POST['tags'].strip()
            all_tags = []
            if ptags:
                tags = ptags.split(',')
                for tag in tags:
                    try:
                        t = Tag.objects.get(name=tag)
                    except Tag.DoesNotExist:
                        t = Tag(name=tag)
                        t.save()
                    all_tags.append(t)
            post.save()
            for tg in all_tags:
                post.tags.add(tg)
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = ArticleForm()
    return render_to_response('post_edit.html', {'form': form, 'is_new': True},context_instance=RequestContext(request))

		
