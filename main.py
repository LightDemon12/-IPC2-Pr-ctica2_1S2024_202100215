from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import threading
import tkinter as tk
import webbrowser
import requests
import tkinter.messagebox as messagebox
class Cliente:
    def __init__(self, nombre, correo, nit):
        self.nombre = nombre
        self.correo = correo
        self.nit = nit

app = Flask(__name__)
CORS(app)

# Lista para almacenar los clientes
clientes = [
    Cliente("Juan José Juárez Jiménez", "jujojuji@ingenieria.usac.edu.gt", "123456789"),
    Cliente("Ana Maria", "ana.maria@ingenieria.usac.edu.gt", "987654321"),
]

@app.route("/")
def index():
    return "Hello World!"

@app.route("/api", methods=["GET"])
def api():
    return jsonify({"message": "Hello World!"})

@app.route("/api/cliente", methods=["POST"])
def cliente():
    global clientes  # Indica que estamos utilizando la variable global 'clientes'
    data = request.get_json()
    nombre = data["nombre"]
    correo = data["correo"]
    nit = data["nit"]

    # Verificar si el NIT ya está en uso
    for cliente_existente in clientes:
        if cliente_existente.nit == nit:
            return jsonify({"error": "El NIT ya está en uso."}), 400

    # Si el NIT no está en uso, crear el cliente y agregarlo a la lista
    cliente = Cliente(nombre, correo, nit)
    clientes.append(cliente)
    return jsonify({"mensaje": "Cliente creado", "cliente": {
        "nombre": cliente.nombre,
        "correo": cliente.correo,
        "nit": cliente.nit
    }})



@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    return render_template('clientes.html', clientes=clientes)

def run_flask():
    app.run(debug=False, host='0.0.0.0', port=4000)



def boton_XML():
    nombre = text_input_nombre.get()
    correo = text_input_correo.get()
    nit = text_input_nit.get()

    # Crear el diccionario de datos para enviar al servidor
    data = {"nombre": nombre, "correo": correo, "nit": nit}

    # Enviar la solicitud al servidor Flask
    url = "http://localhost:4000/api/cliente"
    response = requests.post(url, json=data)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        messagebox.showinfo("Cliente Creado", "El cliente ha sido creado exitosamente.")
    elif response.status_code == 400:
        messagebox.showerror("Error", "El NIT ingresado ya está en uso. Por favor, ingrese un NIT único.")
    else:
        messagebox.showerror("Error", "Ocurrió un error al procesar la solicitud. Por favor, inténtelo de nuevo más tarde.")

def boton_gestion_maquetas():
    webbrowser.open("http://localhost:4000/api/clientes")


def run_tkinter():
    root = tk.Tk()
    root.title("Regisro de Clientes")

    # Etiquetas
    label_nombre = tk.Label(root, text="Nombre:")
    label_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="e")

    label_correo = tk.Label(root, text="Correo Electrónico:")
    label_correo.grid(row=1, column=0, padx=10, pady=5, sticky="e")

    label_nit = tk.Label(root, text="NIT:")
    label_nit.grid(row=2, column=0, padx=10, pady=5, sticky="e")

    # Entradas de texto
    global text_input_nombre, text_input_correo, text_input_nit  # Hacer estas variables globales para que estén disponibles en la función boton_XML
    text_input_nombre = tk.Entry(root)
    text_input_nombre.grid(row=0, column=1, padx=10, pady=5)

    text_input_correo = tk.Entry(root)
    text_input_correo.grid(row=1, column=1, padx=10, pady=5)

    text_input_nit = tk.Entry(root)
    text_input_nit.grid(row=2, column=1, padx=10, pady=5)

    # Crear los botones
    button_xml = tk.Button(root, text="Guardar Usuario", command=boton_XML)
    button_xml.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    button_gestion_maquetas = tk.Button(root, text="Ver listado de usuario", command=boton_gestion_maquetas)
    button_gestion_maquetas.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    root.mainloop()

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    tkinter_thread = threading.Thread(target=run_tkinter)
    tkinter_thread.start()
