from django import forms
from .models import ProjectComment, PostComment

class ProjectCommentForm(forms.ModelForm):

	guest = forms.CharField(widget=forms.TextInput(attrs = {'class': 'authorcomment', 'maxlength': '30'}))
	text = forms.CharField(widget=forms.Textarea(attrs= {'class': 'textcomment', 'style':'resize:none;'}))

	class Meta:
		
		model = ProjectComment
		fields = ('guest', 'text')

class PostCommentForm(forms.ModelForm):

	guest = forms.CharField(widget=forms.TextInput(attrs = {'class': 'authorcomment', 'maxlength': '30'}))
	text = forms.CharField(widget=forms.Textarea(attrs= {'class': 'textcomment', 'style':'resize:none;'}))

	class Meta:
		
		model = PostComment
		fields = ('guest', 'text')