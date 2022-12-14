#write a python program to find all the jobs from this url  'https://www.linkedin.com/jobs/data-scientist-jobs?position=1&pageNum=0&currentJobId=3390271556' and save information about those jobs to a csv fiel

import re
import requests
from bs4 import BeautifulSoup
import csv
import os 
from time import sleep

HEADERS = {
    'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64)'
                    'AppleWebKit/537.36 (KHTML, like Gecko)'
                    'Chrome/44.0.2403.157 Safari/537.36'),
    'Accept-Language': 'en-US, en;q=0.5'
}

def extract_records():
    url = 'https://www.linkedin.com/jobs/data-scientist-jobs?position=1&pageNum=0&currentJobId=3390271556'
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    jobs = soup.find_all('li')
    
    for job in jobs:
        try:
            company_parent = job.find('h4', class_='base-search-card__subtitle')
            job_parent = job.find('div', class_='base-search-card__info')
            job_title = job_parent.find('h3', class_='base-search-card__title').text
            company = company_parent.find('a', class_='hidden-nested-link').text
            job_location_parent = job.find('div', class_='base-search-card__metadata')
            job_location = job_location_parent.find('span', class_='job-search-card__location').text
            date_posted = job_location_parent.find('time', class_='job-search-card__listdate').text
            job_link = job.find('a', class_='base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]').get('href')
            result = (job_title, company, job_location,date_posted , job_link)
            print(result)
            #remove all space from the result
            result = [x.strip() for x in result]
            write_to_csv(result)

        except:
            pass
        
        

def write_to_csv(result):

    with open('jobs.csv', 'a', newline='') as f:
        #name the columns after the variables in the result
        fieldnames = ['job_title', 'company', 'job_location', 'job_link']
        writer = csv.writer(f)
        writer.writerow(result)

  
        


extract_records()

print('code completed')