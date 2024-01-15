alumnos = ['angel','bryan','carlos','hiroito','claudia','samael','marco']

for alumno in alumnos:
    print(alumno)


# for se puede utilizar con string (textos)

frase = 'no hay mal que por bien no venga'

for letra in frase:
    if letra != ' ':
        print(letra)

# Forma 3
# continue > termina el ciclo actual (la iteracion en camino) y no permite hacer nada mas luego
# del continue
    
    if letra == ' ':
        continue
    print(letra)

# operador ternario solo se puede colocar en sus resultados PALABRAS NO CLAVES
# si no queremos realizar nada en un operador ternario podemos colocarlo ahi

None if letra == ' ' else print(letra)



# range > si quiero  realizar en for normal manual sin uso de listas, tuplas , set o texto
# range (limite) > el for se ejecutara hasta que el valor sea menor que el tope (limite)

for numero in range(4):
    print(numero)

# valor inicial , limite
print('-----------------------------')
for numero in range(1,4):
    print(numero)

print('-----------------------------')
# valor inicial , limite , incremento
for numero in range(1,10,2):
    print(numero)


# texto
print('-----------------------------')
texto = 'Hola me llamo eduardo'
vocales = ['a','e','i','o','u']

# iterar la variable texto y ver cuantas vocales hay
numero_vocal = 0

for letra in texto:
    for vocal in vocales:
        if letra == vocal:
            numero_vocal = numero_vocal + 1

print (numero_vocal)

print('-----------------------------')

contador = 0

for letra in texto:
    if letra in vocales:
        contador = contador + 1

print ('hay', contador , 'vocales')
print ('hay {} vocales'.format(contador))
print (f'hay {contador} vocales')


print('-----------------------------')
# operador llamado MODULO %

print(99/5) #cociente
print(99 % 5) # residuo entero
print(99 // 5) # cociente entero sin el uso de decimales


# utilizando range realice

print('-----------------------------')

range(1,56)
# quiero saber cuantos numeros pares tengo
p = 0

for numero in range (1,56):
    if numero %  2 == 0 :
        p = p + 1

print('tenemos' , p ,' numeros pares en el rango')