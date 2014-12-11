#coding=utf-8
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Tag(models.Model):
	"""标签"""
	name = models.CharField(max_length = 40)
	
	def __str__(self):
		return self.name

class Category(models.Model):
	"""分类目录"""
	name = models.CharField(max_length = 40)

	def __str__(self):
		return self.name

class Article(models.Model):
	"""文章"""
	author = models.ForeignKey(User)
	title = models.CharField(max_length = 200)
	text = RichTextField("正文")
	tags = models.ManyToManyField(Tag)
	category = models.ManyToManyField(Category)
	click = models.IntegerField(default = 1)
	like = models.IntegerField(default = 1)
	comment_num = models.IntegerField(default = 0)
	create_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)

	def publish(self):
		self.published_date = timezone.now()

	def __str__(self):
		return self.title

class Comment(models.Model):
	"""评论"""
	author = models.CharField(max_length = 20)
	email = models.EmailField()
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	post = models.ForeignKey(Article)

	def __str__(self):
		return '{0}:{1}'.format(self.author, self.Article.title)

class Evaluate(models.Model):
	"""顶，踩"""
	ip = models.CharField(max_length = 40)
	evaluate = models.IntegerField()
	post = models.ForeignKey(Article)
	
