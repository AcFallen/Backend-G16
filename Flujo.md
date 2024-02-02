1. Crear una instancia de flask
2. Crear la conexion en variables.py
    1. configurar el link de conexion
3. Crear la instancia de migraciones
    1. usar FLASK DB INIT
    ``` 
        Migrate(app=app , db=conexion)
    ```
4. Crear la variable de entorno en el archivo .env

5. activar el entorno
    ```
    source entorno_flask_sql_alchemy/scripts/activate
    ```