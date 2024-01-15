# el while puede convertirse en un bucle infinito

numero = 10 
while numero < 20:
    print(numero)
    numero+=1

# el dowhile no existe en python
    
valor = input()

# adivina el numero
numero = 225
numero_adivinado = 0 

while numero_adivinado != numero:
    numero_adivinado = int(input('Porfavor ingresa un numero'))
    if numero_adivinado < numero:
        print('el numero es mayor')
    else:
        print('el numero es menor')

