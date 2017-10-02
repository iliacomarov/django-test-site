#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import *

class SubscriberForm (forms.ModelForm):
    class Meta:
        model = Subscribers
        exclude = [""]
