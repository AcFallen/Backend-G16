from flask import Flask, request

# > __name > Variable de python que sirve para indicar si el archivo que estamos utilizando 
# es principal del proyecto esto sirve para que la instancia de Flask solamente corra en el archivo
# evitar circunstancias de Flask en archivos secundarios de proyectos
app = Flask(__name__)


# Decoradores
# Sirve para utilizar un metodo sin la necesidad de modificarlo desde la clase en la cual estamos haciendo la referencia

@app.route('/', methods = ['GET' , 'POST', 'PUT'] )
def inicio():

    if request.method == 'PUT':
        return {
            'message': 'Actualizacion exitosa'
        },202
    elif request.method == 'GET':
        return{
            'message': 'Devolucion Exitosa'
        },200
    
    



    print(request.method)


    return {
        'message':'Bienvenido a mi primera Api con Flask',
        'content':'hola'
    }

#levantamos nuestro servidor de Flask
app.run(debug=True)