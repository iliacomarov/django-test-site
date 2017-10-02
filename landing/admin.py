#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *

class SubscriberAdmin(admin.ModelAdmin):
    #list_display = ["subscriber_name", "subscriber_email"]
    list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ["subscriber_name", "subscriber_email"]
    search_fields = ["subscriber_name", "subscriber_email"]

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)