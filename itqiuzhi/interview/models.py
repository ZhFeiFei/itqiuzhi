# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.models import AbstractUser

from DjangoUeditor.models import UEditorField
from django.db import models


# Create your models here.
class User(AbstractUser):
    """
    用户表
    """
    # username = models.CharField(verbose_name="用户姓名", max_length=50)
    # email = models.CharField(verbose_name="邮箱", max_length=50)
    # password = models.CharField(verbose_name="密码", max_length=128)
    mobile = models.CharField(verbose_name="手机", max_length=11, blank=True, null=True)
    birthday = models.DateField(verbose_name="生日", blank=True, null=True)
    gen = (
        ("male", "男"),
        ("female", "女")
    )
    gender = models.CharField(verbose_name="性别", choices=gen, default="male", max_length=10)
    image = models.ImageField(verbose_name="图片", upload_to="user/%Y/%m", blank=True, null=True)

    # 使后台管理变为中文描述
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class Author(models.Model):
    """
    发布人表
    """
    name = models.CharField(verbose_name="发布人姓名", max_length=50)
    image = models.ImageField(verbose_name="头像", upload_to="author/%Y/%m")
    position = models.CharField(verbose_name="职位", max_length=50)

    # 使后台管理变为中文描述
    class Meta:
        verbose_name = "发布人"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Interview(models.Model):
    """
    招聘详情
    """
    title = models.CharField(verbose_name="标题", max_length=50)
    salarys = (
        ("s1", "2k以下"),
        ("s2", "2k-5k"),
        ("s3", "5k-10k"),
        ("s4", "10k-15k"),
        ("s5", "15k-25k"),
        ("s6", "25k-50k"),
        ("s7", "50k以上"),
    )
    salary = models.CharField(verbose_name="薪资", choices=salarys, default="s4", max_length=20)
    educations = (
        ("e1", "不限"),
        ("e2", "中专及以下"),
        ("e3", "高中"),
        ("e4", "大专"),
        ("e5", "本科"),
        ("e6", "硕士"),
        ("e7", "博士"),
    )
    education = models.CharField(verbose_name="学历", choices=educations, default="e1", max_length=20)
    des = models.CharField(verbose_name="职位描述", max_length=20)
    # content = models.TextField(verbose_name="公司内容")
    content = UEditorField(verbose_name="内容", width=700, height=200, default="",
                           imagePath="content/%(basename)s_/%(datetime)s.%(extname)s",
                           filePath="content/%(basename)s_/%(datetime)s.%(extname)s")
    workTypes = (
        ("w1", "不限"),
        ("w2", "全职"),
        ("w3", "兼职"),
        ("w4", "实习"),
    )
    workType = models.CharField(verbose_name="工作性质", choices=workTypes, default="w1", max_length=20)
    image = models.ImageField(verbose_name="图片", upload_to="interview/%Y/%m")
    author = models.ForeignKey(Author, verbose_name="所属发布人")
    company = models.CharField(verbose_name="公司", max_length=50)
    years = (
        ("y1", "不限"),
        ("y2", "应届生"),
        ("y3", "1年以内"),
        ("y4", "1-3年"),
        ("y5", "3-5年"),
        ("y6", "5-10年"),
        ("y7", "10年以上"),
    )
    yearsRequire = models.CharField(verbose_name="工作经验", choices=years, default="y1", max_length=20)
    trades = (
        ("t1", "技术"),
        ("t2", "产品"),
        ("t3", "设计"),
        ("t4", "运营"),
        ("t5", "市场销售"),
        ("t6", "职能"),
        ("t7", "金融"),
        ("t8", "文案公关"),
        ("t9", "教师"),
        ("t10", "校招"),
    )
    trade = models.CharField(verbose_name="行业", choices=trades, default="t1", max_length=10)
    domain = models.CharField(verbose_name="公司领域", max_length=20)
    scales = (
        ("s1", "不限"),
        ("s2", "0-19人"),
        ("s3", "20-99人"),
        ("s4", "100-499人"),
        ("s5", "500-999人"),
        ("s6", "1000-9999人"),
        ("s7", "10000人以上"),
    )
    scale = models.CharField(verbose_name="公司规模", choices=scales, default="s1", max_length=20)
    moments = (
        ("m1", "不限"),
        ("m2", "未融资"),
        ("m3", "天使轮"),
        ("m4", "A轮"),
        ("m5", "B轮"),
        ("m6", "C轮"),
        ("m7", "D轮"),
        ("m8", "D轮以上"),
        ("m9", "已上市"),
        ("m10", "不需要融资"),
    )
    moment = models.CharField(verbose_name="目前公司阶段", choices=moments, default="m1", max_length=10)
    companyHome = models.URLField(verbose_name="公司首页", max_length=100)
    welfare1 = models.CharField(verbose_name="公司福利1", max_length=10, blank=True, null=True)
    welfare2 = models.CharField(verbose_name="公司福利2", max_length=10, blank=True, null=True)
    welfare3 = models.CharField(verbose_name="公司福利3", max_length=10, blank=True, null=True)
    locations = (
        ("l1", "北京"),
        ("l2", "上海"),
        ("l3", "天津"),
        ("l4", "广州"),
        ("l5", "杭州"),
        ("l6", "深圳"),
        ("l7", "其他"),
    )
    location = models.CharField(verbose_name="工作地区", choices=locations, default="l1", max_length=10)
    map = models.URLField(verbose_name="工作地图", max_length=100)
    pub_time = models.DateTimeField(verbose_name="发布时间", default=datetime.now)
    read_counts = models.IntegerField(verbose_name="阅读次数", default=0)

    # 使后台管理变为中文描述
    class Meta:
        verbose_name = "详情"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Image(models.Model):
    """
    图片设计合计
    """
    name = models.CharField(verbose_name="轮播图片名称", max_length=10)
    homeImage = models.ImageField(verbose_name="轮播图", upload_to="images/%Y/%m", blank=True, null=True)
    homeImageSmall = models.ImageField(verbose_name="小轮播图", upload_to="images/%Y/%m", blank=True, null=True)
    recommend_Image = models.ImageField(verbose_name="面包屑推荐图", upload_to="images/%Y/%m", blank=True, null=True)

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
