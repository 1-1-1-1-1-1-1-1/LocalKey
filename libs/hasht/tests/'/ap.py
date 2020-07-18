import os

for i in dir(os):
	if 'remove' in i:
		print(i, eval(f'os.{i}.__doc__ '), sep = ': ')

pass