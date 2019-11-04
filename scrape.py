from urllib.request import urlopen
from bs4 import BeautifulSoup


def main():
    quote_page = 'https://www.stepstone.se/lediga-jobb-i-hela-sverige/data-it/'
    page = urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')

    # parse html
    job_list = soup.find_all('article', attrs={'data-id': ''})


    print('Debugging...')

if __name__ == '__main__':
    main()
