#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(max_length=256, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.product_name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = "ProductImage"
        verbose_name_plural = "ProductImages"