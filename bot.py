import os
import requests

# Conexión con tu base de datos NexusDB
SB_URL = os.getenv("SUPABASE_URL")
SB_KEY = os.getenv("SUPABASE_KEY")
HEADERS = {
    "apikey": SB_KEY, 
    "Authorization": f"Bearer {SB_KEY}", 
    "Content-Type": "application/json"
}

def enviar_resultado(loteria, hora, numero):
    # Esto enviará el número a tu Supabase automáticamente
    datos = {"loteria": loteria, "hora": hora, "numero": numero}
    url = f"{SB_URL}/rest/v1/Resultados"
    requests.post(url, headers=HEADERS, json=datos)
    print(f"Guardado: {loteria} {hora} -> {numero}")

if __name__ == "__main__":
    print("Robot Nexus iniciado...")
    # Aquí irá el escáner de las páginas de lotería

