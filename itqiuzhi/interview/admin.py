# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from interview.models import User, Author, Interview, Image


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email',)
    list_filter = ('username', 'email',)
    search_fields = ('username', 'email',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'position',)
    list_filter = ('name', 'position',)
    search_fields = ('name', 'position',)


class InterviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'des', 'company',)
    list_filter = ('title', 'des', 'company',)
    search_fields = ('title', 'des', 'company',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(User, UserAdmin),
admin.site.register(Author, AuthorAdmin),
admin.site.register(Interview, InterviewAdmin),
admin.site.register(Image, ImageAdmin),
