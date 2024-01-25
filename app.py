from flask import Flask
from  variables import conexion

app = Flask(__name__)

# Inicializar la conexion a nuetra BD
# al momento de pasarle la aplicacion de flask en esta se encontrara la cadena de conexion ala bd

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/alumnos'

conexion.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)