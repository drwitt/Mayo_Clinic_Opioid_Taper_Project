#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 11:05:22 2019

@author: dannywitt
"""
#import pandas as pd
#import numpy as np

from RedCap_API.api_connect import api_get
from RedCap_API.api_connect import api_post

from Opioid_app_backend.construct_patients import Patient_Builder
from Opioid_app_backend.opioid_dose_taper import Taper
from Opioid_app_backend.prescription import Prescription
from Opioid_app_backend.prepare_redcap_output import Generate_first_patient_month_list, Generate_patient_month_list
#from Opioid_app_backend.print_report import Print_monthly_report

import requests
requests.packages.urllib3.disable_warnings() 

print('Running main.py...\n')


def generate_patient_output(patient):

      #Generate patient information:
      print('Generating taper for: \n\tName: {} \n\tSubject ID: {}\n'.format(patient.first_name, patient.ID_number))
      
      #Step 1: Print monthly report #1 (Month 1 for given patient)

      #Month 1:

      first_patient_row = Generate_first_patient_month_list(patient)
      
      #Submit month #1 to RedCap:
          
      api_post(first_patient_row)
      
      #Step 3: For months 2-12, print reports for months 2-12 for given patient:

      #Month 2-12:

      for month in range(2,13):
           #Execute new month:
           patient.research_study_timer.New_month()
           
           #Execute Taper:
           taper = Taper(patient)
           
           #Execute prescription object HERE:
           prescription = Prescription(patient,
                                       taper)
           
           #Print out (for testing purposes)
           #Print_monthly_report(patient)
           
           #Generate patient list:
           new_patient_row = Generate_patient_month_list(patient,
                                                         month,
                                                         prescription)
          
           #Submit POST for current patient-month data to RedCap:
           api_post(new_patient_row)
          
           pass
      return


def main():
    #Launch api GET call (RedCap to local server):
    print('Connecting to Mayo RedCap server.\n')
    payload = api_get()
    
    #Ingest payload, check data, and construct patient instances:
    print('Building patient objects.\n')
    patient_obj_list = Patient_Builder(payload).build_patients()
    
    #Iterate through patient objects, apply taper, and generate prescription
    #information for each month:
    for patient in patient_obj_list:
        generate_patient_output(patient)
       
    #Generate taper report (output file):

    #Safety Check:

    return

if __name__ == '__main__':
    main()





