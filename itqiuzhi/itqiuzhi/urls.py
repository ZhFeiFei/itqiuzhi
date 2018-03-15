# -*- coding: utf-8 -*-
"""itqiuzhi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve  # 媒体文件图片解析模块

from interview.views import InterListView, InterDetailView, RegView, LoginView, LogoutView, IndexView
from itqiuzhi.settings import MEDIA_ROOT  # 媒体文件图片解析路径

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),  # 首页映射
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 管理媒体文件路径和处理模块
    url(r'^interlist/$', InterListView.as_view(), name="interlist"),  # 求职列表详情页面映射
    url(r'^interdetail/(?P<interview_id>\d+)/$', InterDetailView.as_view(), name="interdetail"),  # 招聘详情
    url(r'^ueditor/', include('DjangoUeditor.urls')),  # 增加编辑器的映射
    url(r'^register/$', RegView.as_view(), name="register"),
    url(r'^login/$',LoginView.as_view(),name="login"),
    url(r'^logout/$',LogoutView.as_view(),name="logout"),


]
