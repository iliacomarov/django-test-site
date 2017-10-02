#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Subscribers (models.Model):
    subscriber_name = models.CharField(max_length=128)
    subscriber_email = models.EmailField()

