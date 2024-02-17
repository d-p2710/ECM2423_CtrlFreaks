# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 12:31:47 2024

@author: theow
"""

from django.urls import path

from .views import SignUpView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]