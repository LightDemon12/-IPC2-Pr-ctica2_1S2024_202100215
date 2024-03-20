from flask import Flask, render_template, request, jsonify
from client import Cliente
app = Flask(__name__)

clientes = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar_cliente', methods=['POST'])
def guardar_cliente():
    nombre = request.form['nombre']
    correo = request.form['correo']
    nit = request.form['nit']

    # Verificar si el cliente ya existe
    for cliente in clientes:
        if cliente.nit == nit:
            return 'El cliente ya existe'

    nuevo_cliente = Cliente(nombre, correo, nit)
    clientes.append(nuevo_cliente)
    return 'Cliente guardado correctamente'

@app.route('/getClientes')
def get_clientes():
    return jsonify(clientes=[cliente.__dict__ for cliente in clientes])

if __name__ == '__main__':
    app.run(debug=True)
