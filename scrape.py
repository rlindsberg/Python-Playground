from urllib.request import urlopen
from bs4 import BeautifulSoup


def main():
    quote_page = 'https://www.stepstone.se/lediga-jobb-i-hela-sverige/data-it/'
    page = urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')

    # parse html
    job_list = soup.find_all('article', attrs={'data-id': ''})

    # parse the first job
    job_company = job_list[0].find('span', attrs={'class': 'text-bold'}).text
    job_title = job_list[0].find('h5').text
    job_location = job_list[0].find('span', attrs={'class': 'subtitle'}).text.split('·')[1]

    print('Debugging...')

if __name__ == '__main__':
    main()
