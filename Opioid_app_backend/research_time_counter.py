#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:55:50 2019

@author: dannywitt
"""
import numpy as np
import pandas as pd

class Research_month:
    
    def __init__(self):
        self.year = range(2,14)
        self.year_iterator = iter(self.year)
        self.current_month = 1
        self.months_remaining = 13 - self.current_month
        return 
    
    def __str__(self):
        return 'Patient\'s Current Research Enrollment Month: {}'.format(str(self.current_month))
    
    def New_month(self):
        self.current_month = self.year_iterator.__next__()
        return
