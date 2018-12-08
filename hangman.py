from random import shuffle

class Card:
suits = ['пикей', 'червей', 'бубей', 'крестей']
values = [
None, None, '2', '3', '4', '5',
'6', '7', '8', '9', '10', 'валета',
'даму', 'короля', 'туза'
]
def __init__(self, v, s):
self.suit = s
self.value = v

def __lt__(self, c2):
if self.value < c2.value:
return True
if self.value == c2.value:
if self.suit < c2.suit:
return True
else:
return False
return False

def __gt__(self, c2):
if self.value > c2.value:
return True
if self.value == c2.value:
if self.suit > c2.suit:
return True
else:
return False
return False

def __repr__(self):
v = self.values[self.value] + ' ' + self.suits[self.suit]
return v


class Deck:
def __init__(self):
self.cards = []
for i in range(2, 15):
for j in range(4):
self.cards.append(Card(i, j))
shuffle(self.cards)

def rm_card(self):
if len(self.cards) == 0:
return
return self.cards.pop()

class Player:
def __init__(self, name):
self.wins = 0
self.card = None
self.name = name

class Game:
def __init__(self):
name1 = input('имя игрока 1: ')
name2 = input('имя игрока 2: ')
self.deck = Deck()
self.p1 = Player(name1)
self.p2 = Player(name2)

def wins(self, winner):
w = '{} забирает карты'.format(winner)
print(w)

def draw(self, p1_name, p1_card, p2_name, p2_card):
d = '{} кладет {}, а {} кладет {}'.format(p1_name, p1_card, p2_name, p2_card)
print(d)

def play_game(self):
cards = self.deck.cards
print('Lets go!')
while len(cards) >= 2:
response = input('Нажмите любую клавишу для начала игры. Выход - X.')
if response == 'X':
break
p1_card = self.deck.rm_card()
p2_card = self.deck.rm_card()
p1_name = self.p1.name
p2_name = self.p2.name
self.draw(p1_name, p1_card, p2_name, p2_card)
if p1_card > p2_card:
self.p1.wins += 1
self.wins(self.p1.name)
else:
self.p2.wins += 1
self.wins(self.p2.name)
win = self.winner(self.p1, self.p2)
print('Игра окончена. Победил {}'.format(win))

def winner(self, p1, p2):
if p1.wins > p2.wins:
return p1.name
if p1.wins < p2.wins:
return p2.name
return 'Ничья'


game = Game()
game.play_game()

