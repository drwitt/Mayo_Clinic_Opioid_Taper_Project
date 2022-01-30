#!/usr/bin/env python

from redcap import Project

def api_get():
    """
    Use PyCap API access

    url: https://pycap.readthedocs.io/en/latest/index.html

    citation: Burns, S. S., Browne, A., Davis, G. N., Rimrodt, S. L., & Cutting,
    L. E. PyCap (Version 1.0) [Computer Software]. Nashville, TN: Vanderbilt
    University and Philadelphia, PA: Childrens Hospital of Philadelphia.
    Available from https://github.com/sburns/PyCap. doi:10.5281/zenodo.9917
    """

    api_key = 'DEBB8885432E076DFCBA7BE262B8B228'
    api_url = 'https://redcapcln4-prod.mayo.edu/redcap/api/'

    project = Project(api_url, api_key, verify_ssl=False)
    
    #Options for data export FROM RedCap:

    #post GET call for all data in RedCap project:
    #data = project.export_records()

    #Identify subset of REDCap IDs:
    rc_ids = ['100', '102', '103', '104', '105']

    #post GET call to REDCap to export data depending on args:
    data = project.export_records(records=rc_ids)

    return data

def api_post(patient_month_vars):
    """
    Arg: <patient_month_output> is a list object of variables which correspond to the
    <output_field_names> list of keys/field names; the list will have the same 
    length as the <output_field_names> list
        
    Use PyCap API access

    url: https://pycap.readthedocs.io/en/latest/index.html

    citation: Burns, S. S., Browne, A., Davis, G. N., Rimrodt, S. L., & Cutting,
    L. E. PyCap (Version 1.0) [Computer Software]. Nashville, TN: Vanderbilt
    University and Philadelphia, PA: Childrens Hospital of Philadelphia.
    Available from https://github.com/sburns/PyCap. doi:10.5281/zenodo.9917
    """

    api_key = 'DEBB8885432E076DFCBA7BE262B8B228'
    api_url = 'https://redcapcln4-prod.mayo.edu/redcap/api/'

    project = Project(api_url, api_key, verify_ssl=False)

    #Options for data import TO RedCap (e.g. data = project.import_records())
    
    #Create list of field names to serve as keys in dictionary, which will 
    #be POSTED to RedCap via API:
    
    output_field_names = ['study_id',
                        'redcap_event_name', #variable = 'month_1_arm_1'
                        'first_name_taper_out',
                        'last_name_taper_out',
                        'prim_opioid_name_out',
                        'total_med_1_24_hr_dose',
                        'total_med_1_24_hr_mme',
                        'sec_opioid_name_out',
                        'total_med_2_24_hr_dose',
                        'total_med_2_24_hr_mme',
                        'pre_taper_mme',
                        'total_mme',
                        'percent_mme_decrease',
                        'med_1_episode_1',
                        'med_1_episode_1_dose',
                        'med_1_episode_1_dose_freq',
                        'med_1_episode_1_unit_dose',
                        'med_1_episode_1_active_cap',
                        'med_1_episode_1_placeb_cap',
                        'med_1_episode_1_total_cap',
                        'med_2_episode_1',
                        'med_2_episode_1_dose',
                        'med_2_episode_1_dose_freq',
                        'med_2_episode_1_unit_dose',
                        'med_2_episode_1_active_cap',
                        'med_2_episode_1_placeb_cap',
                        'med_2_episode_1_total_cap',
                        'med_1_episode_2',
                        'med_1_episode_2_dose',
                        'med_1_episode_2_dose_freq',
                        'med_1_episode_2_unit_dose',
                        'med_1_episode_2_active_cap',
                        'med_1_episode_2_placeb_cap',
                        'med_1_episode_2_total_cap',
                        'med_2_episode_2',
                        'med_2_episode_2_dose',
                        'med_2_episode_2_dose_freq',
                        'med_2_episode_2_unit_dose',
                        'med_2_episode_2_active_cap',
                        'med_2_episode_2_placeb_cap',
                        'med_2_episode_2_total_cap',
                        'med_1_episode_1',
                        'med_1_episode_3_dose',
                        'med_1_episode_3_dose_freq',
                        'med_1_episode_3_unit_dose',
                        'med_1_episode_3_active_cap',
                        'med_1_episode_3_placeb_cap',
                        'med_1_episode_3_total_cap',
                        'med_2_episode_3',
                        'med_2_episode_3_dose',
                        'med_2_episode_3_dose_freq',
                        'med_2_episode_3_unit_dose',
                        'med_2_episode_3_active_cap',
                        'med_2_episode_3_placeb_cap',
                        'med_2_episode_3_total_cap',
                        'med_1_episode_4',
                        'med_1_episode_4_dose',
                        'med_1_episode_4_dose_freq',
                        'med_1_episode_4_unit_dose',
                        'med_1_episode_4_active_cap',
                        'med_1_episode_4_placeb_cap',
                        'med_1_episode_4_total_cap',
                        'med_2_episode_4',
                        'med_2_episode_4_dose',
                        'med_2_episode_4_dose_freq',
                        'med_2_episode_4_unit_dose',
                        'med_2_episode_4_active_cap',
                        'med_2_episode_4_placeb_cap',
                        'med_2_episode_4_total_cap'
                        ]
                        
                        
    
    patient_month_out_dict = dict(list(zip(output_field_names, patient_month_vars)))
    project.import_records([patient_month_out_dict])
    
    return 

