#!/usr/bin/env python
# -*- coding: utf-8 -*-

from GSCD_1106 import GSCD
GSCD = GSCD()
data = GSCD.readexcel("test.xlsx",u"指标")
GSCD.line_chart(data)
degree = GSCD.cal_GSCD(data)
print GSCD.factor_sort(degree)



