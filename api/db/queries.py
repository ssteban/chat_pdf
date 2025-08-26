from .connection import DatabaseConnection
from ..utils.auth import hash_password, verify_password

def register_user(user, fecha, rol="USER"):
    with DatabaseConnection() as conn:
        cursor = conn.cursor()
        try:
            hashed_password = hash_password(user.contraseña)

            cursor.execute(
                """
                INSERT INTO usuario (nombre_usuario, correo, fecha_creacion, estado)
                VALUES (%s, %s, %s, %s) RETURNING id_usuario
                """,
                (user.nombre, user.correo, fecha, "activo")
            )
            id_usuario = cursor.fetchone()[0]

            cursor.execute(
                """
                INSERT INTO acceso (id_usuario, username, password, rol_usuario)
                VALUES (%s, %s, %s, %s)
                """,
                (id_usuario, user.correo, hashed_password, rol)
            )

            conn.commit()
            print(f"Usuario {user.nombre} registrado con rol {rol} e id {id_usuario}")
            return True

        except Exception as e:
            print(f"Error al registrar usuario: {e}")
            conn.rollback()
            return None
        finally:
            cursor.close()


def login_user(username, password):
    with DatabaseConnection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                SELECT a.id_usuario, a.username, a.password, a.rol_usuario, u.estado, u.nombre_usuario
                FROM acceso a
                JOIN usuario u ON a.id_usuario = u.id_usuario
                WHERE username = %s
                """,
                (username,)
            )
            user_data = cursor.fetchone()
            
            if not verify_password(password, user_data[2]):
                return {"error": "Contraseña incorrecta"}

            return {
                "id_usuario": user_data[0],
                "username": user_data[1],
                "rol_usuario": user_data[3],
                "estado": user_data[4],
                "nombre": user_data[5]
            }

        except Exception as e:
            print(f"Error al iniciar sesión: {e}")
            return {"error": f"Error interno: {e}"}
        finally:
            cursor.close()
