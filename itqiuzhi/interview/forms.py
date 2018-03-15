# -*- coding: utf-8 -*-
from django import forms


class RegForm(forms.Form):
    """
    用户注册表单
    """
    email = forms.EmailField(required=True, max_length=100, error_messages={"required": "邮箱不能为空"})
    password = forms.CharField(required=True, max_length=8, error_messages={"required": "密码不能为空"})


class LoginForm(forms.Form):
    """
    用户登录表单
    """
    email = forms.EmailField(required=True, max_length=100, error_messages={"required": "邮箱不能为空"})
    password = forms.CharField(required=True, max_length=8, error_messages={"required": "密码不能为空"})
