#!/usr/bin/env python

from redcap import Project

def api_get():
    api_key = 'DEBB8885432E076DFCBA7BE262B8B228'
    api_url = 'https://redcapcln4-prod.mayo.edu/redcap/api/'

    project = Project(api_url, api_key, verify_ssl=False)

    #post GET call for all data in RedCap project:
    data = project.export_records()
    return data
