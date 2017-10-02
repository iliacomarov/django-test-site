#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Subscriber (models.Model):
    subscriber_name = models.CharField(max_length=128)
    subscriber_email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.subscriber_name, self.subscriber_email)

