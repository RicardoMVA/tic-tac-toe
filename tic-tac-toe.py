import time
import string
import graphics

print('\n\n  Welcome to Tic-Tac-Toe!')
time.sleep(1.5)
print('\n  To play, you need to input coordinates')
print('  For example: A1 or B2, got it?')
print(graphics.board_start())
time.sleep(3)

game_running = True

class Player(object):

	def __init__(self, name, symbol):
		self.symbol = symbol
		self.name = name

	def set_symbol(self):
		symbol = input("\n  Choose 'X' or 'O' as your symbol: ").lower()
		while symbol != 'x' and symbol != 'o':
			print("  Pick a valid symbol")
			symbol = input("\n  Choose 'X' or 'O' as your symbol: ").lower()
		else:
			if symbol == 'x':
				print("  You pick 'X', so player 2 will use 'O'")
				self.symbol = 'X'
				player_2.symbol = 'O'
			else:
				print("  You pick 'O', so player 2 will use 'X'")
				self.symbol = 'O'
				player_2.symbol = 'X'
			return self.symbol


def player_name(self):
	#
	# set player name
	#
	while True:
		self.name = input('  ')
		time.sleep(1)		
		if self.name == '' or self.name == ' ':
			print('  Pick a valid name!')
			time.sleep(1)
			continue
		elif player_2.name == player_1.name:
			print('  Pick a different name from player 1!')
			time.sleep(1)
			print('\n  Name of the second player: ')
			continue
		else:
			print('\n  Hi, ', self.name)
			time.sleep(1)
			break


def check_winner(lst):
#
# checks for winning combination in passed lst:
#
	if 'a1' in lst and 'a2' in lst and 'a3' in lst:
		return True
	elif 'b1' in lst and 'b2' in lst and 'b3' in lst:
		return True
	elif 'c1' in lst and 'c2' in lst and 'c3' in lst:
		return True
	elif 'a1' in lst and 'b1' in lst and 'c1' in lst:
		return True
	elif 'a2' in lst and 'b2' in lst and 'c2' in lst:
		return True
	elif 'a3' in lst and 'b3' in lst and 'c3' in lst:
		return True
	elif 'a1' in lst and 'b2' in lst and 'c3' in lst:
		return True
	elif 'c1' in lst and 'b2' in lst and 'a3' in lst:
		return True
	else:
		return False


def run_game():
	#
  	# starts game from scratch:
 	#
	global count, current_player, current_symbol, current_list, play_list
	global player_1, player_2, lst_1, lst_2

	count = 0
	play_list = ['a1', 'a2', 'a3', 'b1', 'b2','b3', 'c1', 'c2', 'c3']
	current_list = []
	player_1 = Player('abc',0)
	lst_1 = []
	player_2 = Player('def',0)
	lst_2 = []

	graphics.board_start()
	print("  Then, let's play!")
	
	print('\n  Name of the first player: ')
	player_name(player_1)
	player_1.set_symbol()

	print('\n  Name of the second player: ')
	player_name(player_2)

	while check_winner(current_list) == False:
		player_turn()
		get_move()
		continue

	else:
		print('  %s won the game!' %(current_player))
		repeat()


while game_running == True:
	run_game()
	continue
