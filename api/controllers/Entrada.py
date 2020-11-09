from flask import Flask, render_template, redirect, url_for, flash, jsonify
from db.db import cnx
import json
import ast

app = Flask(__name__)

class Entrada():
    global cur
    cur = cnx.cursor()

    def list():
        cur.execute('SELECT * FROM entrada')
        data = cur.fetchall()
        return data
        cnx.close

    def findOne(id):
        cur.execute('SELECT * FROM entrada WHERE id = {0}'.format(id))
        data = cur.fetchall()
        return json.dumps(ast.literal_eval(json.dumps(data[0])))
        cnx.close

    def create(entrada):
        entrada = entrada.replace("\\", "")[1:-1]
        body = ast.literal_eval(entrada)
        data = (body['parametros'],body['dataset'],body['archivo'],body['descripcion'],body['tipo_producto'],body['nombre_producto'])
        sql_insert = "INSERT INTO entrada (parametros,dataset,archivo,descripcion,tipo_producto,nombre_producto) VALUES (%s,%s,%s,%s,%s,%s)"
        cur.execute(sql_insert, data)
        cnx.commit()
        return {'estado': 'Insertado'},201


    def edit(entrada, id):
        entrada = entrada.replace("\\", "")[1:-1]
        body = ast.literal_eval(entrada)
        data = (body['parametros'],body['dataset'],body['archivo'],body['descripcion'],body['tipo_producto'],body['nombre_producto'],id)
        cur.execute("""UPDATE entrada
            SET parametros = %s,
                dataset = %s,
                archivo = %s,
                descripcion = %s,
                tipo_producto = %s,
                nombre_producto = %s
            WHERE id = %s
        """, (data))
        cnx.commit()
        return {'estado': 'Actualizado'},201

    def delete(id):
        cur.execute('DELETE FROM entrada WHERE id = {0}'.format(id))
        cnx.commit()
        return {'estado': 'Eliminado'},200

if __name__ == "__main__":
    app.run(port=3000, debug=True)