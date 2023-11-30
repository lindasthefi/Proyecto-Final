import requests

def crear_repositorio(nombre, token):
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    payload = {
        "name": nombre,
        "private": False  # Cambia a True si deseas un repositorio privado
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        print(f"Repositorio '{nombre}' creado exitosamente en GitHub.")
    else:
        print(f"Error al crear el repositorio. Código de estado: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    nombre_repositorio = "Proyecto-Final"
    token_de_acceso = "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"

    crear_repositorio(nombre_repositorio, token_de_acceso)
