from flask_sqlalchemy import SQLAlchemy
from twilio.rest import Client
from os import environ
from dotenv import load_dotenv

load_dotenv()
conexion = SQLAlchemy()
cliente_twilio = Client(username=environ.get('TWILIO_ACCOUNT_SID'),
                        password=environ.get('TWILIO_AUTH_TOKEN'))
