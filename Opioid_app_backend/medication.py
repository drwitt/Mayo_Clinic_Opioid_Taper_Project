#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 11:05:22 2019

@author: dannywitt
"""
import numpy as np
import pandas as pd

class Medication:
    
    def __init__(self,
                 med_name,
                 combination_state,
                 combination_drug_unit_doses,
                 delivery_rate,
                 drug_delivery_form,
                 available_opioid_doses,
                 available_combination_doses,
                 MME_conversion_factor):
        self.med_name = med_name
        self.combination_state = combination_state
        self.combination_drug_unit_doses = combination_drug_unit_doses
        self.delivery_rate = delivery_rate
        self.drug_delivery_form = drug_delivery_form
        self.available_opioid_unit_doses = available_opioid_doses
        self.minimum_dose_available = min(available_opioid_doses)
        self.combined_drug_name = self.is_combined_drug()
        self.available_combination_doses = available_combination_doses
        self.MME_conversion_factor = MME_conversion_factor
        
    def full_drug_name(self):
        return '{} ({}, {} form)'.format(self.med_name, 
                                self.delivery_rate,
                                self.drug_delivery_form)
        
    def is_combined_drug(self):
        if self.combination_state == 'Combined':
            self.combined_drug_name = self.med_name.split()[-1]
        else:
            self.combined_drug_name = 'Not Combined'
        return self.combined_drug_name
    
#Classes for each specific drug (inheriting from Medication class):
        
#Updated medications included in study, as of April 20, 2019:

class Hydrocodone_Acetaminophen(Medication):

    def __init__(self,
                 med_name = 'Hydrocodone Acetaminophen',
                 combination_state = 'Combined',
                 combination_drug_unit_doses = 325,
                 delivery_rate = 'Immediate Release',
                 drug_delivery_form = 'Capsule',
                 available_opioid_doses = [2.5, 5, 3.75, 7.5, 10],
                 #Include whole and "cut in half" doses:
                 available_combination_doses = [(2.5, 162.5),
                                                (3.75, 162.5),
                                                (5, 162.5),
                                                (5, 325),
                                                (7.5, 325), 
                                                (10, 325)],
                MME_conversion_factor = 1.0):
        super().__init__(med_name,
                         combination_state,
                         combination_drug_unit_doses,
                         delivery_rate,
                         drug_delivery_form,
                         available_opioid_doses,
                         available_combination_doses,
                         MME_conversion_factor)
        return

class Hydromorphone_Immediate_Release(Medication):
    
    def __init__(self,
                 med_name = 'Hydromorphone',
                 combination_state = 'Not Combined',
                 combination_drug_unit_doses = 'NA',
                 delivery_rate = 'Immediate Release',
                 drug_delivery_form = 'Tablet',
                 available_opioid_doses = [1, 2],
                 available_combination_doses = 'Not Combined',
                 MME_conversion_factor = 4.0):
        super().__init__(med_name,
                         combination_state,
                         combination_drug_unit_doses,
                         delivery_rate,
                         drug_delivery_form,
                         available_opioid_doses,
                         available_combination_doses,
                         MME_conversion_factor)
        return
    
class Morphine_Extended_Release(Medication):
    
    def __init__(self,
                 med_name = 'Morphine',
                 combination_state = 'Not Combined',
                 combination_drug_unit_doses = 'NA',
                 delivery_rate = 'Extended Release',
                 drug_delivery_form = 'Capsule',
                 available_opioid_doses = [7.5, 15, 30],
                 available_combination_doses = 'Not Combined',
                 MME_conversion_factor = 1.0):
        super().__init__(med_name,
                         combination_state,
                         combination_drug_unit_doses,
                         delivery_rate,
                         drug_delivery_form,
                         available_opioid_doses,
                         available_combination_doses, 
                         MME_conversion_factor)
        return

class Morphine_Immediate_Release(Medication):
    
    def __init__(self,
                 med_name = 'Morphine',
                 combination_state = 'Not Combined',
                 combination_drug_unit_doses = 'NA',
                 delivery_rate = 'Immediate Release',
                 drug_delivery_form = 'Capsule',
                 available_opioid_doses = [7.5, 15, 30],
                 available_combination_doses = 'Not Combined',
                 MME_conversion_factor = 1.0):
        super().__init__(med_name,
                         combination_state,
                         combination_drug_unit_doses,
                         delivery_rate,
                         drug_delivery_form,
                         available_opioid_doses,
                         available_combination_doses,
                         MME_conversion_factor)
        return

class Oxycodone_Immediate_Release(Medication):
    
    def __init__(self,
                 med_name = 'Oxycodone',
                 combination_state = 'Not Combined',
                 combination_drug_unit_doses = 'NA',
                 delivery_rate = 'Immediate Release',
                 drug_delivery_form = 'Capsule',
                 available_opioid_doses = [2.5, 5, 10, 20],
                 available_combination_doses = 'Not Combined',
                 MME_conversion_factor = 1.5):
        super().__init__(med_name,
                         combination_state,
                         combination_drug_unit_doses,
                         delivery_rate,
                         drug_delivery_form,
                         available_opioid_doses,
                         available_combination_doses,
                         MME_conversion_factor)
        return

class Oxycodone_Extended_Release(Medication):
    
    def __init__(self,
                 med_name = 'Oxycodone',
                 combination_state = 'Not Combined',
                 combination_drug_unit_doses = 'NA',
                 delivery_rate = 'Extended Release',
                 drug_delivery_form = 'Capsule',
                 available_opioid_doses = [2.5, 5, 10],
                 available_combination_doses = 'Not Combined',
                 MME_conversion_factor = 1.5):
        super().__init__(med_name,
                         combination_state,
                         combination_drug_unit_doses,
                         delivery_rate,
                         drug_delivery_form,
                         available_opioid_doses,
                         available_combination_doses,
                         MME_conversion_factor)
        return

class Oxycodone_Acetaminophen(Medication):
    
    def __init__(self,
                 med_name = 'Oxycodone Acetaminophen',
                 combination_state = 'Combined',
                 combination_drug_unit_doses = '325mg',
                 delivery_rate = 'Immediate Release',
                 drug_delivery_form = 'Tablet',
                 available_opioid_doses = [2.5, 5, 10],
                 available_combination_doses = [(2.5, 162.5),
                                                (5, 325),
                                                (5, 162.5),
                                                (10, 325)],
                 MME_conversion_factor = 1.5):
        super().__init__(med_name,
                         combination_state,
                         combination_drug_unit_doses,
                         delivery_rate,
                         drug_delivery_form,
                         available_opioid_doses,
                         available_combination_doses,
                         MME_conversion_factor)
        return

class Tramadol_Immediate_Release(Medication):
    
    def __init__(self,
                 med_name = 'Tramadol',
                 combination_state = 'Not Combined',
                 combination_drug_unit_doses = 'NA',
                 delivery_rate = 'Immediate Release',
                 drug_delivery_form = 'Capsule',
                 available_opioid_doses = [25, 50],
                 available_combination_doses = 'Not Combined',
                 MME_conversion_factor = 0.1):
        super().__init__(med_name,
                         combination_state,
                         combination_drug_unit_doses,
                         delivery_rate,
                         drug_delivery_form,
                         available_opioid_doses,
                         available_combination_doses,
                         MME_conversion_factor)
        return

##############################################################################
#Additional Medications (not used in current study implementation):
        
#class Hydromorphone_Extended_Release(Medication):
#    
#    def __init__(self,
#                 med_name = 'Hydromorphone',
#                 combination_state = 'Not Combined',
#                 combination_drug_unit_doses = 'NA',
#                 delivery_rate = 'Extended Release',
#                 drug_delivery_form = 'Tablet',
#                 available_opioid_doses = [8, 12, 16, 32],
#                 available_combination_doses = 'Not Combined',
#                 MME_conversion_factor = 4.0):
#        super().__init__(med_name,
#                         combination_state,
#                         combination_drug_unit_doses,
#                         delivery_rate,
#                         drug_delivery_form,
#                         available_opioid_doses,
#                         available_combination_doses,
#                         MME_conversion_factor)
#        return
#
#class Codeine_Acetaminophen(Medication):
#    
#    def __init__(self,
#                 med_name = 'Codeine Acetaminophen',
#                 combination_state = 'Combined',
#                 combination_drug_unit_doses = '300mg',
#                 delivery_rate = 'Immediate Release',
#                 drug_delivery_form = 'Tablet',
#                 available_opioid_doses = [15, 30, 60],
#                 available_combination_doses = [(15, 300),(30, 300), (60, 300)],
#                 MME_conversion_factor = 0.15):
#        super().__init__(med_name,
#                         combination_state,
#                         combination_drug_unit_doses,
#                         delivery_rate,
#                         drug_delivery_form,
#                         available_opioid_doses,
#                         available_combination_doses,
#                         MME_conversion_factor)
#        return
#
#class Codeine_Sulfate(Medication):
#    
#    def __init__(self,
#                 med_name = 'Codeine Sulfate',
#                 combination_state = 'Not Combined',
#                 combination_drug_unit_doses = 'NA',
#                 delivery_rate = 'Immediate Release',
#                 drug_delivery_form = 'Tablet',
#                 available_opioid_doses = [15, 30, 60],
#                 available_combination_doses = 'Not Combined',
#                 MME_conversion_factor = 0.15):
#        super().__init__(med_name,
#                         combination_state,
#                         combination_drug_unit_doses,
#                         delivery_rate,
#                         drug_delivery_form,
#                         available_opioid_doses,
#                         available_combination_doses,
#                         MME_conversion_factor)
#        return
#
#class Hydrocodone_Ibuprofen(Medication):
#    
#    def __init__(self,
#                 med_name = 'Hydrocodone Ibuprofen',
#                 combination_state = 'Combined',
#                 combination_drug_unit_doses = '300mg',
#                 delivery_rate = 'Immediate Release',
#                 drug_delivery_form = 'Tablet',
#                 available_opioid_doses = [2.5, 5, 7.5, 10],
#                 available_combination_doses = [(2.5, 200), 
#                                                (5, 200), 
#                                                (7.5, 200), 
#                                                (10, 200)],
#                MME_conversion_factor = 1.0):
#        super().__init__(med_name,
#                         combination_state,
#                         combination_drug_unit_doses,
#                         delivery_rate,
#                         drug_delivery_form,
#                         available_opioid_doses,
#                         available_combination_doses,
#                         MME_conversion_factor)
#        return
#
#class Meperidine_Hydrochloride(Medication):
#    
#    def __init__(self,
#                 med_name = 'Meperidine Hydrochloride',
#                 combination_state = 'Not Combined',
#                 combination_drug_unit_doses = 'NA',
#                 delivery_rate = 'Immediate Release',
#                 drug_delivery_form = 'Tablet',
#                 available_opioid_doses = [50, 100],
#                 available_combination_doses = 'Not Combined',
#                 MME_conversion_factor = 0.1):
#        super().__init__(med_name,
#                         combination_state,
#                         combination_drug_unit_doses,
#                         delivery_rate,
#                         drug_delivery_form,
#                         available_opioid_doses,
#                         available_combination_doses,
#                         MME_conversion_factor)
#        return
#
#class Morphine_Extended_Release_Tablet(Medication):
#    
#    def __init__(self,
#                 med_name = 'Morphine',
#                 combination_state = 'Not Combined',
#                 combination_drug_unit_doses = 'NA',
#                 delivery_rate = 'Extended Release',
#                 drug_delivery_form = 'Tablet',
#                 available_opioid_doses = [15, 30, 45, 60, 100, 200],
#                 available_combination_doses = 'Not Combined',
#                 MME_conversion_factor = 1.0):
#        super().__init__(med_name,
#                         combination_state,
#                         combination_drug_unit_doses,
#                         delivery_rate,
#                         drug_delivery_form,
#                         available_opioid_doses,
#                         available_combination_doses,
#                         MME_conversion_factor)
#        return
#    
#class Oxycodone_Immediate_Release_Tablet(Medication):
#    
#    def __init__(self,
#                 med_name = 'Oxycodone',
#                 combination_state = 'Not Combined',
#                 combination_drug_unit_doses = 'NA',
#                 delivery_rate = 'Immediate Release',
#                 drug_delivery_form = 'Tablet',
#                 available_opioid_doses = [5, 10, 15, 20, 30],
#                 available_combination_doses = 'Not Combined',
#                 MME_conversion_factor = 1.5):
#        super().__init__(med_name,
#                         combination_state,
#                         combination_drug_unit_doses,
#                         delivery_rate,
#                         drug_delivery_form,
#                         available_opioid_doses,
#                         available_combination_doses,
#                         MME_conversion_factor)
#        return
#    
#class Oxycodone_Aspirin(Medication):
#    
#    def __init__(self,
#                 med_name = 'Oxycodone Aspirin',
#                 combination_state = 'Combined',
#                 combination_drug_unit_doses = '325mg',
#                 delivery_rate = 'Immediate Release',
#                 drug_delivery_form = 'Tablet',
#                 available_opioid_doses = [4.8355],
#                 available_combination_doses = [(4.8355, 325)],
#                 MME_conversion_factor = 1.5):
#        super().__init__(med_name,
#                         combination_state,
#                         combination_drug_unit_doses,
#                         delivery_rate,
#                         drug_delivery_form,
#                         available_opioid_doses,
#                         available_combination_doses, 
#                         MME_conversion_factor)
#        return
#
#class Oxycodone_Ibuprofen(Medication):
#    
#    def __init__(self,
#                 med_name = 'Oxycodone Ibuprofen',
#                 combination_state = 'Combined',
#                 combination_drug_unit_doses = '400mg',
#                 delivery_rate = 'Immediate Release',
#                 drug_delivery_form = 'Tablet',
#                 available_opioid_doses = [5],
#                 available_combination_doses = [(5, 400)],
#                 MME_conversion_factor = 1.5):
#        super().__init__(med_name,
#                         combination_state,
#                         combination_drug_unit_doses,
#                         delivery_rate,
#                         drug_delivery_form,
#                         available_opioid_doses,
#                         available_combination_doses,
#                         MME_conversion_factor)
#        return
#
#class Oxymorphone_Immediate_Release(Medication):
#    
#    def __init__(self,
#                 med_name = 'Oxymorphone',
#                 combination_state = 'Not Combined',
#                 combination_drug_unit_doses = 'NA',
#                 delivery_rate = 'Immediate Release',
#                 drug_delivery_form = 'Tablet',
#                 available_opioid_doses = [5, 10],
#                 available_combination_doses = 'Not Combined',
#                 MME_conversion_factor = 3.0):
#        super().__init__(med_name,
#                         combination_state,
#                         combination_drug_unit_doses,
#                         delivery_rate,
#                         drug_delivery_form,
#                         available_opioid_doses,
#                         available_combination_doses,
#                         MME_conversion_factor)
#        return
#    
#class Oxymorphone_Extended_Release(Medication):
#    
#    def __init__(self,
#                 med_name = 'Oxymorphone',
#                 combination_state = 'Not Combined',
#                 combination_drug_unit_doses = 'NA',
#                 delivery_rate = 'Extended Release',
#                 drug_delivery_form = 'Tablet',
#                 available_opioid_doses = [5, 7.5, 10, 15, 20, 30, 40],
#                 available_combination_doses = 'Not Combined',
#                 MME_conversion_factor = 3.0):
#        super().__init__(med_name,
#                         combination_state,
#                         combination_drug_unit_doses,
#                         delivery_rate,
#                         drug_delivery_form,
#                         available_opioid_doses,
#                         available_combination_doses,
#                         MME_conversion_factor)
#        return
#
#class Tramadol_Extended_Release(Medication):
#    
#    def __init__(self,
#                 med_name = 'Tramadol',
#                 combination_state = 'Not Combined',
#                 combination_drug_unit_doses = 'NA',
#                 delivery_rate = 'Extended Release',
#                 drug_delivery_form = 'Tablet',
#                 available_opioid_doses = [100, 200, 300],
#                 available_combination_doses = 'Not Combined',
#                 MME_conversion_factor = 0.1):
#        super().__init__(med_name,
#                         combination_state,
#                         combination_drug_unit_doses,
#                         delivery_rate,
#                         drug_delivery_form,
#                         available_opioid_doses,
#                         available_combination_doses,
#                         MME_conversion_factor)
#        return  
#    
#class Tramadol_Acetaminophen(Medication):
#    
#    def __init__(self,
#                 med_name = 'Tramadol Acetaminophen',
#                 combination_state = 'Combined',
#                 combination_drug_unit_doses = '325mg',
#                 delivery_rate = 'Immediate Release',
#                 drug_delivery_form = 'Tablet',
#                 available_opioid_doses = [37.5],
#                 available_combination_doses = [(37.5, 325)],
#                 MME_conversion_factor = 0.1):
#        super().__init__(med_name,
#                         combination_state,
#                         combination_drug_unit_doses,
#                         delivery_rate,
#                         drug_delivery_form,
#                         available_opioid_doses,
#                         available_combination_doses,
#                         MME_conversion_factor)
#        return
