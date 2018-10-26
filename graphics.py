def board_start():
    global line_0, line_1, line_2, line_3
    global line_4, line_5, line_6
    global board
    line_0 = ('                            \n')
    line_1 = ('        A       B       C   \n')
    line_2 = ('            |       |       \n')
    line_3 = ('   1        |       |       \n')
    line_4 = ('     _______|_______|_______\n')
    line_5 = ('   2        |       |       \n')
    line_6 = ('   3        |       |       \n')
    board = (line_0 + line_1 + line_2 + line_3
    	         + line_4 + line_2 + line_5 + line_4
    	         + line_2 + line_6 + line_2 + line_0)
    return board


def print_symbol(play, symbol):
	global line_3, line_5, line_6, board

	if play == 'a1':
		line_3 = line_3[:8] + symbol + line_3[9:]
	elif play == 'a2':
		line_5 = line_5[:8] + symbol + line_5[9:]
	elif play == 'a3':
		line_6 = line_6[:8] + symbol + line_6[9:]
	elif play == 'b1':
		line_3 = line_3[:16] + symbol + line_3[17:]
	elif play == 'b2':
		line_5 = line_5[:16] + symbol + line_5[17:]
	elif play == 'b3':
		line_6 = line_6[:16] + symbol + line_6[17:]
	elif play == 'c1':
		line_3 = line_3[:24] + symbol + line_3[25:]
	elif play == 'c2':
		line_5 = line_5[:24] + symbol + line_5[25:]
	elif play == 'c3':
		line_6 = line_6[:24] + symbol + line_6[25:]

	board = (line_0 + line_1 + line_2 + line_3
    	         + line_4 + line_2 + line_5 + line_4
    	         + line_2 + line_6 + line_2 + line_0)
	return board
