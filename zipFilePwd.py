import random, pyminizip, os, sys

com_lvl = 9


def clear_screen():
	os.system('clear')

def check_argv():
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	password_len = int(sys.argv[3])
	return input_file, output_file, password_len

def random_password_generator(password_len):
	clear_screen()
	with open('list.txt') as file:
		lines = [line for line in file]

	while True:
		random_line = random.randint(0, len(lines)-1)
		password    = lines[random_line].replace("\n","")
		if len(lines[random_line]) >= password_len:
			break
	return password, random_line

input_file, output_file, password_len = check_argv()
if check_argv():
	try:
		password, random_line = random_password_generator(password_len)
		print(f'Original File:		{input_file:_^25}')
		print(f'Zipped File:		{output_file:_^25}')
		print(f'Random Line:		{random_line+1:_^25}')
		print(f'Password:		{password:_^25}')
		print(f'Password Len:		{len(password):_^25}')

		try:
			pyminizip.compress(input_file, None, output_file, password, com_lvl)
		except Exception as e:
			print(e)
	except Exception as e:
		print(e)
else:
	print('Missing arguments')