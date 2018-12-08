import random as rd

def hungman(word):
	wrong = 0
	stages = ["",
		"________         ",
		"|       |        ",
		"|       |        ",
		"|       |        ",
		"|       o        ",
		"|      /|\\       ",
		"|      / \\       ",
		"|                "
	]
	rletters = list(word)
	board = ['_'] * len(word)
	win = False
	print('Welcome to execution!')
	print(' '.join(board))

	while wrong < len(stages) - 1:
		print('\n')
		char = input('Enter char: ')
		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters[cind] = '$'
		else:
			wrong += 1
		print((" ".join(board)))
		e = wrong + 1
		print('\n'.join(stages[0: e]))
		if "_" not in board:
			print('You are winner! The word: {}'.format(word))
			win = True
			break
	if not win:
		print('You are loser! The word: {}'.format(word))

words = ['кулинария', 'парадигма', 'президент', 'машина', 'паровоз', 'самолет', 'праздник']
rd_word = words[rd.randint(0, len(words))]
hungman(rd_word)
