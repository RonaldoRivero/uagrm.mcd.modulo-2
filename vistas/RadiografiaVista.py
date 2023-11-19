from negocios.RadiografiaNegocio import RadiografiaNegocio
import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd


class CRUDApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Modulo 2")
        self.__radiografia_negocio = RadiografiaNegocio()
        self.__registro_seleccionado = None

        self.df = pd.DataFrame(columns=['Nombre_imagen', 'Formato_imagen', 'Dimension_imagen', 'Ruta_imagen'])

        self.label_tipo = ttk.Label(root, text="Tipo de imagen:")
        self.combo_tipo = ttk.Combobox(root, values=["normal", "covid", "neumonia viral", "opacidad pulmonar"])
        self.combo_tipo.set("normal")
        self.btn_mostrar = ttk.Button(root, text="Mostrar", command=self.mostrar_registros)

        # Crear widgets
        self.label_nombre = ttk.Label(root, text="Nombre de la imagen:")
        self.entry_nombre = ttk.Entry(root)

        self.label_formato = ttk.Label(root, text="Formato de la imagen:")
        self.entry_formato = ttk.Entry(root)

        self.label_dimension = ttk.Label(root, text="Dimension de la imagen:")
        self.entry_dimension = ttk.Entry(root)

        self.label_ruta = ttk.Label(root, text="Ruta de la imagen:")
        self.entry_ruta = ttk.Entry(root)

        self.label_archivo = ttk.Label(root, text="Seleccionar archivo:")
        self.entry_archivo = ttk.Entry(root)
        self.btn_seleccionar_archivo = ttk.Button(root, text="Seleccionar", command=self.seleccionar_archivo)

        self.btn_agregar = ttk.Button(root, text="Agregar", command=self.agregar_registro)

        # Botones para actualizar y eliminar
        self.btn_actualizar = ttk.Button(root, text="Actualizar", command=self.actualizar_registro)
        self.btn_eliminar = ttk.Button(root, text="Eliminar", command=self.eliminar_registro)

        # Diseño de la interfaz
        self.label_tipo.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.combo_tipo.grid(row=0, column=1, padx=10, pady=5)
        self.btn_mostrar.grid(row=0, column=2, padx=10, pady=5)

        self.label_nombre.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=5)

        self.label_formato.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_formato.grid(row=2, column=1, padx=10, pady=5)

        self.label_dimension.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_dimension.grid(row=3, column=1, padx=10, pady=5)

        self.label_ruta.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_ruta.grid(row=4, column=1, padx=10, pady=5)

        self.label_archivo.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_archivo.grid(row=5, column=1, padx=10, pady=5)
        self.btn_seleccionar_archivo.grid(row=5, column=2, padx=10, pady=5)

        self.btn_agregar.grid(row=6, column=0, columnspan=2, pady=10)

        self.btn_actualizar.grid(row=9, column=0, pady=10)
        self.btn_eliminar.grid(row=9, column=1, pady=10)

        # Crear una tabla para mostrar los registros
        self.tree = ttk.Treeview(root, columns=self.df.columns, show='headings')
        for i, col in enumerate(self.df.columns):
            self.tree.heading(i, text=col)
            self.tree.column(i, width=100)
        self.tree.grid(row=8, column=0, columnspan=4, padx=10, pady=5)

        # Configurar la selección de fila en la tabla
        self.tree.bind("<ButtonRelease-1>", self.seleccionar_fila)

    def seleccionar_archivo(self):
        ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo",
                                                  filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.gif")])
        if ruta_archivo:
            self.entry_archivo.delete(0, tk.END)
            self.entry_archivo.insert(0, ruta_archivo)

    def agregar_registro(self):
        tipo = self.combo_tipo.get()
        nombre = self.entry_nombre.get()
        formato = self.entry_formato.get()
        dimension = self.entry_dimension.get()
        ruta = self.entry_ruta.get()
        archivo = self.entry_archivo.get()
        # Copiar el archivo al directorio del proyecto
        '''
        if archivo:
            nuevo_nombre_archivo = f"{nombre}.{formato}"  # Cambiar el nombre del archivo si es necesario
            nuevo_path = f"ruta/del/proyecto/{nuevo_nombre_archivo}"  # Cambiar la ruta del proyecto
            shutil.copy(archivo, nuevo_path)
        '''
        self.__radiografia_negocio.registrar(tipo, nombre, formato, dimension, ruta)
        self.limpiar_formulario()
        self.actualizar_tabla()

    def mostrar_registros(self):
        self.actualizar_tabla()

    def actualizar_tabla(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        lista = self.__radiografia_negocio.listar(self.combo_tipo.get())
        for row in lista:
            self.tree.insert("", "end", values=tuple(row))

    def seleccionar_fila(self, event):
        item = self.tree.selection()
        if item:
            values = self.tree.item(item, "values")
            self.__registro_seleccionado = values
            self.limpiar_formulario()
            self.entry_nombre.insert(0, values[0])
            self.entry_formato.insert(0, values[1])
            self.entry_dimension.insert(0, values[2])
            self.entry_ruta.insert(0, values[3])

    def actualizar_registro(self):
        if self.__registro_seleccionado is not None:
            nombre_a_actualizar = self.__registro_seleccionado[0]
            tipo = self.combo_tipo.get()
            nombre = self.entry_nombre.get()
            formato = self.entry_formato.get()
            dimension = self.entry_dimension.get()
            ruta = self.entry_ruta.get()
            archivo = self.entry_archivo.get()

            self.__radiografia_negocio.actualizar(tipo, nombre_a_actualizar, nombre, formato, dimension, ruta)
            self.limpiar_formulario()
            self.actualizar_tabla()
        else:
            tk.messagebox.showinfo("Error", f"No selecciono un registro.")

    def eliminar_registro(self):
        if self.__registro_seleccionado is not None:
            nombre_a_eliminar = self.__registro_seleccionado[0]
            tipo = self.combo_tipo.get()

            self.__radiografia_negocio.eliminar(tipo, nombre_a_eliminar)
            self.limpiar_formulario()
            self.actualizar_tabla()
        else:
            tk.messagebox.showinfo("Error", f"No selecciono un registro.")

    def limpiar_formulario(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_formato.delete(0, tk.END)
        self.entry_dimension.delete(0, tk.END)
        self.entry_ruta.delete(0, tk.END)
        self.entry_archivo.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()