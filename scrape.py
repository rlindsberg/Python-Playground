"""This program scrapes www.stepstone.se for data&IT jobs and prints them to the console
Author:
    Roderick Karlemstrand
Date:
    3 Nov 2019

Copyright (c) waved, Roderick Karlemstrand - No Rights Reserved
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sqlite3


def main():
    # create database
    conn = sqlite3.connect('scraped_vacancies.sqlite')
    cur = conn.cursor()
    cur.execute('CREATE TABLE Vacancies (Vacancy_title VARCHAR, Company_name VARCHAR, Location VARCHAR)')
    conn.commit()

    # prepare for BeautifulSoup
    quote_page = 'https://www.stepstone.se/lediga-jobb-i-hela-sverige/data-it/'
    page = urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')

    # parse html
    job_list = soup.find_all('article', attrs={'data-id': ''})

    # parse the first job
    for job in job_list:
        job_company = job.find('span', attrs={'class': 'text-bold'}).text
        job_title = job.find('h5').text
        job_location = job.find('span', attrs={'class': 'subtitle'}).text.split('·')[1]
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Found a new job!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print(("%s; %s; %s \n\n" % (job_company, job_title, job_location)))

        # save job to database. SQL-injection is not welcomed
        cur.execute('INSERT INTO Vacancies (Vacancy_title, Company_name, Location) VALUES (?, ?, ?)',
                    (job_title, job_company, job_location))
        conn.commit()

    conn.close()

    print('Debugging...')

if __name__ == '__main__':
    main()
