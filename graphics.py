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


def circle(str):
	global line_3, line_5, line_6
	global board

	if str == 'a1':
		line_3 = line_3[:8] + 'O' + line_3[9:]
	elif str == 'a2':
		line_5 = line_5[:8] + 'O' + line_5[9:]
	elif str == 'a3':
		line_6 = line_6[:8] + 'O' + line_6[9:]
	elif str == 'b1':
		line_3 = line_3[:16] + 'O' + line_3[17:]
	elif str == 'b2':
		line_5 = line_5[:16] + 'O' + line_5[17:]
	elif str == 'b3':
		line_6 = line_6[:16] + 'O' + line_6[17:]
	elif str == 'c1':
		line_3 = line_3[:24] + 'O' + line_3[25:]
	elif str == 'c2':
		line_5 = line_5[:24] + 'O' + line_5[25:]
	elif str == 'c3':
		line_6 = line_6[:24] + 'O' + line_6[25:]

	board = (line_0 + line_1 + line_2 + line_3
    	         + line_4 + line_2 + line_5 + line_4
    	         + line_2 + line_6 + line_2 + line_0)
	return board


def ex(str):
	global line_3, line_5, line_6
	global board

	if str == 'a1':
		line_3 = line_3[:8] + 'X' + line_3[9:]
	elif str == 'a2':
		line_5 = line_5[:8] + 'X' + line_5[9:]
	elif str == 'a3':
		line_6 = line_6[:8] + 'X' + line_6[9:]
	elif str == 'b1':
		line_3 = line_3[:16] + 'X' + line_3[17:]
	elif str == 'b2':
		line_5 = line_5[:16] + 'X' + line_5[17:]
	elif str == 'b3':
		line_6 = line_6[:16] + 'X' + line_6[17:]
	elif str == 'c1':
		line_3 = line_3[:24] + 'X' + line_3[25:]
	elif str == 'c2':
		line_5 = line_5[:24] + 'X' + line_5[25:]
	elif str == 'c3':
		line_6 = line_6[:24] + 'X' + line_6[25:]

	board = (line_0 + line_1 + line_2 + line_3
    	         + line_4 + line_2 + line_5 + line_4
    	         + line_2 + line_6 + line_2 + line_0)
	return board