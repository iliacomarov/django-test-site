#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
import datetime
from .forms import SubscriberForm

def landing(request):
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        #new_form = form.save()
        pass

    return render(request, 'landing/landing.html', locals())