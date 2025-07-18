from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import base64
from io import BytesIO
from PyPDF2 import PdfReader
import uvicorn

app = FastAPI()


app.add_middleware(CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



def cargarInfoDB(usuario, pdf_base, contenido_pdf, nombre_pdf):

    return True


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