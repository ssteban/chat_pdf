from .connection import DatabaseConnection
from ..utils.auth import hash_password

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
                (id_usuario, user.nombre, hashed_password, rol)
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
