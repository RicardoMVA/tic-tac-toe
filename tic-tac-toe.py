import time
import string
import graphics

print('\n\n  Welcome to Tic-Tac-Toe!')
time.sleep(1.5)
print('\n  To play, you need to input coordinates')
time.sleep(1.5)
print('  For example: A1 or B2, got it?')
time.sleep(1.5)
print("  Then, let's play!")
time.sleep(1.5)
print(graphics.board_start())

def game_on():

	#
  	# Player names:
 	#
	global player_1, player_2
	
	while True:
		player_1 = input('\n  Name of the first player: ')
		time.sleep(1)		
		if player_1 == '' or player_1 == ' ':
			print('  Pick a valid name!')
			time.sleep(1)
			continue
		else:
			print('\n  Hi, ', player_1)
			time.sleep(1)
			break

	while True:
		player_2 = input('\n  Name of the second player: ')
		time.sleep(1)
		if player_2 == player_1:
			print('  Pick a different name from player 1!')
			time.sleep(1)
			continue
		elif player_2 == '' or player_2 == ' ':
			print('  Pick a valid name!')
			time.sleep(1)
			continue
		else:
			print('\n  Hi, ', player_2)
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
	vitoria_2 = False
	repetir = 0

	while True:
		if winner_1 == True:
			print('  %s won the game!' %(player_1))
			repetir = input('  Want to play again?\n  ')
			if repetir == 'yes' or repetir == 'Yes' or repetir == 'y':
				graphics.board_start()
				game_on()
				break
			else:
				print('  No? Ok, thanks for playing!')
				break 

		elif vitoria_2 == True:
			print('  %s won the game!' %(player_2))
			repetir = input('  Want to play again?\n  ')
			if repetir == 'yes' or repetir == 'Yes' or repetir == 'y':
				graphics.board_start()
				game_on()
				break
			else:
				print('  No? Ok, thanks for playing!')
				break
		
		else:
			while winner_1 == False and vitoria_2 == False:
				play_1 = input('\n  %s, pick a coordinate: ' %(player_1)).lower()			  				
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
						repetir = input('  Want to play again?\n  ')
						if repetir == 'yes' or repetir == 'Yes' or repetir == 'y':
							graphics.board_start()
							game_on()
							break
						else:
							print('  No? Ok, thanks for playing!')
							break
					else:
						while True:
							play_2 = input('\n  %s, pick a coordinate: ' %(player_2)).lower()  			  							
							if play_2 not in play_list:
								print('  Invalid play')
								continue
							else:
								play_list.remove(play_2)
								lst_2.append(play_2)
								graphics.ex(play_2)	
								print(graphics.board)
								vitoria_2 = check_winner(lst_2)
								time.sleep(1)
								if vitoria_2 == True:
									break
								else:
									break
					continue			
			continue

game_on()
