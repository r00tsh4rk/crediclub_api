"""
Archivo: conf.py
Descripción: Configuración central de la aplicación.
Actualización: 09/12/2022.
Lenguaje: Python
Framework: Flask 
Autor: Josue Alejandro Ruiz Chimal.
"""
class AppConfig():
    # Modo de depuración activo
    DEBUG = True
    # Datos de conexión a MySQL
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_HOST = '127.0.0.1'
    MYSQL_DB = 'crediclub'

config = {
    'dev_mod': AppConfig
}