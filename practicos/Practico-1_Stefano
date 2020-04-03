import random
def adivina(n_intentos):
    n_random = random.randint(0, 100)
    
    for i in range (int(n_intentos)):
        print("Intento", i+1, "para acertar el número.")
        n_user = int( input('Me siento con suerte con el: ') )
        
        if n_random == n_user: 
            print("HA ACERTADO EN", i+1, "INTENTOS, USTED ES UN GENIO")
            break;
        elif n_random < n_user and i != (int(n_intentos)-1):
            print("Un poco más chico, che!")
        elif n_random > n_user and i != (int(n_intentos)-1):
            print("Ay... más grande")    
        else: 
            print("No acertaste :/ Se acabaron los intentos, lo 100to")

n_intentos = input('Este programa lo desafía a divinar un número ¿En cuántos intentos se cree capaz?  ')    
adivina(n_intentos)
