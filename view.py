import tkinter as tk
from tkinter import ttk

class TaskBuddyView:
    """
    Vista del sistema TaskBuddy.
    Se encarga únicamente de la interfaz gráfica.
    No maneja lógica de negocio (cumple MVC).
    """

    def __init__(self, controlador):
        self.controlador = controlador

        # Ventana principal
        self.root = tk.Tk()
        self.root.title("TaskBuddy – Recordatorio de tareas")
        self.root.geometry("400x500")

        # ---- Campos de entrada ----
        tk.Label(self.root, text="Título").pack()
        self.entry_titulo = tk.Entry(self.root)
        self.entry_titulo.pack()

        tk.Label(self.root, text="Descripción").pack()
        self.entry_desc = tk.Entry(self.root)
        self.entry_desc.pack()

        tk.Label(self.root, text="Fecha (dd/mm/aaaa)").pack()
        self.entry_fecha = tk.Entry(self.root)
        self.entry_fecha.pack()

        tk.Label(self.root, text="Prioridad").pack()
        self.entry_prioridad = ttk.Combobox(self.root, values=["Alta", "Media", "Baja"])
        self.entry_prioridad.pack()

        # Botón para agregar tarea
        tk.Button(self.root, text="Agregar tarea",
                  command=self.agregar).pack(pady=10)

        # ---- Lista de tareas ----
        tk.Label(self.root, text="Lista de tareas").pack()
        self.lista = tk.Listbox(self.root, height=12)
        self.lista.pack(fill=tk.BOTH, expand=True)

        # Botón para eliminar
        tk.Button(self.root, text="Eliminar seleccionada",
                  command=self.eliminar).pack(pady=10)

    # ---------------------------------------------------
    #        MÉTODOS DE LA VISTA QUE USAN EL CONTROLADOR
    # ---------------------------------------------------

    def agregar(self):
        """
        Envía datos al controlador para agregar una tarea.
        Luego actualiza la vista.
        """
        self.controlador.agregar_tarea(
            self.entry_titulo.get(),
            self.entry_desc.get(),
            self.entry_fecha.get(),
            self.entry_prioridad.get()
        )
        self.actualizar()

    def eliminar(self):
        """
        Envía al controlador qué tarea se desea eliminar.
        """
        seleccion = self.lista.curselection()
        if seleccion:
            self.controlador.eliminar_tarea(seleccion[0])
            self.actualizar()

    def actualizar(self):
        """
        Refresca la lista de tareas desde el controlador.
        """
        self.lista.delete(0, tk.END)
        for tarea in self.controlador.obtener_tareas():
            self.lista.insert(tk.END, str(tarea))

    def iniciar(self):
        """
        Inicia el loop de la aplicación.
        """
        self.root.mainloop()
