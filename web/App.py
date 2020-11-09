from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
import requests
import json
from werkzeug import secure_filename

app = Flask(__name__)


@app.route('/')
def listarEntradas():
    entradas_list = requests.get('http://127.0.0.1:3000/').json()
    return render_template('index.html', entrada = entradas_list)

@app.route('/agregar_entrada')
def agregar_entrada():
    return render_template('agregar_entrada.html')

@app.route('/nueva_entrada', methods=['POST'])
def nueva_entrada(): 
    if request.method == 'POST':
        parametros = request.form['parametros']
        dataset = request.form['dataset']
        archivo = request.form['archivo']
        descripcion = request.form['descripcion']
        tipo_producto = request.form['tipo_producto']
        nombre_producto = request.form['nombre_producto']
        print('2:' + str(type(request.form)))
        requests.post('http://127.0.0.1:3000/nueva_entrada', json = json.dumps(request.form))
        return redirect(url_for('listarEntradas'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_entrada(id):
    data = requests.get('http://127.0.0.1:3000/edit/'+id).json()
    return render_template('editar_entrada.html', entrada  = data)

@app.route('/update/<id>', methods=['POST'])
def actualizar_entrada(id):
    if request.method == 'POST':
        parametros = request.form['parametros']
        dataset = request.form['dataset']
        archivo = request.form['archivo']
        descripcion = request.form['descripcion']
        tipo_producto = request.form['tipo_producto']
        nombre_producto = request.form['nombre_producto']
        print(type(json.dumps(request.form)))
        requests.put('http://127.0.0.1:3000/update/'+id, json = json.dumps(request.form))
        return redirect(url_for('listarEntradas'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def eliminar_entrada(id):
    requests.delete('http://127.0.0.1:3000/delete/'+id)
    return redirect(url_for('listarEntradas'))

if __name__ == "__main__":
    app.run(port=8000, debug=True)
