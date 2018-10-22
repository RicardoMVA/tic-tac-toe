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
  	# Nome dos jogadores:
 	#
	global jogador_1, jogador_2
	
	while True:
		jogador_1 = input('\n  Name of the first player: ')
		time.sleep(1)		
		if jogador_1 == '' or jogador_1 == ' ':
			print('  Pick a valid name!')
			time.sleep(1)
			continue
		else:
			print('\n  Hi, ', jogador_1)
			time.sleep(1)
			break

	while True:
		jogador_2 = input('\n  Name of the second player: ')
		time.sleep(1)
		if jogador_2 == jogador_1:
			print('  Pick a different name from player 1!')
			time.sleep(1)
			continue
		elif jogador_2 == '' or jogador_2 == ' ':
			print('  Pick a valid name!')
			time.sleep(1)
			continue
		else:
			print('\n  Hi, ', jogador_2)
			time.sleep(1)
			break

	#
	# Checando o vencedor:
	#
	def checar_vencedor(lista):
		if 'a1' in lista and 'a2' in lista and 'a3' in lista:
			return True
		elif 'b1' in lista and 'b2' in lista and 'b3' in lista:
			return True
		elif 'c1' in lista and 'c2' in lista and 'c3' in lista:
			return True
		elif 'a1' in lista and 'b1' in lista and 'c1' in lista:
			return True
		elif 'a2' in lista and 'b2' in lista and 'c2' in lista:
			return True
		elif 'a3' in lista and 'b3' in lista and 'c3' in lista:
			return True
		elif 'a1' in lista and 'b2' in lista and 'c3' in lista:
			return True
		elif 'c1' in lista and 'b2' in lista and 'a3' in lista:
			return True
		else:
			return False

	#
	# Lógica do game_on:
	#
	lista_de_jogadas = ['a1', 'a2', 'a3', 'b1', 'b2','b3', 'c1', 'c2', 'c3']
	jogada_1 = 0
	lista_1 = []
	vitoria_1 = False
	jogada_2 = 0
	lista_2 = []
	vitoria_2 = False
	repetir = 0

	while True:
		if vitoria_1 == True:
			print('  %s won the game!' %(jogador_1))
			repetir = input('  Want to play again?\n  ')
			if repetir == 'yes' or repetir == 'Yes' or repetir == 'y':
				graphics.board_start()
				game_on()
				break
			else:
				print('  No? Ok, thanks for playing!')
				break 

		elif vitoria_2 == True:
			print('  %s won the game!' %(jogador_2))
			repetir = input('  Want to play again?\n  ')
			if repetir == 'yes' or repetir == 'Yes' or repetir == 'y':
				graphics.board_start()
				game_on()
				break
			else:
				print('  No? Ok, thanks for playing!')
				break
		
		else:
			while vitoria_1 == False and vitoria_2 == False:
				jogada_1 = input('\n  %s, pick a coordinate: ' %(jogador_1)).lower()			  				
				if jogada_1 not in lista_de_jogadas:
					print('  Invalid play')
					continue
				else:
					lista_de_jogadas.remove(jogada_1)				
					lista_1.append(jogada_1)
					graphics.circle(jogada_1)									
					print(graphics.board)
					vitoria_1 = checar_vencedor(lista_1)
					time.sleep(1)
					if vitoria_1 == True:
						break
					elif len(lista_1) == 5:
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
							jogada_2 = input('\n  %s, pick a coordinate: ' %(jogador_2)).lower()  			  							
							if jogada_2 not in lista_de_jogadas:
								print('  Invalid play')
								continue
							else:
								lista_de_jogadas.remove(jogada_2)
								lista_2.append(jogada_2)
								graphics.ex(jogada_2)	
								print(graphics.board)
								vitoria_2 = checar_vencedor(lista_2)
								time.sleep(1)
								if vitoria_2 == True:
									break
								else:
									break
					continue			
			continue

game_on()
