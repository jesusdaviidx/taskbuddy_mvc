import pygame

class Tarea:
    """
    Representa una tarea individual.
    Aplica encapsulamiento mediante atributos protegidos.
    """

    def __init__(self, titulo: str, descripcion: str, fecha: str, prioridad: str):
        self._titulo = titulo
        self._descripcion = descripcion
        self._fecha = fecha
        self._prioridad = prioridad

    # Getters (encapsulamiento)
    @property
    def titulo(self):
        return self._titulo

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def fecha(self):
        return self._fecha

    @property
    def prioridad(self):
        return self._prioridad

    def __str__(self):
        """
        Ejemplo de polimorfismo: representación distinta al convertir el objeto a cadena.
        """
        return f"{self._titulo} – {self._fecha} ({self._prioridad})"


class GestorTareas:
    """
    Clase que maneja la lógica de negocio:
    agrega, elimina y devuelve tareas.
    """

    def __init__(self):
        self._tareas = []

    def agregar_tarea(self, titulo, descripcion, fecha, prioridad):
        tarea = Tarea(titulo, descripcion, fecha, prioridad)
        self._tareas.append(tarea)

    def obtener_tareas(self):
        return self._tareas

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self._tareas):
            self._tareas.pop(indice)


class Recordatorio:
    """
    Clase que maneja los sonidos de notificación.
    Usa pygame (librería externa obligatoria).
    """

    def __init__(self):
        pygame.mixer.init()

    def sonar(self):
        """
        Reproduce un sonido de recordatorio.
        """
        pygame.mixer.music.load("sonido_recordatorio.mp3")
        pygame.mixer.music.play()
