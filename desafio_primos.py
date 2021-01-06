def comprobacion(numero):
    for i in range (2,numero):
        if numero % i == 0:
            print(numero,' no es un número primo.')
            print(i,"multiplicado por", numero//i ,"es",numero)
            break
        else:
            print('El número ', numero,' es primo.')
            break


def run():
    numero = int(input('(No use decimales) Escriba un número: '))
    comprobacion(numero)
    if numero < 3:
        print('El número debe ser mayor a 2.')


if __name__ == '__main__':
    run()