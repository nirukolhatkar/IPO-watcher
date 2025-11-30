import requests
from bs4 import BeautifulSoup


def scrape_ipowatch():
    url = 'https://ipowatch.in/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example: Finding IPO details (you will need to adjust based on actual site structure)
    ibo_details = []
    for ipo in soup.find_all('div', class_='ipo-details'):
        title = ipo.find('h2').text
        gmp = ipo.find('span', class_='gmp').text
        ibo_details.append({'Title': title, 'GMP': gmp})

    return ibo_details


if __name__ == '__main__':
    details = scrape_ipowatch()
    for detail in details:
        print(detail)