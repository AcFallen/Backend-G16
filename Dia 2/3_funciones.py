# def > definition

def saludar():
    print('hola')

saludar()


def sumar(numero1,numero2):
    resultado =numero1+numero2
    print('el resultado es',resultado)

sumar(10,20)


def multiplicar(numero1,numero2):
    resultado = numero1 * numero2
    return resultado

resultado_multiplicacion = multiplicar(10,10)
print(resultado_multiplicacion)


# parametros opcionales

def saludarCordialmente(nombre,cargo='Senior'):
    return 'buenas noches {} {}'.format(cargo,nombre)


print(saludarCordialmente('roberto'))


# # el * al momento de declarar una funcion indicaremos que recibiremos n parametros
# def sumarNumeros(*args):
#     return args

# resultado = sumarNumeros(10,20,30,40,50,60,70,80,90)

# print(resultado)


# print('--------------------')
# contador = 0

# for numero in resultado:
#     contador = numero + contador

# print(contador)



# el * al momento de declarar una funcion indicaremos que recibiremos n parametros


def sumarNumeros(*args):
    contador = 0
    for numero in args:
        contador = numero + contador
    return contador

resultado = sumarNumeros(10,20,30,40,50,60,70,80,90)

print(resultado)


print('--------------')

def capturarPersona(**kwargs):
    return kwargs

resultado = capturarPersona(nombre='eduardo',
                apellido='de rivero',
                correo='exaple.gmail',
                estatura = 1.87)


print(resultado)

data = {
    'nombre':'eduardo',
    'apellido':'de rivero',
    'correo':'exaple.gmail',
    'estatura' : 1.87
}

# get solo sirve para devolver informacion mas no para saignar nuevos valores
print(data.get('apellido'))
data['edad'] = 30

print(data)