from fastapi import APIRouter, HTTPException, Response
from ..utils.utils_time import obtenerfecha
from ..utils.auth import create_token
from ..utils.cookies import set_cookie, delete_cookie
from pydantic import BaseModel
from ..db.queries import register_user, login_user

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
async def login(user: LoginUser, response: Response):
    try:
        verify = login_user(user.correo, user.contraseña)

        if "error" in verify:
            return {"datos": False, "mensaje": "Credenciales inválidas, Intente de nuevo"}

        token = create_token(verify['username'], verify['rol_usuario'])
        set_cookie(response, token)

        return {
            "datos": True,
            "token": token,
            "nombre": verify['nombre']
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al iniciar sesión: {e}")
    

@router.post("/logout")
async def logout():
    try:
        response = Response()
        delete_cookie(response)
        return {"success": True, "mensaje": "Cierre de sesión exitoso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al cerrar sesion: {e}")