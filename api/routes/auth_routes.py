from fastapi import APIRouter, HTTPException
from ..utils.utils_time import obtenerfecha
from pydantic import BaseModel
from ..db.queries import register_user

router = APIRouter()

class RegisterUser(BaseModel):
    nombre: str
    correo: str
    contraseña: str

class LoginUser(BaseModel):
    correo: str
    contraseña: str

@router.post("/register")
async def register(user: RegisterUser):
    try:
        fecha = obtenerfecha()
        creado = register_user(user, fecha)

        if not creado:
            raise HTTPException(status_code=400, detail="No se pudo registrar el usuario")

        return {
            "success": True,
            "mensaje": "Usuario registrado exitosamente",
            "nombre": user.nombre,
            "correo": user.correo,
            "fecha_registro": fecha
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al registrar usuario: {e}")


@router.post("/login")
async def login(user: LoginUser):
    try:

        return {
            "datos": True,
            "nombre": "Fidel Sanchez",
            "correo": user.correo
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al iniciar sesión: {e}")