from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import os, random, glob

root = Tk()
root.title('FlashCards 1.0')
original_path = os.getcwd()
scale = 0.60

os.chdir(f'{os.getcwd()}\\Lib')

# -----------------------------------------------------------------------------------------------------------------------------------------------------
# States (USA)

def randomize_states():
	global our_states, rand, state_img, ans_label, ans_input, ans_button
	ans_button['state'] = 'enabled'

	our_states = [x.split('.')[0] for x in glob.glob('*.gif')]
	rand = random.randint(0, len(our_states)-1)
	state = f'{our_states[rand]}.gif'

	img = Image.open(state)
	iw, ih = img.width, img.height
	scale = 0.60

	state_img = ImageTk.PhotoImage(img.resize((int(iw*scale), int(ih*scale)), Image.ANTIALIAS))
	show_state.config(image=state_img)

	ans_label['text'] = ''
	ans_input.delete(0, END)
def state_ans():
	answer = ans_input.get().lower()

	if answer == our_states[rand]:
		response = f'Correct!'
		root.after(500, randomize_states)
		newnum = int(all_correct['text'].split(': ')[1]) + 1

		ans_button['state'] = DISABLED

		all_correct['text'] = f'Correct: {newnum}'
	else:
		response = f'Incorrect '

	if answer == 'washington state' and 'washington' == our_states[rand]:
		response = 'correct'

	ans_label['text'] = response
def states():
	global all_correct, state_img, ans_input, ans_label, rand, our_states, show_state, ans_button
	hide_all_frames()
	state_frame.pack(fill='both', expand=1)

	'''
	our_states = [x.split('.')[0] for x in glob.glob('*.gif')]
	rand = random.randint(0, len(our_states)-1)
	state = f'{our_states[rand]}.gif'

	img = Image.open(state)
	iw, ih = img.width, img.height
	scale = 0.60

	state_img = ImageTk.PhotoImage(img.resize((int(iw*scale), int(ih*scale)), Image.ANTIALIAS))
	'''
	show_state = Label(state_frame, background='#FFFFFF')
	show_state.pack(pady=(0, 15))

	controls_frame = Frame(state_frame, background='#FFFFFF')
	controls_frame.pack(pady=10)

	ans_input = ttk.Entry(state_frame, width=50)
	ans_input.pack(pady=15)
	random_button = ttk.Button(controls_frame, text='Next ...', command=randomize_states)
	random_button.grid(row=0, column=1, padx=10, ipadx=5)
	ans_button = ttk.Button(controls_frame, text='Check Answer', command=province_ans)
	ans_button.grid(row=0, column=0, padx=10)

	ans_label = Label(state_frame, text='', font=('Helvetica', 18), background='#FFFFFF')
	ans_label.pack(pady=15)

	all_correct = Label(state_frame, text='Correct: 0', relief='flat', anchor=E, bd=1)
	all_correct.pack(side=BOTTOM, fill=X, ipady=2)

	randomize_states()

# -----------------------------------------------------------------------------------------------------------------------------------------------------
# State Capitals (USA)

def random_capitals():
	global our_states, our_state_capitals, ans_list, answer, capital_radiobutton1, capital_radiobutton2, capital_radiobutton3, pass_button, capital_ans_button
	our_states = [x.split('.')[0] for x in glob.glob('*.gif')]
	our_state_capitals = {
			'alabama':'Montgomery',
			'arizona':'Phoenix',
			'california':'Sacramento',
			'florida':'Tallahassee',
			'hawaii':'Honolulu',
			'michigan':'Lansing',
			'new mexico':'Santa Fe',
			'new york':'Albany',
			'ohio':'Columbus',
			'texas':'Austin',
			'vermont':'Montpelier',
			'washington':'Olympia',
			'wisconsin':'Madison'
	}

	ans_list = []
	count = 1
	while count < 4:
		rand = random.randint(0, len(our_states)-1)
			
		if count == 1:
			answer = our_states[rand]
			global state_img
			state = f'{our_states[rand]}.gif'

			img = Image.open(state)
			iw, ih = img.width, img.height

			state_img = ImageTk.PhotoImage(img.resize((int(iw*scale), int(ih*scale)), Image.ANTIALIAS))
			show_state.config(image=state_img)

		ans_list.append(our_states[rand])
		our_states.remove(our_states[rand])

		random.shuffle(our_states)
		count += 1

	random.shuffle(ans_list)

	global capital_radio
	capital_radio.set(our_state_capitals[ans_list[0]])

	capital_radiobutton1['value'] = our_state_capitals[ans_list[0]]
	capital_radiobutton2['value'] = our_state_capitals[ans_list[1]]
	capital_radiobutton3['value'] = our_state_capitals[ans_list[2]]

	capital_radiobutton1['text'] = our_state_capitals[ans_list[0]]
	capital_radiobutton2['text'] = our_state_capitals[ans_list[1]]
	capital_radiobutton3['text'] = our_state_capitals[ans_list[2]]

	capital_ans_button['state'] = 'enabled'
	ans_label['text'] = ' '
	print('hi')
def state_capital_ans():
	if capital_radio.get() == our_state_capitals[answer]:
		response = f'Correct!'
		root.after(500, random_capitals)
		newnum = int(all_correct['text'].split(': ')[1]) + 1

		capital_ans_button['state'] = DISABLED

		all_correct['text'] = f'Correct: {newnum}'
	else:
		response = f'Incorrect '

	ans_label['text'] = response
def state_capitals():
	global show_state, our_states, our_state_capitals, ans_label, answer, all_correct, capital_ans_button, capital_radiobutton1, capital_radiobutton2, capital_radiobutton3, pass_button, capital_radio, capital_ans_button
	hide_all_frames()
	state_capital_frame.pack(fill='both', expand=1)
	controls_frame = Frame(state_capital_frame)
	pass_button = ttk.Button(controls_frame, text='Next ...', command=random_capitals)
	capital_ans_button = ttk.Button(controls_frame, text='Check Answer', command=state_capital_ans)
	

	show_state = Label(state_capital_frame, background='#FFFFFF')
	show_state.pack(pady=(0, 15))

	capital_radio = StringVar()

	capital_radiobutton1 = ttk.Radiobutton(state_capital_frame, variable=capital_radio, style='WhiteBG.TRadiobutton')
	capital_radiobutton2 = ttk.Radiobutton(state_capital_frame, variable=capital_radio, style='WhiteBG.TRadiobutton')
	capital_radiobutton3 = ttk.Radiobutton(state_capital_frame, variable=capital_radio, style='WhiteBG.TRadiobutton')

	capital_radiobutton1.pack()
	capital_radiobutton2.pack()
	capital_radiobutton3.pack()
	ans_label = Label(state_capital_frame, text='', font=('Helvetica', 18), background='#FFFFFF')

	random_capitals()

	controls_frame.pack(pady=10)

	pass_button.grid(row=0, column=1, padx=10, ipadx=5)
	capital_ans_button.grid(row=0, column=0, padx=10)

	ans_label.pack(pady=15)

	all_correct = Label(state_capital_frame, text='Correct: 0', relief='flat', anchor=E, bd=1)
	all_correct.pack(side=BOTTOM, fill=X, ipady=2)

# -----------------------------------------------------------------------------------------------------------------------------------------------------
# World Flags

def random_flags():
	global our_states, ans_list, answer, capital_radiobutton1, capital_radiobutton2, capital_radiobutton3, pass_button, capital_ans_button
	CURDIR = os.getcwd()
	os.chdir(f'{CURDIR}\\flags')
	our_flags = [x.split('.')[0] for x in glob.glob('*.png')]
	os.chdir(f'{CURDIR}')

	ans_list = []
	count = 1
	while count < 4:
		rand = random.randint(0, len(our_flags)-1)
			
		if count == 1:
			answer = our_flags[rand]
			global flag_img
			flg = f'flags\\{our_flags[rand]}.png'

			img = Image.open(flg)
			iw, ih = img.width, img.height

			flag_img = ImageTk.PhotoImage(img.resize((int(iw*scale), int(ih*scale)), Image.ANTIALIAS))
			show_state.config(image=flag_img)

		ans_list.append(our_flags[rand])
		our_flags.remove(our_flags[rand])

		random.shuffle(our_flags)
		count += 1

	random.shuffle(ans_list)

	global capital_radio
	capital_radio.set(ans_list[0])

	capital_radiobutton1['value'] = ans_list[0]
	capital_radiobutton2['value'] = ans_list[1]
	capital_radiobutton3['value'] = ans_list[2]

	capital_radiobutton1['text'] = ans_list[0]
	capital_radiobutton2['text'] = ans_list[1]
	capital_radiobutton3['text'] = ans_list[2]

	capital_ans_button['state'] = 'enabled'
	ans_label['text'] = ' '
	print('hi')
def flag_ans():
	if capital_radio.get() == answer:
		response = f'Correct!'
		root.after(500, random_flags)
		newnum = int(all_correct['text'].split(': ')[1]) + 1

		capital_ans_button['state'] = DISABLED

		all_correct['text'] = f'Correct: {newnum}'
	else:
		response = f'Incorrect '

	ans_label['text'] = response
def flags():
	global show_state, our_flags, ans_label, answer, all_correct, capital_ans_button, capital_radiobutton1, capital_radiobutton2, capital_radiobutton3, pass_button, capital_radio, capital_ans_button
	hide_all_frames()
	state_capital_frame.pack(fill='both', expand=1)
	controls_frame = Frame(state_capital_frame, background='#FFFFFF')
	pass_button = ttk.Button(controls_frame, text='Next ...', command=random_flags)
	capital_ans_button = ttk.Button(controls_frame, text='Check Answer', command=flag_ans)
	

	show_state = Label(state_capital_frame, background='#FFFFFF')
	show_state.pack(pady=(0, 15))

	capital_radio = StringVar()

	capital_radiobutton1 = ttk.Radiobutton(state_capital_frame, variable=capital_radio, style='WhiteBG.TRadiobutton')
	capital_radiobutton2 = ttk.Radiobutton(state_capital_frame, variable=capital_radio, style='WhiteBG.TRadiobutton')
	capital_radiobutton3 = ttk.Radiobutton(state_capital_frame, variable=capital_radio, style='WhiteBG.TRadiobutton')

	capital_radiobutton1.pack()
	capital_radiobutton2.pack()
	capital_radiobutton3.pack()
	ans_label = Label(state_capital_frame, text='', font=('Helvetica', 18), background='#FFFFFF')

	random_flags()

	controls_frame.pack(pady=10)

	pass_button.grid(row=0, column=1, padx=10, ipadx=5)
	capital_ans_button.grid(row=0, column=0, padx=10)

	ans_label.pack(pady=15)

	all_correct = Label(state_capital_frame, text='Correct: 0', relief='flat', anchor=E, bd=1)
	all_correct.pack(side=BOTTOM, fill=X, ipady=2)

# -----------------------------------------------------------------------------------------------------------------------------------------------------
# Provinces (CAN)

def randomize_prov():
	global our_states, rand, state_img, ans_label, ans_input, ans_button
	ans_button['state'] = 'enabled'

	our_states = [x.split('.')[0] for x in glob.glob('*.gif')]
	rand = random.randint(0, len(our_states)-1)
	state = f'{our_states[rand]}.gif'

	img = Image.open(state)
	iw, ih = img.width, img.height
	scale = 0.60

	state_img = ImageTk.PhotoImage(img.resize((int(iw*scale), int(ih*scale)), Image.ANTIALIAS))
	show_state.config(image=state_img)

	ans_label['text'] = ''
	ans_input.delete(0, END)
def province_ans():
	answer = ans_input.get().lower()

	if answer == our_states[rand]:
		response = f'Correct!'
		root.after(500, randomize_prov)
		newnum = int(all_correct['text'].split(': ')[1]) + 1

		ans_button['state'] = DISABLED

		all_correct['text'] = f'Correct: {newnum}'
	else:
		response = f'Incorrect '

	if answer == 'washington state' and 'washington' == our_states[rand]:
		response = 'correct'

	ans_label['text'] = response
def canada_states():
	'''
	global all_correct, state_img, ans_input, ans_label, rand, our_states, show_state, ans_button
	'''
	hide_all_frames()
	state_frame.pack(fill='both', expand=1)
	ttk.Label(state_frame, text='coming soon ...').pack()
	'''

	show_state = Label(state_frame, background='#FFFFFF')
	show_state.pack(pady=(0, 15))

	controls_frame = Frame(state_frame, background='#FFFFFF')
	controls_frame.pack(pady=10)

	ans_input = ttk.Entry(state_frame, width=50)
	ans_input.pack(pady=15)
	random_button = ttk.Button(controls_frame, text='Next ...', command=randomize_prov)
	random_button.grid(row=0, column=1, padx=10, ipadx=5)
	ans_button = ttk.Button(controls_frame, text='Check Answer', command=province_ans)
	ans_button.grid(row=0, column=0, padx=10)

	ans_label = Label(state_frame, text='', font=('Helvetica', 18), background='#FFFFFF')
	ans_label.pack(pady=15)

	all_correct = Label(state_frame, text='Correct: 0', relief='flat', anchor=E, bd=1)
	all_correct.pack(side=BOTTOM, fill=X, ipady=2)

	randomize_prov()
	'''

# -----------------------------------------------------------------------------------------------------------------------------------------------------
# Addition

def randomaddition(level):
	global rand1, rand2, add_1, add_2, add_img1, add_img2

	if level == 1:
		rand1 = random.randint(0, 10)
		rand2 = random.randint(0, 10)
	elif level == 2:
		rand1 = random.randint(10, 20)
		rand2 = random.randint(5, 20)
		if rand1 or rand2 == 13:
			if random.randint(0, 1) == 1:
				rand1 += 1
				rand2 += 1
			else:
				rand1 -= 1
				rand2 -= 1
	elif level == 3:
		possible_numbers = [99, 50, 67, 88, 21, 74, 100, 154, 175, 111, 231]

		random.shuffle(possible_numbers)
		rand1 = possible_numbers[0]
		random.shuffle(possible_numbers)
		rand2 = possible_numbers[0]

	add_img1, add_img2 = ImageTk.PhotoImage(Image.open(f'numeral\\{rand1}.png')), ImageTk.PhotoImage(Image.open(f'numeral\\{rand2}.png'))

	add_1['image'] = add_img1
	add_2['image'] = add_img2

	answer_msg['text'] = ''
	answer_box_add.delete(0, END)
def add_ans(level):
	global answer_msg, answer_box_add

	answer = rand1 + rand2

	if answer_box_add.get() == str(answer):
		response = 'Correct!'
		root.after(500, lambda: randomaddition(level))
		newnum = int(all_correct['text'].split(': ')[1]) + 1
		all_correct['text'] = f'Correct: {newnum}'
	else:
		response = 'Incorrect'

	answer_msg['text'] = response
def addition(level=1):
	global add_1, add_2, answer_box_add, answer_msg, all_correct

	hide_all_frames()
	add_frame.pack(fill='both', expand=1)

	Label(add_frame, text='Addition', font=('Helvetica', 18)).pack(pady=15)

	pic_frame = ttk.Frame(add_frame, width=400, height=300)
	pic_frame.pack()

	add_1 = Label(pic_frame)
	add_2 = Label(pic_frame)
	sign = Label(pic_frame, text='+', font=('Helvetica', 24))

	add_1.grid(row=0, column=0)
	sign.grid(row=0, column=1)
	add_2.grid(row=0, column=2)

	answer_box_add = ttk.Entry(add_frame, width=40)
	answer_box_add.pack(pady=(15, 5))

	add_answer_button = ttk.Button(add_frame, text='Check Answer', command=lambda: add_ans(level))
	add_answer_button.pack(ipadx=5, pady=5)

	answer_msg = Label(add_frame, text='', font=('Helvetica', 18))
	answer_msg.pack(pady=10)

	all_correct = Label(add_frame, text='Correct: 0', relief='flat', anchor=E, bd=1)
	all_correct.pack(side=BOTTOM, fill=X, ipady=2)
	randomaddition(level)

# -----------------------------------------------------------------------------------------------------------------------------------------------------
# Multiplication

def randommultiply(level):
	global rand1, rand2, add_1, add_2, add_img1, add_img2

	if level == 1:
		rand1 = random.randint(0, 10)
		rand2 = random.randint(0, 10)
	elif level == 2:
		rand1 = random.randint(10, 20)
		rand2 = random.randint(5, 20)
		if rand1 or rand2 == 13:
			if random.randint(0, 1) == 1:
				rand1 += 1
				rand2 += 1
			else:
				rand1 -= 1
				rand2 -= 1
	elif level == 3:
		possible_numbers = [99, 50, 67, 88, 21, 74, 100, 154, 175, 111, 231]

		random.shuffle(possible_numbers)
		rand1 = possible_numbers[0]
		random.shuffle(possible_numbers)
		rand2 = possible_numbers[0]

	add_img1, add_img2 = ImageTk.PhotoImage(Image.open(f'numeral\\{rand1}.png')), ImageTk.PhotoImage(Image.open(f'numeral\\{rand2}.png'))

	add_1['image'] = add_img1
	add_2['image'] = add_img2

	answer_msg['text'] = ''
	answer_box_add.delete(0, END)
def mul_ans(level):
	global answer_msg, answer_box_add

	answer = rand1 + rand2

	if answer_box_add.get() == str(answer):
		response = 'Correct!'
		root.after(500, lambda: randomaddition(level))
	else:
		response = 'Incorrect'

	answer_msg['text'] = response
def multiplication(level=1):
	global add_1, add_2, answer_box_add, answer_msg

	hide_all_frames()
	add_frame.pack(fill='both', expand=1)

	Label(add_frame, text='Multiplication', font=('Helvetica', 18)).pack(pady=15)

	pic_frame = ttk.Frame(add_frame, width=400, height=300)
	pic_frame.pack()

	add_1 = Label(pic_frame)
	add_2 = Label(pic_frame)
	sign = Label(pic_frame, text='+', font=('Helvetica', 24))

	add_1.grid(row=0, column=0)
	sign.grid(row=0, column=1)
	add_2.grid(row=0, column=2)

	answer_box_add = ttk.Entry(add_frame, width=40)
	answer_box_add.pack(pady=(15, 5))

	add_answer_button = ttk.Button(add_frame, text='Check Answer', command=lambda: add_ans(level))
	add_answer_button.pack(ipadx=5, pady=5)

	answer_msg = Label(add_frame, text='', font=('Helvetica', 18))
	answer_msg.pack(pady=10)
	randomaddition(level)

# -----------------------------------------------------------------------------------------------------------------------------------------------------
# Facts about 3D Shapes

def shape_shifter_show(shape):
	top = Toplevel(root)
	if shape == 'cube':
		ttk.Label(top, text='Cube').pack(pady=5)

def three_dee():
	global l1, shapes
	hide_all_frames()
	threed_frame.pack(expand=1, fill='both')

	shapes = [
		ImageTk.PhotoImage(Image.open('3D Shapes\\cube.png').resize((200, 200), Image.ANTIALIAS)),
		ImageTk.PhotoImage(Image.open('3D Shapes\\sphere.png').resize((200, 200), Image.ANTIALIAS)),
		ImageTk.PhotoImage(Image.open('3D Shapes\\cone.png').resize((200, 200), Image.ANTIALIAS)),
		ImageTk.PhotoImage(Image.open('3D Shapes\\rectprism.png').resize((200, 200), Image.ANTIALIAS)),
		ImageTk.PhotoImage(Image.open('3D Shapes\\pyramid.png').resize((200, 200), Image.ANTIALIAS))
	]

	ttk.Label(threed_frame, text='3D Shape Dictionary').pack(pady=5)

	img_frame = ttk.Frame(threed_frame)
	img_frame.pack(pady=5)

	sk = ttk.Frame(img_frame)
	sk.grid(row=0, column=0)

	ttk.Button(sk, text='Cube', image=shapes[0], compound='top', command=lambda: shape_shifter_show('cube')).grid(row=0, column=0, padx=5)
	ttk.Button(sk, text='Sphere', image=shapes[1], compound='top').grid(row=0, column=1, padx=10)
	ttk.Button(sk, text='Cone', image=shapes[2], compound='top').grid(row=0, column=2, padx=10)

	ssk = ttk.Frame(img_frame)
	ssk.grid(row=1, column=0, pady=5)

	ttk.Button(ssk, text='Rectangular Prism', image=shapes[3], compound='top').grid(row=0, column=0, padx=10)
	ttk.Button(ssk, text='Pyramid (Square)', image=shapes[4], compound='top').grid(row=0, column=1, padx=10)


def hide_all_frames():
	for w in state_frame.winfo_children():
		w.destroy()
	for w in state_capital_frame.winfo_children():
		w.destroy()
	for w in add_frame.winfo_children():
		w.destroy()

	state_frame.pack_forget()
	state_capital_frame.pack_forget()
	add_frame.pack_forget()





menu = Menu(root)
root['menu'] = menu
root['bg'] = '#FFFFFF'

style = ttk.Style()
style.configure('WhiteBG.TRadiobutton', background='#FFFFFF')

qz_menu = Menu(menu, tearoff=0)
menu.add_cascade(label='Quiz', menu=qz_menu)

sg_menu = Menu(menu, tearoff=0)
menu.add_cascade(label='Facts', menu=sg_menu)

# Facts!
sg_menu.add_command(label='3D Shapes', command=three_dee)

# Geography Flashcards
geo_menu = Menu(qz_menu, tearoff=0)
qz_menu.add_cascade(label='Geography', menu=geo_menu)
geo_menu.add_command(label='States (USA)', command=states)
geo_menu.add_command(label='State Capitals (USA)', command=state_capitals)
geo_menu.add_command(label='World Flags', command=flags)
geo_menu.add_command(label='[Coming Soon] Provinces (CAN)', command=canada_states, state=DISABLED)

# Math Flashcards
math_menu = Menu(qz_menu, tearoff=0)
qz_menu.add_cascade(label='Math', menu=math_menu)

add_menu = Menu(math_menu, tearoff=0)
math_menu.add_cascade(label='Addition', menu=add_menu)
add_menu.add_command(label='Level 1', command=lambda: addition(level=1))
add_menu.add_command(label='Level 2', command=lambda: addition(level=2))
add_menu.add_command(label='Level 3', command=lambda: addition(level=3))

qz_menu.add_separator()
qz_menu.add_command(label='Quit', command=root.quit, foreground='purple')

state_frame = Frame(root, width=500, height=500, bd=0, background='#FFFFFF')
state_capital_frame = Frame(root, width=500, height=500, background='#FFFFFF')
add_frame = Frame(root, width=500, height=500)
threed_frame = Frame(root, width=500, height=500)







root.mainloop()