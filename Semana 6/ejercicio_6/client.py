import requests # type: ignore

URL = "http://localhost:5000/notas"

def mostrar_menu():
    print("\n--- GESTIÓN DE NOTAS ---")
    print("1. Ver notas")
    print("2. Agregar nota")
    print("3. Eliminar nota")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        # Petición GET al servidor
        respuesta = requests.get(URL)
        for nota in respuesta.json():
            print(f"[{nota['id']}] {nota['contenido']}")

    elif opcion == "2":
        contenido = input("Contenido de la nota: ")
        # Petición POST con datos en formato JSON
        requests.post(URL, json={"contenido": contenido})
        print("Nota guardada en el servidor.")

    elif opcion == "3":
        id_nota = input("ID de la nota a eliminar: ")
        # Petición DELETE a una URL específica
        requests.delete(f"{URL}/{id_nota}")
        print("Solicitud de eliminación enviada.")

    elif opcion == "4":
        break