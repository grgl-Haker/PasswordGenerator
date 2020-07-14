import random
import sys

dl = int(input('Длина: '))
cr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
pas = []
for x in range(0, dl):
	crs = random.choice(cr)
	pas.append(crs)
print(''.join(pas))


print('Commands: /s сохраняет пароль. ex закрывает программу')
command = input()


if command == '/s':
	fname = input('Имя(без разширения): ')
	f = open(fname + '.txt', 'w')
	f.write(''.join(pas))
	print('Пароль сохранён')
if command == 'ex':
	sys.exit()