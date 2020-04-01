import random

def num_random(intentos):
	numero = random.randint(0, 100)
	print (numero)
		
	for i in range (int(intentos)):
		ingr = int(input('Numero: '))

		if ingr == numero:
			print ('Correcto, el numero es ' ,numero, ', en ' ,i+1, ' intentos.')
			break
		elif ingr < numero:
			print('Mas grande!')
		else:
			print('Es menor!')
	else:
			print('Se terminaron los intentos')

x = input('Ingrese la cantidad de intentos: ')

num_random(x)


		
		



	
	

	
