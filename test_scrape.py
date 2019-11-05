"""This program scrapes www.stepstone.se for data&IT jobs and prints them to the console
Author:
    Roderick Karlemstrand
Date:
    3 Nov 2019

Copyright (c) waved, Roderick Karlemstrand - No Rights Reserved
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest


class TestStringMethods(unittest.TestCase):

    def test_scrape_jobs_in_single_category(self):
        quote_page = 'https://www.stepstone.se/lediga-jobb-i-hela-sverige/data-it/'
        page = urlopen(quote_page)
        soup = BeautifulSoup(page, 'html.parser')

        # parse html
        job_list = soup.find_all('article', attrs={'data-id': ''})
        self.assertNotEqual(job_list, [], 'The vacancy list is empty; '
                                          'there is probably something wrong with the website or the code')

        # parse the first job
        for job in job_list:
            job_company = job.find('span', attrs={'class': 'text-bold'}).text
            job_title = job.find('h5').text
            job_location = job.find('span', attrs={'class': 'subtitle'}).text.split('·')[1]

            self.assertNotEqual(job_company, None, 'The scraped company name is undefined')
            self.assertNotEqual(job_title, None, 'The scraped vacancy title is undefined')
            self.assertNotEqual(job_location, None, 'The scraped location is undefined')

    def test_scrape_categories(self):
        quote_page = 'https://www.stepstone.se'
        page = urlopen(quote_page)
        soup = BeautifulSoup(page, 'html.parser')

        # parse categories
        job_categories = soup.find(id='frontpage-category-list').find_all('a')

        self.assertNotEqual(job_categories, [], 'The category list is empty')

        for cat in job_categories:
            cat_with_no_of_jobs = cat.text
            # remove the number of jobs and extra space char at position -1
            job_cat = cat_with_no_of_jobs.split('(', 1)[0][0:-1]
            cat_url = cat['href']

            self.assertNotEqual(job_cat, None, 'The scraped category is undefined')
            self.assertNotEqual(cat_url, None, 'The scraped category url is undefined')


if __name__ == '__main__':
    unittest.main()
