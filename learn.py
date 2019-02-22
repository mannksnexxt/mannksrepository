# todo = ['Milk', 'Bread', 'Cocount', 'Apple']
# count = 1
# def showList(arr, count):
# 	for i in todo:
# 		print('{}: {}'.format(count, i))
# 		count += 1

# showList(todo, count)



# new_user = []
# attrs = ['name', 'age', 'speciality']

# user_name = input('Your name: ')
# new_user.append(user_name)

# user_age = int(input('Your age: '))
# new_user.append(user_age)

# user_spec = input('Your speciality: ')
# new_user.append(user_spec)

# with open('users.txt', 'w') as file:
# 	for i, j in enumerate(attrs):
# 		text = ('{}: {}\n').format(attrs[i], new_user[i])
# 		file.write(text)

# import csv

# with open('table.csv', 'r') as file:
# 	item = csv.reader(file)
# 	for word in item:
# 		print(', '.join(word))

# import random as rd

# def hungman(word):
# 	wrong = 0
# 	stages = ["",
# 		"________         ",
# 		"|       |        ",
# 		"|       |        ",
# 		"|       |        ",
# 		"|       o        ",
# 		"|      /|\\       ",
# 		"|      / \\       ",
# 		"|                "
# 	]
# 	rletters = list(word)
# 	board = ['_'] * len(word)
# 	win = False
# 	print('Welcome to execution!')
# 	print(' '.join(board))

# 	while wrong < len(stages) - 1:
# 		print('\n')
# 		char = input('Enter char: ')
# 		if char in rletters:
# 			cind = rletters.index(char)
# 			board[cind] = char
# 			rletters[cind] = '$'
# 		else:
# 			wrong += 1
# 		print((" ".join(board)))
# 		e = wrong + 1
# 		print('\n'.join(stages[0: e]))
# 		if "_" not in board:
# 			print('You are winner! The word: {}'.format(word))
# 			win = True
# 			break
# 	if not win:
# 		print('You are loser! The word: {}'.format(word))

# words = ['кулинария', 'парадигма', 'президент', 'машина', 'паровоз', 'самолет', 'праздник']
# rd_word = words[rd.randint(0, len(words))]
# hungman(rd_word)


# from random import randint as rint

# rd = rint(100, 999)

# def summ_tripple_num(num):
# 	new_num = str(num)
# 	full_summ = 0
# 	for i in new_num:
# 		full_summ += int(i)
# 	return full_summ

# print(rd)
# print(summ_tripple_num(rd))


# class Triangle:
# 	def __init__(self, a, b, c):
# 		self.cath_a = a
# 		self.cath_b = b
# 		self.hypot = c
# 	def get_area(self):
# 		return (self.cath_a * self.cath_b) / 2
# 	def get_perimeter(self):
# 		return self.cath_a + self.cath_b + self.hypot

# triang = Triangle(3, 9, 8)

# print(triang.get_area())
# print(triang.get_perimeter())



# from random import shuffle

# class Card:
# 	suits = ['пикей', 'червей', 'бубей', 'крестей']
# 	values = [
# 		None, None, '2', '3', '4', '5',
# 		'6', '7', '8', '9', '10', 'валета',
# 		'даму', 'короля', 'туза'
# 	]
# 	def __init__(self, v, s):
# 		self.suit = s
# 		self.value = v

# 	def __lt__(self, c2):
# 		if self.value < c2.value:
# 			return True
# 		if self.value == c2.value:
# 			if self.suit < c2.suit:
# 				return True
# 			else:
# 				return False
# 		return False

# 	def __gt__(self, c2):
# 		if self.value > c2.value:
# 			return True
# 		if self.value == c2.value:
# 			if self.suit > c2.suit:
# 				return True
# 			else:
# 				return False
# 		return False

# 	def __repr__(self):
# 		v = self.values[self.value] + ' ' + self.suits[self.suit]
# 		return v


# class Deck:
# 	def __init__(self):
# 		self.cards = []
# 		for i in range(2, 15):
# 			for j in range(4):
# 				self.cards.append(Card(i, j))
# 		shuffle(self.cards)

# 	def rm_card(self):
# 		if len(self.cards) == 0:
# 			return
# 		return self.cards.pop()

# class Player:
# 	def __init__(self, name):
# 		self.wins = 0
# 		self.card = None
# 		self.name = name

# class Game:
# 	def __init__(self):
# 		name1 = input('имя игрока 1: ')
# 		name2 = input('имя игрока 2: ')
# 		self.deck = Deck()
# 		self.p1 = Player(name1)
# 		self.p2 = Player(name2)

# 	def wins(self, winner):
# 		w = '{} забирает карты'.format(winner)
# 		print(w)

# 	def draw(self, p1_name, p1_card, p2_name, p2_card):
# 		d = '{} кладет {}, а {} кладет {}'.format(p1_name, p1_card, p2_name, p2_card)
# 		print(d)

# 	def play_game(self):
# 		cards = self.deck.cards
# 		print('Lets go!')
# 		while len(cards) >= 2:
# 			response = input('Нажмите любую клавишу для начала игры. Выход - X.')
# 			if response == 'X':
# 				break
# 			p1_card = self.deck.rm_card()
# 			p2_card = self.deck.rm_card()
# 			p1_name = self.p1.name
# 			p2_name = self.p2.name
# 			self.draw(p1_name, p1_card, p2_name, p2_card)
# 			if p1_card > p2_card:
# 				self.p1.wins += 1
# 				self.wins(self.p1.name)
# 			else:
# 				self.p2.wins += 1
# 				self.wins(self.p2.name)
# 		win = self.winner(self.p1, self.p2)
# 		print('Игра окончена. Победил {}'.format(win))

# 	def winner(self, p1, p2):
# 		if p1.wins > p2.wins:
# 			return p1.name
# 		if p1.wins < p2.wins:
# 			return p2.name
# 		return 'Ничья'


# game = Game()
# game.play_game()




# !!!!!!!!!!!!!!!FIZZBUZZ

# for i in range(1, 101):
# 	if i % 3 == 0 and i % 5 == 0:
# 		print('FizzBuzz')
# 	elif i % 3 == 0:
# 		print('Fizz')
# 	elif i % 5 == 0:
# 		print('Buzz')
# 	else:
# 		print(i)


# def is_palindrome(word):
# 	word = word.lower()
# 	return word[::-1] == word


# word = 'шалаш'
# print( is_palindrome(word) )


# print(l1)
# print(l2)


#####################################################################

# import requests
# from bs4 import BeautifulSoup as bs
# import re


# def get_response(url, prms, headers):
# 	session = requests.Session()
# 	response = session.get(url, params = prms, headers = headers)
# 	if response.status_code == 200:
# 		return response
# 	else:
# 		return 'Error'


# def get_vacancyes(response):
# 	vacancyes = []
# 	soup = bs(response.content, 'html.parser')
# 	divs = soup.find_all('div', attrs = {'data-qa': 'vacancy-serp__vacancy'})
# 	for div in divs:
# 		title = div.find('a', attrs = {'data-qa': 'vacancy-serp__vacancy-title'}).text
# 		link = div.find('a', attrs = {'data-qa': 'vacancy-serp__vacancy-title'})['href']
# 		compensation_test = div.find('div', attrs = {'class': 'vacancy-serp-item__compensation'})

# 		if compensation_test is not None:
# 			compensation = compensation_test.text
# 		else:
# 			compensation = '-'

# 		vacancyes.append({
# 			'title': title,
# 			'link': link,
# 			'compensation': compensation
# 		})
# 	return vacancyes

# def pretty(vacancyes_dict):
# 	for vacancy in vacancyes_dict:
# 		print('-------------------------------------------------------------------------')
# 		print(f'*{ vacancy["title"] }* | зарплата: { vacancy["compensation"] }')
# 		print(vacancy['link'])
# 		print()




# # response = requests.get('https://hh.ru/search/vacancy', params = keys, headers = headers)
# search_text = input('Enter search query: ')
# url = 'https://hh.ru/search/vacancy'
# keys = {'text': f'{search_text}', 'area': '1', 'from': 'suggest_post', 'page': '0'}
# headers = {
# 	'accept': '*/*',
# 	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}



# if __name__ == '__main__':
# 	all_vacancyes = get_vacancyes( get_response(url, keys, headers) )
# 	pretty(all_vacancyes)

#######################################################################################



# from requests import get, post
# from json import dumps, loads
# # https://api.myjson.com/bins/9o784

# class myjsonRequest():
# 	def __init__(self, id = ''):
# 		self.id = id
# 		self.url = 'https://api.myjson.com/bins'
# 		self.response = None

# 	def get(self, type='dict'):
# 		self.response = get(self.url + '/' + self.id)
# 		if self.response.status_code == 200:
# 			if type == 'json':
# 				return dumps(loads(self.response.text), indent = 4)
# 			return loads(self.response.text)
# 		else:
# 			return 'Bad request'

# 	def create(self, json_data):
# 		self.id = loads( post('https://api.myjson.com/bins', json = json_data).text )['uri'].replace('https://api.myjson.com/bins/', '')
# 		return self.id




# data = {
# 	'id': 1,
# 	'key': 'value',
# 	'title': 'Myjson lib',
# 	'status': True
# }



# # json = myjsonRequest()

# # add = json.create(data)
# # print(add + '==' + json.id) # bin ID == bin ID

# # get_text = json.get('json')
# # print(get_text)

# # 
# json = myjsonRequest('9o784') # with bin ID

# get_text = json.get('json') # returns a Str pretty json
# print(get_text)

# get_text = json.get() # returns a Dict json
# print(get_text)


####################################################################################
from os import mkdir, chdir, getcwd
from os.path import exists
import pickle
class Filer:
    def __init__(self, dictname="unnamed_dict"):
        self.my_name = dictname
        self.true_path = f'{getcwd()}/{self.my_name}/'
        if not exists(dictname):
            mkdir(dictname)

    def __getitem__(self, item):
    	with open(self.true_path + item, 'r') as file:
    		value = file.read()
    			file.close()
    			return 'Error'
    		return value

    def __setitem__(self, item, value):
    	with open(self.true_path + item, 'w') as file:
        	file.write(value)
        	file.close()
# TEST
filer_dict = Filer("cats")
print(filer_dict["Megan"])
filer_dict["Megan"] = 'test'











