tareas = []

def mostrar_menu():
    print("/n📌 MENU DEL GESTOR DE TAREAS📌")
    print("1. agregar  tareas")
    print("2. ver tareas")
    print("3. marcar tarea como completada")
    print("4. eliminar tarea")
    print("5. salir")
    
def agregar_tarea():
    terea = input("escribe la nueva tarea: ")
    tareas.append(terea)
    print(f"✅terea {terea} agregada con exito.")
    
def ver_tereas():
    if not tareas:
        print("📭 no hay tareas pendientes.")
    else:
        print("/n📋 lista de tareas:")
        for i, tarea in enumerate(tareas, 1): 
            print(f"{i}. '{tarea}' ")
            
def completar_tarea():
    ver_tereas()
    if tareas:
        try:
            indice = int(input("ingrese el numero de la tarea completada: ")) - 1
            if 0 <= indice < len(tareas):
                print(f"✔ tarea '{tareas[indice]}' completada y eliminada.")
                tareas.pop(indice)
            else:
                print("⚠ numero invalido.")
        except ValueError:
            print("⚠ ingresa un numero valido")
            
def eliminar_tarea():
    ver_tereas()
    if tareas:
        try:
            indice = int(input("ingrese el numero de la tarea a eliminar: ")) - 1
            if 0 <= indice < len(tareas):
                print(f"🗑 tarea '{tareas[indice]}' eliminada")
                tareas.pop(indice)
            else:
                print("⚠ numero invalido.")
        except ValueError:
            print("⚠ ingresa en numero valido.")
            
while True:
    mostrar_menu()
    opcion = input("selecciona una opcion (1-5): ")
    
    if opcion == "1":
        agregar_tarea
    elif opcion == "2":
        ver_tereas()
    elif opcion == "3":
        completar_tarea
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        print("🖐 ¡hasta luego!")
        break
    else:
        print("⚠ opcion no valida. intenta de nuevo.")