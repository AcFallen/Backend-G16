edad = 20
nacionalidad = 'venezolano'

if edad > 18 and nacionalidad == 'peruano':
    print('puedes votar')
else:
    print('no puedes votar')


# Segun el sexo y la estatura hacer lo siguiente
# si es Masculino
    # si mide mas de 1.50 entonces indicar que no hay prendas
    # si mide entre 1.30 y 1.49 indicar que si hay ropa
    # si mide menos de 1.30 indicar que no hay prendas
# si es Femenino
    # si mide mas de 1.40 indicar que no hay prendas
    # si mide entre 1.10 y 1.49 indicar que si hay
    # si mide menos de 1.10 indicar que no hay

sexo = 'Masculino'
estatura = 1.35
# output > SI HAY ROPA

sexo = 'Masculino'
estatura = 1.80
# output > NO HAY ROPA

sexo = 'Femenino'
estatura = 1.20
# output > SI HAY ROPA

sexo = 'Femenino'
estatura = 1.08
# output > NO HAY ROPA

if sexo == 'Masculino':
    if estatura < 1.30:
        print('No hay ropa')
    elif estatura < 1.50:
        print('si hay ropa')
    elif estatura > 1.50:
        print( 'no hay ropa')
elif sexo == 'Femenino':
    if estatura < 1.10:
        print('No hay ropa')
    elif estatura < 1.50:
        print('si hay ropa')
    elif estatura > 1.40:
        print( 'no hay ropa')


# OPERADOR TERNARIO
# Condicion que sirve para ejecutarse en una sola linea

nacionalidad = 'peruano'

if nacionalidad == 'peruano':
    print('paga 5 soles')
else:
    print('paga 8 soles')


# RESULTADO SI ES VERDADERO                                 ELSE RESULTADO SI ES FALSE

resultado = 'pague 5 soles' if nacionalidad == 'peruano' else 'pague 8 soles'

print(resultado)