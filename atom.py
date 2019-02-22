import requests, csv
from datetime import datetime
from bs4 import BeautifulSoup
from multiprocessing import Pool


def get_html(url):
    response = requests.get(url)
    return response.text

def get_links(html):
    soup = BeautifulSoup(html, 'lxml')
    tds = soup.find('table', id='currencies-all').find_all('td', class_='currency-name')
    links = []
    for td in tds:
        a = td.find('a', class_='link-secondary').get('href')
        link = 'https://coinmarketcap.com' + a
        links.append(link)
    return links

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        name = soup.find('h1', class_='details-panel-item--name').text.strip()
    except:
        name = ''
    try:
        price = soup.find('span', class_='details-panel-item--price__value').text.strip()
    except:
        price = ''
    data = {'name': name,
            'price': price}
    return data

def write_csv(data):
    with open('cmc.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow( (data['name'],
                        data['price']) )

        print(data['name'], ' parsed')

def make_all(url):
    html = get_html(url)
    data = get_page_data(html)
    write_csv(data)

def main():
    start = datetime.now()

    url = 'https://coinmarketcap.com/all/views/all/' # https://www.youtube.com/watch?time_continue=2886&v=IGPUs49a1Zo
    all_links = get_links(get_html(url))

    with Pool(40) as p:
        p.map(make_all, all_links)

    end = datetime.now()
    total = end - start




hi
if __name__ == '__main__':
    main()
