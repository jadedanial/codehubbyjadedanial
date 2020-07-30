from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Skill, Social, Profile, Project, ProjectView, ProjectFeedback, Log, Post, PostView, PostFeedback, SessionIPUrlKey
from .forms import *
from django.db.models import F

def home(request):

	logcounts = Log.objects.all().count()

	if logcounts > 6:

		logmid = round(logcounts / 2)
		logstart = logmid - 3
		logend = logstart + 5

	else:

		logstart = 0
		logend = 0

	postcounts = Post.objects.all().count()

	if postcounts > 6:

		postmid = round(postcounts / 2)
		poststart = postmid - 3
		postend = poststart + 5

	else:

		poststart = 0
		postend = 0

	context = {
		'skills': Skill.objects.all(),
		'socials': Social.objects.all(),
		'profiles': Profile.objects.all(),
		'projects': Project.objects.all(),
		'projectviews': ProjectView.objects.all(),
		'projectfeedbacks': ProjectFeedback.objects.all(),
		'logs': Log.objects.all().order_by('-logdate'),
		'posts': Post.objects.all().order_by('-dateposted'),
		'postviews': PostView.objects.all(),
		'postfeedbacks': PostFeedback.objects.all(),
		'featuredlogs': Log.objects.all().order_by('logdate')[logstart:logend],
		'featuredposts': Post.objects.all().order_by('dateposted')[poststart:postend]
	}

	for project in Project.objects.all():

		projectobject = ProjectView.objects.filter(project=project)

		if projectobject:

			pass

		else:

			projectView = ProjectView.objects.create(project=project, view=0)
			projectView.save()

	for post in Post.objects.all():

		postobject = PostView.objects.filter(post=post)

		if postobject:

			pass

		else:

			postView = PostView.objects.create(post=post, view=0)
			postView.save()

	return render(request, 'blog/index.html', context)

def getSession(request):

	if not request.session.session_key:

		request.session.save()

	session_id = request.session.session_key
	return session_id

def getIP(request):

	forwardedfor = request.META.get('HTTP_X_FORWARDED_FOR')

	if forwardedfor:

		ip = forwardedfor.split(',')[0]

	else:

		ip = request.META.get('REMOTE_ADDR')

	return ip

def projectdetail(request, category, pk, slug):

	SessionIPUrl = getSession(request) + getIP(request) + request.build_absolute_uri()

	project = get_object_or_404(Project, pk=pk)
	projectfeedback = ProjectFeedback.objects.filter(project=project).order_by('-pk')

	if request.method == 'POST':

		projectfeedbackform = ProjectFeedbackForm(request.POST or None)

		if projectfeedbackform.is_valid():

			guest = request.POST.get('guest')
			text = request.POST.get('text')

			projectFeedback = ProjectFeedback.objects.create(project=project, guest=guest, text=text)
			projectFeedback.save()

			return HttpResponseRedirect(request.path_info + '#feedback')

	else:

		projectfeedbackform = ProjectFeedbackForm()

	approvedCount = ProjectFeedback.objects.filter(project=project, approved=True).count()

	if(SessionIPUrlKey.objects.filter(sessionipurlkey=SessionIPUrl).count() <= 0):

		Sessionipurlkey = SessionIPUrlKey.objects.create(sessionipurlkey=SessionIPUrl)
		Sessionipurlkey.save()

		if(ProjectView.objects.filter(project=project).count() <= 0):

			projectView = ProjectView.objects.create(project=project, view=1)
			projectView.save()

		else:

			ProjectView.objects.filter(project=project).update(view=F('view') + 1)

	context = {
		'subject': project,
		'feedbacks': projectfeedback,
		'feedbackform': projectfeedbackform,
		'approvedcounts': approvedCount,
		'profiles': Profile.objects.all(),
		'views': ProjectView.objects.all(),
		'allcontents': Project.objects.all().order_by('title'),
		'category': category
	}

	return render(request, 'blog/post.html', context)

def postdetail(request, category, pk, slug):

	SessionIPUrl = getSession(request) + getIP(request) + request.build_absolute_uri()

	post = get_object_or_404(Post, pk=pk)
	postfeedback = PostFeedback.objects.filter(post=post).order_by('-pk')

	if request.method == 'POST':

		postfeedbackform = PostFeedbackForm(request.POST or None)

		if postfeedbackform.is_valid():

			guest = request.POST.get('guest')
			text = request.POST.get('text')

			postFeedback = PostFeedback.objects.create(post=post, guest=guest, text=text)
			postFeedback.save()

			return HttpResponseRedirect(request.path_info + '#feedback')

	else:

		postfeedbackform = PostFeedbackForm()

	approvedCount = PostFeedback.objects.filter(post=post, approved=True).count()

	if(SessionIPUrlKey.objects.filter(sessionipurlkey=SessionIPUrl).count() <= 0):

		Sessionipurlkey = SessionIPUrlKey.objects.create(sessionipurlkey=SessionIPUrl)
		Sessionipurlkey.save()

		if(PostView.objects.filter(post=post).count() <= 0):

			postView = PostView.objects.create(post=post, view=1)
			postView.save()

		else:

			PostView.objects.filter(post=post).update(view=F('view') + 1)

	context = {
		'subject': post,
		'feedbacks': postfeedback,
		'feedbackform': postfeedbackform,
		'approvedcounts': approvedCount,
		'profiles': Profile.objects.all(),
		'views': PostView.objects.all(),
		'allcontents': Post.objects.all().order_by('dateposted'),
		'category': category
	}

	return render(request, 'blog/post.html', context)