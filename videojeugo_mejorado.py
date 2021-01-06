import random


def run():
    intentos = 5
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un numero del 1 al 100: '))
    
    while numero_elegido != numero_aleatorio:
        if numero_elegido < 1 or numero_elegido > 100 or intentos == 0:
            print('Juego terminado')   
            break
        else:
            if(numero_elegido < numero_aleatorio):
                print('Busca un numero mas grande')
            elif(numero_elegido > numero_aleatorio):
                print('Busca un numero mas pequeno')
            else:
                print('Ganaste')
                break
            
            intentos -= 1

            numero_elegido = int(input('Elige otro numero: '))
    
    if intentos == 0:
        print('PERDISTE!')
    else:
        print('FELICIDADES GANASTE!')
          
    
if __name__ == "__main__":
    run()