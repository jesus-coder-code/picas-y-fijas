import random

dig = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

numero_secreto = ''

for i in range(4):
	candidato = random.choice(dig)

	while candidato in numero_secreto:
		candidato = random.choice(dig)
	numero_secreto = numero_secreto + candidato

""" numero_secreto = input('jugador1, ingrese el numero de 4 digitos a adivinar: ') """

num = input('jugador2, adivina el numero: ')

intento = 1

def picas_y_fijas(numero_secreto, intento):
	fijas = 0;
	picas = 0;
	for i in range(4):
		if num[i] == numero_secreto[i]:
			fijas = fijas + 1
		elif num[i] in numero_secreto:
			picas = picas + 1
	dict = {
		"PICAS": picas,
		"FIJAS": fijas
	}
	return dict;
	

while num != numero_secreto:
	""" picas = 0
	fijas = 0 """

	""" for i in range(4):
		if num[i] == numero_secreto[i]:
			fijas = fijas + 1
		elif num[i] in numero_secreto:
			picas = picas + 1 """
	""" print(dict(PICAS = picas, FIJAS = fijas)) """
	hola = picas_y_fijas(numero_secreto, intento);
	print(hola);
	num = input('dame otro numero de 4 digitos: ')
	intento = intento + 1;

	if num == numero_secreto:
		break

print('codigo adivinado en ', intento, 'intentos')



