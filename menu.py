def conversor( tipo_moneda, equivalencia ):
    dolares = input('Ingrese cantidad en dolares $:')
    dolares = float(dolares)
    resultado = dolares * equivalencia
    resultado = str(round(resultado,2))
    print('Su equivalencia en '+ tipo_moneda + ' es: ' +resultado ) 

menu = """ 
Bienvenido al menu 😁🙌

1-Pasar de dolares a euros.
2-Pasar de dolares a Pesos Mexicanos
3-Pasar de dolares a Colones Salvadoreños

"""
print(menu)
opcion = int(input('Elija un opción: '))
if opcion == 1:
    conversor( 'euros', 0.83)
elif opcion == 2:
    conversor( 'Pesos Mexicanos', 20.04)
elif opcion == 3:
    conversor( 'Colones Salvadoreños', 8.75)
else:
    print('Opción no valida.')
    
    