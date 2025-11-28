from model import GestorTareas, Recordatorio

class TaskController:
    """
    Controlador principal del proyecto.
    Conecta la vista con el modelo: recibe acciones del usuario,
    ejecuta la lógica en el modelo y actualiza la interfaz.
    """

    def __init__(self):
        self.modelo = GestorTareas()
        self.recordatorio = Recordatorio()

    def agregar_tarea(self, titulo, descripcion, fecha, prioridad):
        """
        Recibe datos desde la vista y se los envía al Modelo.
        Luego reproduce un sonido de recordatorio.
        """
        self.modelo.agregar_tarea(titulo, descripcion, fecha, prioridad)
        self.recordatorio.sonar()

    def obtener_tareas(self):
        """
        Devuelve todas las tareas registradas.
        La Vista las usa para mostrar la lista.
        """
        return self.modelo.obtener_tareas()

    def eliminar_tarea(self, indice):
        """
        Elimina una tarea según la selección del usuario desde la Vista.
        """
        self.modelo.eliminar_tarea(indice)
