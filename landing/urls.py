#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^landing/', views.landing, name='landing'),
]