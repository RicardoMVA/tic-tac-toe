import time
import string
import graphics

print('\n\n  Welcome to Tic-Tac-Toe!')
time.sleep(1.5)
print('\n  To play, you need to input coordinates')
print('  For example: A1 or B2, got it?')
print("  Then, let's play!")
time.sleep(1.5)
print(graphics.board_start())

class Player(object):

	def __init__(self, name, symbol):
		self.symbol = symbol

	def set_name(self, name):
		self.name = name
		return self.name

	def show_name(self):
		return self.name

	def set_symbol(self):
		symbol = ''
		self.symbol = symbol
		symbol = input("Choose 'X' or 'O' as your symbol: ").lower()
		while symbol != 'x' and symbol != 'o':
			print("Pick a valid symbol")
			symbol = input("Choose 'X' or 'O' as your symbol: ").lower()
		else:
			if symbol == 'x':
				print("You pick 'X', so player 2 will use 'O'")
				self.symbol = 'X'
			else:
				print("You pick 'O', so player 2 will use 'X'")
				self.symbol = 'O'
			return self.symbol

	def get_symbol(self):
		return self.symbol

def game_on():

	#
  	# Player names:
 	#
	global player_1, player_2

	player_1 = Player(0,0)
	player_2 = Player(0,0)
	
	while True:
		player_1.set_name(input('\n  Name of the first player: '))
		time.sleep(1)		
		if player_1.show_name() == '' or player_1.show_name() == ' ':
			print('  Pick a valid name!')
			time.sleep(1)
			continue
		else:
			print('\n  Hi, ', player_1.show_name())
			time.sleep(1)
			player_1.set_symbol()
			if player_1.get_symbol() == 'X':
				player_2.symbol = 'O'
			else:
				player_2.symbol = 'X'
			break

	while True:
		player_2.set_name(input('\n  Name of the second player: '))
		time.sleep(1)
		if player_2.show_name() == player_1.show_name():
			print('  Pick a different name from player 1!')
			time.sleep(1)
			continue
		elif player_2.show_name() == '' or player_2.show_name() == ' ':
			print('  Pick a valid name!')
			time.sleep(1)
			continue
		else:
			print('\n  Hi, ', player_2.show_name())
			time.sleep(1)
			break

	#
	# Winner check:
	#
	def check_winner(lst):
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

	#
	# Game logic:
	#
	play_list = ['a1', 'a2', 'a3', 'b1', 'b2','b3', 'c1', 'c2', 'c3']
	play_1 = 0
	lst_1 = []
	winner_1 = False
	play_2 = 0
	lst_2 = []
	winner_2 = False
	repeat = 0

	while True:
		if winner_1 == True:
			print('  %s won the game!' %(player_1.show_name()))
			repeat = input('  Want to play again?\n  ')
			if repeat == 'yes' or repeat == 'Yes' or repeat == 'y':
				graphics.board_start()
				game_on()
				break
			else:
				print('  No? Ok, thanks for playing!')
				break 

		elif winner_2 == True:
			print('  %s won the game!' %(player_2.show_name()))
			repeat = input('  Want to play again?\n  ')
			if repeat == 'yes' or repeat == 'Yes' or repeat == 'y':
				graphics.board_start()
				game_on()
				break
			else:
				print('  No? Ok, thanks for playing!')
				break
		
		else:
			while winner_1 == False and winner_2 == False:
				play_1 = input('\n  %s, pick a coordinate: ' %(player_1.show_name())).lower()			  				
				if play_1 not in play_list:
					print('  Invalid play')
					continue
				else:
					play_list.remove(play_1)				
					lst_1.append(play_1)
					graphics.circle(play_1)									
					print(graphics.board)
					winner_1 = check_winner(lst_1)
					time.sleep(1)
					if winner_1 == True:
						break
					elif len(lst_1) == 5:
						print('  Draw!')
						repeat = input('  Want to play again?\n  ')
						if repeat == 'yes' or repeat == 'Yes' or repeat == 'y':
							graphics.board_start()
							game_on()
							break
						else:
							print('  No? Ok, thanks for playing!')
							break
					else:
						while True:
							play_2 = input('\n  %s, pick a coordinate: ' %(player_2.show_name())).lower()  			  							
							if play_2 not in play_list:
								print('  Invalid play')
								continue
							else:
								play_list.remove(play_2)
								lst_2.append(play_2)
								graphics.ex(play_2)	
								print(graphics.board)
								winner_2 = check_winner(lst_2)
								time.sleep(1)
								if winner_2 == True:
									break
								else:
									break
					continue			
			continue

game_on()
