import requests
from bs4 import BeautifulSoup as bs
import re


def get_response(url, prms, headers):
	session = requests.Session()
	response = session.get(url, params = prms, headers = headers)
	if response.status_code == 200:
		return response
	else:
		return 'Error'


def get_vacancyes(response):
	vacancyes = []
	soup = bs(response.content, 'html.parser')
	divs = soup.find_all('div', attrs = {'data-qa': 'vacancy-serp__vacancy'})
	for div in divs:
		title = div.find('a', attrs = {'data-qa': 'vacancy-serp__vacancy-title'}).text
		link = div.find('a', attrs = {'data-qa': 'vacancy-serp__vacancy-title'})['href']
		compensation_test = div.find('div', attrs = {'class': 'vacancy-serp-item__compensation'})

		if compensation_test is not None:
			compensation = compensation_test.text
		else:
			compensation = '-'

		vacancyes.append({
			'title': title,
			'link': link,
			'compensation': compensation
		})
	return vacancyes

def pretty(vacancyes_dict):
	for vacancy in vacancyes_dict:
		print('-------------------------------------------------------------------------')
		print(f'*{ vacancy["title"] }* | зарплата: { vacancy["compensation"] }')
		print(vacancy['link'])
		print()




# response = requests.get('https://hh.ru/search/vacancy', params = keys, headers = headers)
search_text = input('Enter search query: ')
url = 'https://hh.ru/search/vacancy'
keys = {'text': f'{search_text}', 'area': '1', 'from': 'suggest_post', 'page': '0'}
headers = {
	'accept': '*/*',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}



if __name__ == '__main__':
	all_vacancyes = get_vacancyes( get_response(url, keys, headers) )
	pretty(all_vacancyes)
