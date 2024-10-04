import os

os.system("cls")

# Almacenaniento de Datos
tareas = [
    ("Estudiar para el examen", "Revisar capítulos 1 a 5", "en progreso"),
    ("Hacer ejercicio", "Ir al gimnasio por 1 hora", "completada"),
    ("Llamar al médico", "Solicitar una cita para chequeo", "pendiente"),
    ("Enviar el informe", "Enviar el informe a mi jefe por correo", "en progreso")
]

ingreso_gestion = int(input("""Bienvenido al sistema de gestión de tareas
1. Agregar Tarea
2. Eliminatr Tarea
3. Actualizar tarea
4. Mostrar Tareas
5. Filtrar Tareas
6. Guardar Tareas
7. Cargar Tareas
8. Salir
Ingrese una opción: """))


if 1 == 1:
    os.system("cls")
    print("Tarea Agregada")

if 2 == 2:
    os.system("cls")
    print("Tarea Eliminada")

if 3 == 3:
    os.system("cls")
    print("Estado Actualizado")

if 4 == 4:
    os.system("cls")
    print("Las Tareas Asignadas son: ",tareas)

if 5 == 5:
    os.system("cls")
    print("Estamos programando")
    
if 6 == 6:
    os.system("cls")
    print("Estamos programando")

if 7 == 7:
    os.system("cls")
    print("Estamos programando")



print("   ( ͡• ͜ʖ ͡•)")