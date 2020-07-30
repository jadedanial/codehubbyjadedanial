from django import forms
from .models import ProjectFeedback, PostFeedback

class ProjectFeedbackForm(forms.ModelForm):

	guest = forms.CharField(widget=forms.TextInput(attrs = {'class': 'authorfeedback', 'maxlength': '30'}))
	text = forms.CharField(widget=forms.Textarea(attrs= {'class': 'textfeedback', 'style':'resize:none;'}))

	class Meta:
		
		model = ProjectFeedback
		fields = ('guest', 'text')

class PostFeedbackForm(forms.ModelForm):

	guest = forms.CharField(widget=forms.TextInput(attrs = {'class': 'authorfeedback', 'maxlength': '30'}))
	text = forms.CharField(widget=forms.Textarea(attrs= {'class': 'textfeedback', 'style':'resize:none;'}))

	class Meta:
		
		model = PostFeedback
		fields = ('guest', 'text')