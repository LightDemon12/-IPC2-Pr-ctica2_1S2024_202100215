import tkinter as tk

def guardar_cliente():
    global nombre_entry, correo_entry, nit_entry
    nombre = nombre_entry.get()
    correo = correo_entry.get()
    nit = nit_entry.get()
    # Aquí deberías hacer una solicitud POST a tu endpoint /guardar_cliente
    # con los datos del cliente

def mostrar_clientes():
    # Aquí deberías hacer una solicitud GET a tu endpoint /getClientes
    # y mostrar los clientes en una tabla
    pass

# Creación de la instancia de Tk fuera de las funciones
root = tk.Tk()
root.title('Registro de Clientes')

# Creación de widgets y configuración de la interfaz
nombre_label = tk.Label(root, text='Nombre:')
nombre_label.grid(row=0, column=0)
nombre_entry = tk.Entry(root)
nombre_entry.grid(row=0, column=1)

correo_label = tk.Label(root, text='Correo:')
correo_label.grid(row=1, column=0)
correo_entry = tk.Entry(root)
correo_entry.grid(row=1, column=1)

nit_label = tk.Label(root, text='NIT:')
nit_label.grid(row=2, column=0)
nit_entry = tk.Entry(root)
nit_entry.grid(row=2, column=1)

guardar_button = tk.Button(root, text='Guardar Cliente', command=guardar_cliente)
guardar_button.grid(row=3, column=0, columnspan=2)

mostrar_button = tk.Button(root, text='Mostrar Clientes', command=mostrar_clientes)
mostrar_button.grid(row=4, column=0, columnspan=2)

# Ejecución del bucle principal de la interfaz
root.mainloop()
