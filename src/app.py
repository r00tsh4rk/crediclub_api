"""
Archivo: app.py
Descripción: Script central de la API.
Actualización: 08/12/2022.
Lenguaje: Python
Framework: Flask 
Autor: Josue Alejandro Ruiz Chimal.
"""

from flask import Flask, jsonify, request, Response
import pymysql
pymysql.install_as_MySQLdb()
from flask_mysqldb import MySQL
from conf import config

# Inicialización de la app de Flask
app = Flask(__name__)

#Estableciendo conexión
conexion = MySQL(app)

# Listar todos los clientes de la base de datos 
@app.route('/listar', methods=['GET'])
def getClientes():
    try:
        # Creando cursor para establcer conexión con la Base de datos
        cursor = conexion.connection.cursor()
        consulta = "SELECT * FROM creditos"
        cursor.execute(consulta)
        datos = cursor.fetchall()

        # Definiendo una lista de clientes
        clientes=[]
        for dato in datos:
            # Leyendo los clientes de la base de datos
            cliente = {'id_cliente': dato[0], 'nombre': dato[1], 'apellido_pat': dato[2], 'apellido_mat': dato[3], 'fecha_nacimiento': dato[4], 'rfc': dato[5], 'ingreso_mensual': dato[6], 'dependientes': dato[7], 'estatus_credito': dato[8]}
            # Agregando clientes a la lista 
            clientes.append(cliente)
        # Respuesta en formato json
        return jsonify({'clientes': clientes, 'mensaje': "Lista de clientes"})
        
    except Exception as e:
        # En caso de ocurrir un error se despliega un mensaje 
        return jsonify({'mensaje': "Error al listar los clientes"})

# Obtener cliente por su ID 
@app.route('/listar/<id>', methods=['GET'])
def getCliente(id):
    try:
        # Creando cursor para establcer conexión con la Base de datos
        cursor = conexion.connection.cursor()
        #Consulta SQL que obtiene un cliente basado en su indentificador único.
        consulta = "SELECT * FROM creditos WHERE id_cliente = %s" % id
        cursor.execute(consulta)
        datos = cursor.fetchone()
        
        if(datos != None):
            #Obteniendo cliente basado en si identificador en JSON 
            cliente = {'id_cliente': datos[0], 'nombre': datos[1], 'apellido_pat': datos[2], 'apellido_mat': datos[3], 'fecha_nacimiento': datos[4], 'rfc': datos[5], 'ingreso_mensual': datos[6], 'dependientes': datos[7], 'estatus_credito': datos[8]}
        # Definiendo una lista de clientes leida de la consulta para retornar en JSON 
            return jsonify({'cliente': cliente, 'mensaje': "Cliente encontrado"})
        else:
            return jsonify({'mensaje': "Cliente no encontrado"})
    except Exception as e:
        # En caso de ocurrir un error se despliega un mensaje 
        return jsonify({'mensaje': "Error al leer los datos de la consulta"})

# Función para consultar un registro de crédito de cliente mediante su ID, es utilizada para verbo DELETE de la API
def getClienteByID(id):
    try:
        cursor = conexion.connection.cursor()
        consulta = "SELECT * FROM creditos WHERE id_cliente = {0}".format(id)
        cursor.execute(consulta)
        datos = cursor.fetchone()
        
        if(datos != None):
            cliente = {'id_cliente': datos[0], 'nombre': datos[1], 'apellido_pat': datos[2], 'apellido_mat': datos[3], 'fecha_nacimiento': datos[4], 'rfc': datos[5], 'ingreso_mensual': datos[6], 'dependientes': datos[7], 'estatus_credito': datos[8]}
            return cliente
        else:
            return None
    except Exception as e:
        return e

# Función para consultar un registro de crédito de cliente mediante su RFC, es utilizada para validar que el registro no exista en la BD 
def getClienteByRFC(rfc):
    try:
        cursor = conexion.connection.cursor()
        consulta = "SELECT * FROM creditos WHERE rfc = '{0}'".format(rfc)
        cursor.execute(consulta)
        datos = cursor.fetchone()
        
        if(datos != None):
            cliente = {'id_cliente': datos[0], 'nombre': datos[1], 'apellido_pat': datos[2], 'apellido_mat': datos[3], 'fecha_nacimiento': datos[4], 'rfc': datos[5], 'ingreso_mensual': datos[6], 'dependientes': datos[7], 'estatus_credito': datos[8]}
            return cliente
        else:
            return None
    except Exception as e:
        return e

# Función para crear el RFC del cliente
def getRFC(nombre, apt_pat, apt_mat, fecha):
    rfc = apt_pat[0:2].upper() + apt_mat[0:1].upper() + nombre[0:1].upper() + fecha[-2:] + fecha[3:-5] + fecha[0:2]
    return rfc

# Insertar un nuevo crédito de cliente en la base de datos 
@app.route('/agregar', methods=['POST'])
def addCliente():
    rfc = getRFC(request.json['primer_nombre'], request.json['apellido_pat'], request.json['apellido_mat'], request.json['fecha_nacimiento'])
    try:
        cursor = conexion.connection.cursor()
        # Validando que el cliente no esté previamente registrado en la base de datos
        if(getClienteByRFC(rfc) != None):
            return jsonify({'mensaje': "Cliente con crédito ya aprobado y registrado."}) 
        else:  
            # Validar que los ingresos mensuales sean mayores de 25,000
            if(request.json['ingresos_mensuales']>25000): 
                consulta = """INSERT INTO creditos (primer_nombre, apellido_pat, apellido_mat, fecha_nacimiento, rfc, ingresos_mensuales, dependientes, estatus_credito)
                VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', {5}, {6}, '{7}')""".format(request.json['primer_nombre'], request.json['apellido_pat'], request.json['apellido_mat'],
                request.json['fecha_nacimiento'], rfc, request.json['ingresos_mensuales'], request.json['dependientes'], 'APROBADO')
                cursor.execute(consulta),
                conexion.connection.commit()
                return jsonify({'mensaje': "Cumple con los requisitos para la aprobación de su crédito.",
                'RFC_cliente': rfc, 'estatus_de_credito': 'APROBADO'})  

            # Si los ingresos mensuales son menores que 15,000, se rechaza la aprobación del crédito
            if(request.json['ingresos_mensuales']  < 15000):
                consulta = """INSERT INTO creditos (primer_nombre, apellido_pat, apellido_mat, fecha_nacimiento, rfc, ingresos_mensuales, dependientes, estatus_credito)
                VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', {5}, {6}, '{7}')""".format(request.json['primer_nombre'], request.json['apellido_pat'], request.json['apellido_mat'],
                request.json['fecha_nacimiento'], rfc, request.json['ingresos_mensuales'], request.json['dependientes'], 'NO APROBADO')
                cursor.execute(consulta),
                conexion.connection.commit()
                return jsonify({'mensaje': "Ingresos mensuales insuficientes para aprobación de crédito.",
                'RFC_cliente': rfc, 'estatus_de_credito': 'NO APROBADO'})

            # Si los ingresos se encuentra entre 15,000 y 25,000, se valida que el número de dependientes sea menor de 3 hijos.
            if(request.json['ingresos_mensuales']>= 15000 or request.json['ingresos_mensuales'] < 25000): 
                if(request.json['dependientes'] < 3):
                    consulta = """INSERT INTO creditos (primer_nombre, apellido_pat, apellido_mat, fecha_nacimiento, rfc, ingresos_mensuales, dependientes, estatus_credito)
                    VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', {5}, {6}, '{7}')""".format(request.json['primer_nombre'], request.json['apellido_pat'], request.json['apellido_mat'],
                    request.json['fecha_nacimiento'], rfc, request.json['ingresos_mensuales'], request.json['dependientes'], 'APROBADO')
                    cursor.execute(consulta),
                    conexion.connection.commit()
                    return jsonify({'mensaje': "Cumple con los requisitos para la aprobación de su crédito.",
                'RFC_cliente': rfc, 'estatus_de_credito': 'APROBADO'}) 
                else:
                    consulta = """INSERT INTO creditos (primer_nombre, apellido_pat, apellido_mat, fecha_nacimiento, rfc, ingresos_mensuales, dependientes, estatus_credito)
                    VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', {5}, {6}, '{7}')""".format(request.json['primer_nombre'], request.json['apellido_pat'], request.json['apellido_mat'],
                    request.json['fecha_nacimiento'], rfc, request.json['ingresos_mensuales'], request.json['dependientes'], 'NO APROBADO')
                    cursor.execute(consulta),
                    conexion.connection.commit()
                    return jsonify({'mensaje': "El número de dependientes económicos no cumple con el requisito para aprobación de crédito.",
                    'RFC_cliente': rfc, 'estatus_credito': 'NO APROBADO'})
            else:
                consulta = """INSERT INTO creditos (primer_nombre, apellido_pat, apellido_mat, fecha_nacimiento, rfc, ingresos_mensuales, dependientes, estatus_credito)
                VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', {5}, {6}, '{7}')""".format(request.json['primer_nombre'], request.json['apellido_pat'], request.json['apellido_mat'],
                request.json['fecha_nacimiento'], rfc, request.json['ingresos_mensuales'], request.json['dependientes'], 'NO APROBADO')
                cursor.execute(consulta),
                conexion.connection.commit()
                return jsonify({'mensaje': "Ingresos mensuales insuficientes para aprobación de crédito.",
                'RFC_cliente': rfc, 'estatus_de_credito': 'NO APROBADO'})

    except Exception as e:
        # En caso de ocurrir un error se despliega un mensaje 
        return jsonify({'mensaje': "Error al agregar al registrar el crédito del cliente, verifique información"})

# Función para actualizar la información del crédito de un cliente
@app.route('/actualizar/<id>', methods=['PUT'])
def updCliente(id):
    rfc = getRFC(request.json['primer_nombre'], request.json['apellido_pat'], request.json['apellido_pat'], request.json['fecha_nacimiento'])
    if (id, request.json['primer_nombre'] and request.json['apellido_pat'] and request.json['apellido_mat'] and request.json['fecha_nacimiento'] and
        request.json['ingresos_mensuales'] and request.json['dependientes']):
        try:
            if(getClienteByID(id) != None):
                cursor = conexion.connection.cursor()
                consulta = """UPDATE creditos SET primer_nombre = '{0}', apellido_pat = '{1}', apellido_mat = '{2}', 
                fecha_nacimiento = '{3}', rfc = '{4}', ingresos_mensuales = {5}, dependientes = {6}
                WHERE id_cliente = {7}""".format(request.json['primer_nombre'], request.json['apellido_pat'], request.json['apellido_mat'],
                request.json['fecha_nacimiento'], rfc, request.json['ingresos_mensuales'], request.json['dependientes'], id)
                cursor.execute(consulta)
                conexion.connection.commit() 

                return jsonify({'mensaje': "Información del cliente actualizada correctamente.", 'RFC_cliente': rfc})
            else:
                return jsonify({'mensaje': "Registro de cliente no encontrado.", 'RFC_cliente': rfc})
        except Exception as e:
            return jsonify({'mensaje': e})
    else:
        return jsonify({'mensaje': "Información de crédito de cliente invalida o faltante, favor de verificar la información"})

# Función para eliminar un registro de crédito de un cliente específico
@app.route('/eliminar/<id>', methods=['DELETE'])
def delCliente(id):
    try:
        cliente = getClienteByID(id)
        if cliente != None:
            cursor = conexion.connection.cursor()
            consulta = "DELETE FROM creditos WHERE id_cliente = '{0}'".format(id)
            cursor.execute(consulta)
            conexion.connection.commit() 

            return jsonify({'mensaje': "Registro de crédito eliminado con éxito."})
        else:
            return jsonify({'mensaje': "Registro de crédito del cliente no encontrado."})
    except Exception as e:
        return jsonify({'mensaje': "Error al eliminar el registro de crédito del cliente"})

# Función que despliega la página de error
def no_encontrada(error):
    return '<h1>Error: Página o recurso no encontrado</h1>', 404

# Desliegue de la aplicación en la URL: http://127.0.0.1:5000/
if __name__ == '__main__':
    # Carga de la configuración de la app
    app.config.from_object(config['dev_mod'])
    # Registro de pagina de error 
    app.register_error_handler(404, no_encontrada)
    # Ejecución de la app
    app.run()