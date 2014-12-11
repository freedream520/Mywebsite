from django import forms
from .models import Article, Comment
from ckeditor.widgets import CKEditorWidget

class ArticleForm(forms.ModelForm):
	text = forms.CharField(widget=CKEditorWidget(), label = '内容:')
	class Meta:
		model = Article

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'email', 'text')
        labels = {
            'author': '昵称(必填)',
            'email': '电子邮箱(我们会为您保密)(必填)',
            'text': '评论内容',
        }

