# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 14:04:14 2023

@author: kinwa
"""

import glassdoor_scraper as gs
import pandas as pd

path = r"chromedriver.exe"

df = gs.get_jobs('data_scientist', 1000, False, path, 20)


df.to_csv('glassdoor_jobs.csv', index=False)