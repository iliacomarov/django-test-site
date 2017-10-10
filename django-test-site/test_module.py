#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''test_module.py - example of usage *args and **kvargs in functions'''

all_sales = (12.78, 14, 55.98)
all_sales2 = {'sale1': 4509.78, 'sale2': 123.67}

def daily_sales_total(*all_sales):
    total = 0.0
    for each_sale in all_sales:
        total += float(each_sale)
    return total


def daily_sales_total2(**all_sales2):
    total = 0.0
    for each_sale in all_sales2:
        total += float(all_sales2[each_sale])
    return total

def daily_sales_total3(*args):
    total = 0.0
    for each_sale in all_sales:
        total += float(each_sale)
    return total

def daily_sales_total4(**kwargs):
    total = 0.0
    for each_sale in all_sales2:
        total += float(all_sales2[each_sale])
    return total

print (daily_sales_total(10.90, 67.45))
print (daily_sales_total2())
print (daily_sales_total3())
print (daily_sales_total4())



