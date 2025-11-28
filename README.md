TaskBuddy – Sistema de Recordatorio de Tareas (POO + MVC)

1. Descripción general

TaskBuddy es una aplicación de escritorio desarrollada en Python que permite gestionar tareas pendientes de una forma simple y organizada.
El proyecto fue creado aplicando los principios de Programación Orientada a Objetos (POO) junto con la arquitectura MVC (Modelo – Vista – Controlador), para garantizar una estructura de software clara, modular y fácil de mantener.

Este sistema busca ofrecer una solución básica pero funcional para que cualquier usuario pueda escribir sus tareas del día, almacenarlas y consultarlas cuando lo necesite. Además, incluye una pequeña función de recordatorios que ayuda a evitar que las tareas importantes pasen por alto.

2. Objetivo del software

El propósito principal de TaskBuddy es brindar una herramienta sencilla para el manejo de pendientes diarios.
Está pensado como un programa liviano que no requiere instalación ni configuraciones avanzadas, pero que aun así permite al usuario:

Registrar sus tareas rápidamente
Mantener un listado ordenado
Consultar sus tareas sin complicaciones
Recordar actividades importantes mediante mensajes emergentes

El enfoque es que cualquier persona, incluso sin conocimientos técnicos, pueda usarlo sin dificultad.

3. Funcionalidades

Registrar nuevas tareas
El usuario puede escribir una tarea y agregarla a la lista con un botón.

Guardar las tareas en una lista local
Las tareas se almacenan en memoria durante la ejecución para una consulta rápida.

Mostrar todas las tareas registradas
Un listado muestra en tiempo real todo lo que se ha agregado.

Seleccionar una tarea y recibir un recordatorio
Al elegir una tarea del listado, el sistema genera un mensaje recordatorio.

Interfaz gráfica intuitiva con tkinter
La aplicación presenta una ventana simple, con botones claros y una distribución amigable.

4. Arquitectura del sistema (MVC)

TaskBuddy está organizado siguiendo el modelo MVC, lo cual permite separar la lógica del programa, la interfaz y el controlador que los conecta.

Modelo (Model)

El modelo es el encargado de gestionar toda la información. Sus responsabilidades incluyen:

Guardar internamente la lista de tareas
Agregar nuevas tareas al registro
Retornar las tareas cuando el controlador las solicite
Mantener encapsulados los datos para evitar modificaciones directas

Vista (View)

La vista corresponde a la interfaz construida con tkinter, que permite la interacción con el usuario. Incluye:

Un campo para escribir tareas
Botón para agregar nuevas tareas
Un Listbox donde se muestran todas las tareas
Botón para desplegar el recordatorio de la tarea seleccionada

Controlador (Controller)

El controlador actúa como puente entre el modelo y la vista. Sus funciones principales son:

Recibir la tarea escrita por el usuario y enviarla al modelo
Actualizar el listado de tareas mostrado en la vista
Detectar qué tarea se seleccionó y llamar al recordatorio correspondiente

5. Programación Orientada a Objetos (POO)

Abstracción

Se utiliza una clase base llamada RecordatorioBase, que define el comportamiento general de cualquier recordatorio.

Herencia

La clase RecordatorioTarea hereda de la clase base para especializar el método encargado de mostrar recordatorios.

Polimorfismo

El método mostrar_recordatorio() se sobrescribe en la clase hija, permitiendo que cada tipo de recordatorio pueda comportarse de manera distinta.

Encapsulamiento

La lista de tareas del modelo se mantiene como un atributo privado para evitar accesos directos desde otros componentes.

