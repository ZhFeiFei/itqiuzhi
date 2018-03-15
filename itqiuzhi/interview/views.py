# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.hashers import make_password
from pure_pagination import PageNotAnInteger, EmptyPage, Paginator  # 导入分页库

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django.db.models import Q  # 或逻辑的判断

# 导入用户表单（登录/登出/认证）
from interview.forms import RegForm, LoginForm
from interview.models import Interview, User, Image  # 导入详情列表数据表/类
from django.contrib.auth import login, logout, authenticate  # 导入用户登录/登出/认证
from django.core.urlresolvers import reverse  # 导入reverse解析模块（用来做重定向）


class IndexView(View):
    """
    首页
    """
    def get(self, request):
        all_interviews_read_counts = Interview.objects.order_by('-read_counts')[:4]
        all_interviews_pub_time = Interview.objects.order_by('-pub_time')[:4]
        all_image = Image.objects.all()
        return render(request, "index.html", {
            "all_interview_read_counts": all_interviews_read_counts,
            "all_interview_pub_time":all_interviews_pub_time,
            "all_image":all_image,
        })

class InterListView(View):
    """
    求职详情列表类
    """

    # 取出所有详情列表
    def get(self, request):
        all_interviews = Interview.objects.all()  # 获取所有的详情对象（列表）

        # 点击搜索
        search_input = request.GET.get('search_input', "")
        if search_input:
            all_interviews = Interview.objects.filter(
                Q(title__icontains=search_input) | Q(des__icontains=search_input) | Q(
                    content__icontains=search_input) | Q(company__icontains=search_input))

        # 基于yearsRequire的分类
        salary = request.GET.get('salary', "")
        if salary:
            all_interviews = Interview.objects.filter(salary=salary)

        # 基于yearsRequire的分类
        yearsRequire = request.GET.get('yearsRequire', "")
        if yearsRequire:
            all_interviews = Interview.objects.filter(yearsRequire=yearsRequire)

        # 基于学历的分类
        education = request.GET.get('education', "")
        if education:
            all_interviews = Interview.objects.filter(education=education)

        # 基于工作性质的分类
        workType = request.GET.get('workType', "")
        if workType:
            all_interviews = Interview.objects.filter(workType=workType)

        # 对详情进行分页处理
        try:
            page = request.GET.get('page', 1)  # 获取page参数，若没有的话则设置为1
        except(PageNotAnInteger, EmptyPage):  # 若没出现异常，也设置为1
            page = 1
        p = Paginator(all_interviews, 1, request=request)  # 创建Paginator实例，讲详情页queryset传进来，设置每个页面项目数为1
        interviews = p.page(page)  # 调用Paginator.page函数，传入获取到的参数，对详情queryset执行分页操作
        return render(request, "list.html", {
            "all_interviews": interviews,  # 传递模板变量给前面的模板文件list.html
        })


class InterDetailView(View):
    """
    求职详情页
    """

    def get(self, request, interview_id):  # interview_id参数（此参数通过url映射得到）
        interview = Interview.objects.get(id=int(interview_id))  # 根据详情id得到

        # 增加阅读次数
        interview.read_counts += 1
        interview.save()

        # 推荐同类公司
        company_tag = interview.company  # 以公司作为推荐标签
        company_interviews = Interview.objects.filter(company=company_tag).exclude(
            id=int(interview_id)).order_by('-read_counts')[:3]

        # 推荐同一行业
        trade_tag = interview.trade  # 以行业作为推荐标签
        trade_interviews = Interview.objects.filter(trade=trade_tag).exclude(company=company_tag).order_by(
            '-read_counts')[:3]

        return render(request, "toudi.html", {
            "interview": interview,
            "company_interviews": company_interviews,
            "trade_interviews": trade_interviews,
        })


class RegView(View):
    """
    注册页
    """

    def get(self, request):
        return render(request, "register.html", {

        })

    def post(self, request):
        regform = RegForm(request.POST)  # 通过注册表单获# 取用户提交的内容（form表单中的name字段），然后创建实例regform
        if regform.is_valid():  # 若表单有效性验证成功
            username = request.POST.get("email", "")  # 获取用户/邮箱/密码信息
            email = request.POST.get("email", "")
            password = request.POST.get("password", "")
            user = User()  # 创建用户实例
            user.username = username
            user.email = email
            user.password = password
            user.password = make_password(password)  # 将密码加密处理
            user.save()  # 保存到数据库
            return render(request, "login.html", {})
        else:
            return render(request, "register.html", {
                "regform": regform  # 如果表单验证失败，则停留在本地
            })


class LoginView(View):
    """
    用户登录页
    """

    def get(self, request):  # 用户基础访问
        return render(request, "login.html", {

        })

    def post(self, request):
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = request.POST.get("email", "")
            password = request.POST.get("password", "")
            user = authenticate(username=username, password=password)
            if user is not None:  # 若有账号认证成功
                login(request, user)  # 则登录账号
            else:
                return render(request, "login.html", {"error": '登录验证失败'})
            return HttpResponseRedirect(reverse("index"))  # 重定向到首页
        return render(request, "login.html", {"error": '登录验证失败'})


class LogoutView(View):
    """
    用户注销表单
    """

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))  # 重定向到首页
