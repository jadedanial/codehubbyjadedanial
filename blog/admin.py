from django.contrib import admin
from .models import Skill, Social, Profile, Project, ProjectView, ProjectFeedback, Log, Post, PostView, PostFeedback, SessionIPUrlKey

class SkillAdmin(admin.ModelAdmin):
	
	list_display = ('name', 'imagename')
	list_filter = ('name', 'imagename')
	search_fields = ('name', 'imagename')

class SocialAdmin(admin.ModelAdmin):

	list_display = ('name', 'imagename', 'link')
	list_filter = ('name', 'imagename', 'link')
	search_fields = ('name', 'imagename', 'link')

class ProfileAdmin(admin.ModelAdmin):

	list_display = ('user', 'imagename', 'bio')
	list_filter = ('user', 'imagename', 'bio')
	search_fields = ('user', 'imagename', 'bio')

class ProjectAdmin(admin.ModelAdmin):

	list_display = ('title', 'dateposted', 'author', 'imagename', 'shortcontent', 'slug')
	list_filter = ('title', 'dateposted', 'author', 'imagename', 'shortcontent', 'slug')
	search_fields = ('title', 'dateposted', 'author', 'imagename', 'shortcontent', 'slug')

class ProjectViewAdmin(admin.ModelAdmin):

	list_display = ('project', 'view')
	list_filter = ('project', 'view')
	search_fields = ('project', 'view')

class ProjectFeedbackAdmin(admin.ModelAdmin):

	list_display = ('project', 'guest', 'text', 'datecreated', 'approved')
	list_filter = ('project', 'guest', 'text', 'datecreated', 'approved')
	search_fields = ('project', 'guest', 'text', 'datecreated', 'approved')

class LogAdmin(admin.ModelAdmin):

	list_display = ('logdate', 'title', 'content')
	list_filter = ('logdate', 'title', 'content')
	search_fields = ('logdate', 'title', 'content')

class PostAdmin(admin.ModelAdmin):

	list_display = ('title', 'dateposted', 'author', 'shortcontent', 'slug')
	list_filter = ('title', 'dateposted', 'author', 'shortcontent', 'slug')
	search_fields = ('title', 'dateposted', 'author', 'shortcontent', 'slug')

class PostViewAdmin(admin.ModelAdmin):

	list_display = ('post', 'view')
	list_filter = ('post', 'view')
	search_fields = ('post', 'view')

class PostFeedbackAdmin(admin.ModelAdmin):

	list_display = ('post', 'guest', 'text', 'datecreated', 'approved')
	list_filter = ('post', 'guest', 'text', 'datecreated', 'approved')
	search_fields = ('post', 'guest', 'text', 'datecreated', 'approved')

class SessionIPUrlKeyAdmin(admin.ModelAdmin):

	list_display = ('sessionipurlkey',)
	list_filter = ('sessionipurlkey',)
	search_fields = ('sessionipurlkey',)

admin.site.register(Skill, SkillAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectView, ProjectViewAdmin)
admin.site.register(ProjectFeedback, ProjectFeedbackAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostView, PostViewAdmin)
admin.site.register(PostFeedback, PostFeedbackAdmin)
admin.site.register(SessionIPUrlKey, SessionIPUrlKeyAdmin)