import random

dig = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

numero_secreto = ''

for i in range(4):
	candidato = random.choice(dig)

	while candidato in numero_secreto:
		candidato = random.choice(dig)
	numero_secreto = numero_secreto + candidato

#numero_secreto = input('jugador1, ingrese el numero de 4 digitos a adivinar: ')

num = input('jugador2, adivina el numero: ')

intento = 1

while num != numero_secreto:
	intento = intento + 1
	picas = 0
	fijas = 0

	for i in range(4):
		if num[i] == numero_secreto[i]:
			fijas = fijas + 1
		elif num[i] in numero_secreto:
			picas = picas + 1
	print(dict(PICAS = picas, FIJAS = fijas))
	num = input('dame otro numero de 4 digitos: ')

	if num == numero_secreto:
		break

print('codigo adivinado en ', intento, 'intentos')



