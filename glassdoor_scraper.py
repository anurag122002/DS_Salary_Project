
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:47:59 2023

@author: kinwa
"""

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd

def get_jobs(keyword, num_jobs, verbose, path, slp_time):
    
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    
    #Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)

    url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + keyword + '"&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
    driver.get(url)
    jobs = []

    while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.

        #Let the page load. Change this number based on your internet speed.
        #Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(slp_time)

        #Test for the "Sign Up" prompt and get rid of it.
        try:
           driver.find_element_by_class_name("selected").click()
        except ElementClickInterceptedException:
            pass

        time.sleep(.1)

        try:
            element = driver.find_element_by_css_selector('div[class*="css-raue2m e1fx8g6d0"]')
            #clicking to the X.
            driver.execute_script("arguments[0].click();", element)
            
        except NoSuchElementException:
            print("Not worked")
            pass

    
        #Going through each job in this page
        try:
            job_buttons = driver.find_elements_by_class_name("react-job-listing")  #jl for Job Listing. These are the buttons we're going to click.
        except NoSuchElementException:
            print("Not Found")
        for job_button in job_buttons:  

            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break
            
            job_button.click()  #You might 
            time.sleep(1)
            collected_successfully = False
            
            while not collected_successfully:
                try:
                    try:
                        error_message = driver.find_element_by_xpath('//div[contains(@class, "css-1cci78o erj00if0")]')
                        if error_message:
                            break
                    except NoSuchElementException:
                    
                            company_name = driver.find_element_by_xpath('.//div[@class="css-87uc0g e1tk4kwz1"]').text
                            location = driver.find_element_by_xpath('.//div[@class="css-56kyx5 e1tk4kwz5"]').text
                            job_title = driver.find_element_by_xpath('.//div[contains(@class, "css-1vg6q84 e1tk4kwz4")]').text
                            job_description = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text
                            collected_successfully = True
                    
                except:
                    
                    time.sleep(5)
                    
                    
                    

            try:
                salary_estimate = driver.find_element_by_xpath('.//div[@class="salary-estimate"]').text
            except NoSuchElementException:
                print('Not worked2')
                salary_estimate = -1 #You need to set a "not found value. It's important."
            
            try:
                rating = driver.find_element_by_xpath('.//span[@class="css-1m5m32b e1tk4kwz2"]').text
            except NoSuchElementException:
                rating = -1 #You need to set a "not found value. It's important."

            #Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Job Description: {}".format(job_description[:500]))
                print("Rating: {}".format(rating))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))

            #Going to the Company tab...
            #clicking on this:
            #<div class="tab" data-tab-type="overview"><span>Company</span></div>
           

            

            try:
                size = driver.find_element_by_xpath('.//span[text()="Size"]//following-sibling::*').text
            except NoSuchElementException:
                size = -1

            try:
                founded = driver.find_element_by_xpath('.//span[text()="Founded"]//following-sibling::*').text
            except NoSuchElementException:
                founded = -1

            try:
                type_of_ownership = driver.find_element_by_xpath('.//span[text()="Type"]//following-sibling::*').text
            except NoSuchElementException:
                type_of_ownership = -1

            try:
                industry = driver.find_element_by_xpath('.//span[text()="Industry"]//following-sibling::*').text
            except NoSuchElementException:
                industry = -1

            try:
                sector = driver.find_element_by_xpath('.//span[text()="Sector"]//following-sibling::*').text
            except NoSuchElementException:
                sector = -1

            try:
                revenue = driver.find_element_by_xpath('.//span[text()="Revenue"]//following-sibling::*').text
            except NoSuchElementException:
                revenue = -1

                

            jobs.append({"Job Title" : job_title,
            "Salary Estimate" : salary_estimate,
            "Job Description" : job_description,
            "Rating" : rating,
            "Company Name" : company_name,
            "Location" : location,
            
            "Size" : size,
            "Founded" : founded,
            "Type of ownership" : type_of_ownership,
            "Industry" : industry,
            "Sector" : sector,
            "Revenue" : revenue,
            })
            #add job to jobs

        #Clicking on the "next page" button
        try:
            driver.find_element_by_css_selector('[alt="next-icon"]').click()
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break

    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.