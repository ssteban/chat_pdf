import requests
from datetime import datetime, timedelta

def obtenerfecha():
    try:
        response = requests.get("http://worldclockapi.com/api/json/utc/now")
        data = response.json()

        # Extraer fecha en UTC
        utc_datetime_str = data["currentDateTime"]  # ej: "2025-07-24T22:25Z"
        utc_datetime = datetime.strptime(utc_datetime_str, "%Y-%m-%dT%H:%MZ")

        # Ajustar a hora de Bogotá (UTC -5)
        bogota_time = utc_datetime - timedelta(hours=5)
        solo_fecha = bogota_time.strftime("%Y-%m-%d")

        return solo_fecha

    except Exception as e:
        print("Error al conectarse al servidor de hora:", e)
        return {"error": f"Error al conectarse al servidor de hora: {str(e)}"}