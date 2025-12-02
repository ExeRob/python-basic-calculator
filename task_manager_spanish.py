tareas = []

def mostrar_tareas():
    if not tareas:
        print("\n📋 No hay tareas registradas.")
    else:
        print("\n📋 Lista de tareas:")
        for i, tarea in enumerate(tareas, start=1):
            estado = "✔️ Completada" if tarea["completada"] else "❌ Pendiente"
            print(f"{i}. {tarea['nombre']} - {estado}")

def agregar_tarea():
    nombre = input("\n👉 Ingresá el nombre de la tarea: ")
    tareas.append({"nombre": nombre, "completada": False})
    print("✅ Tarea agregada.")

def completar_tarea():
    mostrar_tareas()
    try:
        num = int(input("\n👉 Número de la tarea a marcar como completada: "))
        tareas[num-1]["completada"] = True
        print("✔️ Tarea completada.")
    except (ValueError, IndexError):
        print("⚠️ Opción inválida.")

def eliminar_tarea():
    mostrar_tareas()
    try:
        num = int(input("\n👉 Número de la tarea a eliminar: "))
        tarea = tareas.pop(num-1)
        print(f"🗑️ Tarea '{tarea['nombre']}' eliminada.")
    except (ValueError, IndexError):
        print("⚠️ Opción inválida.")

def menu():
    while True:
        print("\n==== Gestor de Tareas ====")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("👉 Elegí una opción: ")

        if opcion == "1":
            mostrar_tareas()
        elif opcion == "2":
            agregar_tarea()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("👋 Saliendo del gestor. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida, probá de nuevo.")

if __name__ == "__main__":
    menu()