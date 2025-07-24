from fastapi import FastAPI, UploadFile, Request, File
import requests
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import base64
from io import BytesIO
from PyPDF2 import PdfReader
import uvicorn
from datetime import datetime, timedelta

app = FastAPI()
app.add_middleware(CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

def cargarInfoDB(usuario, pdf_base, contenido_pdf, nombre_pdf):

    return True

@app.post("/registro")
async def registro(request: Request):
    try:
        data = await request.json()
        nombre = data.get("nombre")
        correo = data.get("correo")
        contraseña = data.get("contraseña")
        fecha = obtenerfecha()

        print(nombre, correo, contraseña, fecha)
    except Exception as e:
        print(f"Error al procesar el registro: {e}")
        return JSONResponse(content={"error": "Error al procesar el registro"}, status_code=400)


@app.post("/montar_pdf")
async def montar_pdf(pdf: UploadFile = File(...)):

    try:
        if pdf.content_type != "application/pdf":
            print("El archivo debe ser un PDF")
            return JSONResponse(content={"error": "El archivo debe ser un PDF"}, status_code=400)
        
        contenido = await pdf.read()
        reader = PdfReader(BytesIO(contenido))

        texto = ""
        for page in reader.pages:
            texto += page.extract_text() or ""
        print("PDF recibido con éxito")

        return {"success": True, "nombre": pdf.filename, "contenido": texto}
        

    except Exception as e:
        print(f"Error al montar el PDF: {e}")
        return JSONResponse(content={"error": "Error al montar el PDF"}, status_code=400)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)