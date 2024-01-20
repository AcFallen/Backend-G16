from flask import Flask , request
from uuid import uuid4
from flask_cors import CORS


app = Flask(__name__)
#Para configurar los CORS lo hago de la siguiente manera
CORS(app=app, 
     # que metodos pueden acceder a mi API
     methods = ['GET','POST','PUT','DELETE'], 
     # desde que dominios se puede acceder a mi API
     origins = ['http://localhost:5500' , 'http://127.0.0.1:5500'],
     # que headers (cabezeras) pueden enviar a mi api
     allow_headers = ['accept','authorization','content-type'])

productos = [
    {
        'id': uuid4(),
        'nombre': 'Palta Fuerte',
        'precio': 7.50 , 
        'disponibilidad' : True

    },
    {
        'id': uuid4(),
        'nombre': 'Lechuga Carola',
        'precio': 1.50 , 
        'disponibilidad' : True

    }
]

@app.route('/', methods = ['GET'])
def inicio():
    return {
        'message': 'Bienvenido a la API de Productos'
    }, 200

@app.route('/productos', methods = ['GET'])
def gestionProductos():
    return{
        'message' : 'Los productos son',
        'content': productos
    }, 200

# si voy a recibir un paramtro dinamico, y eso lo voy a manejar internamente
@app.route('/producto/<uuid:id>', methods =['GET'])
def gestionProducto(id):

    for producto in productos:
        if id == producto['id']:
            return {
                'content' : producto
            }, 200
    return{
        'message' : 'El producto noe existe'
    }, 404


@app.route('/producto', methods=['POST'])
def crearProducto():
    data = request.get_json()
    data['id'] = uuid4()
    
    productos.append(data)
    return {
        'message' : 'Producto creado',
        'content' : data
    },201

if __name__ == '__main__':
    app.run(debug=True)