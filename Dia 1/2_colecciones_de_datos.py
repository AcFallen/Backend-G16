# Puedo agrupar varios valores en una variable

# Listas
# Que se puede modificar, es ordenada (maneja indices)

alumnos = ['victor','hitoito','angel','bryan','samael','claudia']

# Las listas empiezan con la posicion 0

print(alumnos[0])
print(alumnos[4])

# Para saber el contenido (longitud) de datos

print(len(alumnos))

# Si queremos recorrer la lista de derecha a izquierda utilizaremos numeros negativos

print(alumnos[-1]) # !! es mas eficiente !!

print(alumnos[len(alumnos)-1])


# Agregar elementos a una lista ya creada
alumnos.append('Frankling')

print(alumnos)

# remover un elemento de la lista lo podemos guardar en una variable

alumno_eliminado = alumnos.pop(3)
print(alumnos)
print(alumno_eliminado)


# Las listas puedem tener varios tipos de datos

mixto = ['lunes',10,False,80.5,[1,2,3]]


# Ejercicio 

ejercicio = [1, 2, 3, [4, 5 ,6]]

# como puedo devolver el valor de 5

resultado = ejercicio [3]

print(resultado[1])

# como puedo devolver el valor de 3

print(ejercicio[2])

# tuplas
# No se pueden modificar y es ordenada (indices)
# se puede guardar valores que jamas se modificaran

meses = ('enero', 'febrero' , 'marzo' , 'abril')

print(meses[0])


data = ('juan', 'roberto', [1,2,3,['eduardo','frank']] )

# obtener eduardo
print(data[2][3][0])

# Set (Conjuntos)
# Desordenada y modificable

colores = {'negro' , 'blanco' , 'guinda' , 'violeta'}

print(colores)

print ('verde' in colores)

colores.remove('blanco')

# Diccionarios
# Ordenados pero por llaves y modificables

persona = {
    'nombre' : 'roberto',
    'edad' : 31 , 
    'nacionalidad' : 'peruano',
    'apellido' : 'de rivero'

}

print(persona.keys()) # llaves
print(persona.values()) # valores
print(persona['nombre']) 


persona = {
    'nombre':"Roberto",
    'edad': 40,
    'hobbies': ['Nada', 'Pescar', 'Jugar videojuegos'],
    'idiomas': [
        {
            'nombre': 'Ingles',
            'nivel': 'Intermedio'
        },
        {
            'nombre': 'Frances',
            'nivel': 'Basico'
        }
    ],
    'habilidades': {'Puntual', 'Economico', 'Proactivo'},
    'debilidades': ('Mentiroso', 'Resentido', 'Comelon')
}

# Darme la edad

print(persona['edad'])

# mostrar los hobbies

print(persona['hobbies'])

# mostrar el ultimo hobbie ingresado

print(persona['hobbies'][-1])

# mostrar los idiomas solo sus nombre

print(persona['idiomas'][0]['nombre'])
print(persona['idiomas'][1]['nombre'])

# ver si es proactivo

print ( 'Proactivo' in persona['habilidades'])

# ver cuantas debilidades tienes (cantidad)

print(len(persona['debilidades']))