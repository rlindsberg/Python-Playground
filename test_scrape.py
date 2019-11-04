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

    def test_scrape(self):
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

            self.assertNotEqual(job_company, None, 'The scraped company name is empty')
            self.assertNotEqual(job_title, None, 'The scraped vacancy title is empty')
            self.assertNotEqual(job_location, None, 'The scraped location is empty')


if __name__ == '__main__':
    unittest.main()
