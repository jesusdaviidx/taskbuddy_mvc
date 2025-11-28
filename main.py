from controller.task_controller import TaskController

def main():
    controller = TaskController()

    while True:
        print("\n===== TASKBUDDY =====")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            descripcion = input("Descripción de la tarea: ")
            controller.agregar_tarea(descripcion)

        elif opcion == "2":
            controller.mostrar_tareas()

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
