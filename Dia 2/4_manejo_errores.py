numero = 10

# try (intentalo)
try:
    print (10/0)
except:
    print('operacion incorrecta')


# crear una funcion que reciba dos numeros y devuelva cual es el mayor
# si el usuario ingresa un valor que no sea un numero entonces volver a pedirselo hasta que se un numero
    
def numeroMayor(numero1, numero2):
    return numero1 if numero1 > numero2 else numero2


while True:
    try:
        numero1 = int(input('ingresa el primer numero:'))
        numero2 = int(input('ingresa el segundo numero:'))
        resultado = numeroMayor(numero1,numero2)

        print ('el numero mayor es {}'.format(resultado))
        break
    except:
        print('tienes que ingresar solo numeros')