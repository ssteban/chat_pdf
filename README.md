# Proyecto Chat PDF

## Descripción General

Este proyecto es una aplicación web que permite a los usuarios cargar un archivo PDF e interactuar con su contenido a través de una interfaz de chat. La aplicación está construida con un backend de FastAPI y un frontend de HTML, CSS y JavaScript puros. Cuenta con autenticación de usuarios, procesamiento de PDF y una funcionalidad de chat impulsada por la API de Google Gemini.

## Características

- **Autenticación de Usuarios**: Sistema seguro de registro e inicio de sesión de usuarios.
- **Seguridad Basada en JWT**: La autenticación se maneja mediante JSON Web Tokens (JWT) almacenados en cookies de tipo `HttpOnly`.
- **Carga de PDF**: Los usuarios pueden subir archivos PDF al servidor.
- **Chat Interactivo**: Una interfaz de chat para hacer preguntas sobre el contenido del PDF cargado.
- **Respuestas Impulsadas por IA**: El backend utiliza la API de Google Gemini para generar respuestas inteligentes basadas en el contenido del PDF.
- **Frontend Adaptable**: La interfaz de usuario está diseñada para ser funcional en diferentes tamaños de pantalla.

## Tecnologías Utilizadas

### Backend
- **Lenguaje**: Python 3
- **Framework**: FastAPI
- **Base de Datos**: PostgreSQL (con el driver `psycopg2`)
- **Autenticación**: `pyjwt` para la generación/validación de tokens, `bcrypt` para el hasheo de contraseñas.
- **IA**: Google Generative AI (`google.generativeai`)
- **Entorno**: `python-dotenv` para la gestión de variables de entorno.

### Frontend
- **Estructura**: HTML5
- **Estilos**: CSS3
- **Lógica**: JavaScript (Vanilla)

## Estructura del Proyecto

```
/
├── api/
│   ├── db/               # Conexión a la base de datos y consultas
│   ├── routes/           # Endpoints de la API (autenticación, usuarios, admin)
│   ├── services/         # Integración con IA (Gemini)
│   ├── utils/            # Ayudantes de autenticación, cookies, etc.
│   └── main.py           # Aplicación principal de FastAPI
├── fron/
│   ├── chat/             # HTML, CSS y JS para la página de chat
│   ├── index.html        # Página de inicio de sesión y registro
│   ├── login_registro.css
│   └── login_registro.js
├── .gitignore
├── requirements.txt
└── README.md
```

## Configuración e Instalación

### Prerrequisitos
- Python 3.10+
- Base de datos PostgreSQL
- Una cuenta de Google AI para obtener la clave de la API de Gemini.

### Configuración del Backend

1.  **Clona el repositorio:**
    ```bash
    git clone <url-del-repositorio>
    cd chat_pdf
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configura la base de datos:**
    - Asegúrate de tener un servidor de PostgreSQL en funcionamiento.
    - Crea una base de datos para el proyecto.
    - Deberás crear las tablas `usuario` y `acceso` manualmente, basándote en las consultas de `api/db/queries.py`.

5.  **Configura las variables de entorno:**
    - Crea un archivo `.env` en el directorio raíz.
    - Añade las siguientes variables, reemplazando los valores de ejemplo:
      ```
      DB_HOST=tu_host_de_db
      DB_USER=tu_usuario_de_db
      DB_PASSWORD=tu_contraseña_de_db
      DB_NAME=tu_nombre_de_db
      SECRET_KEY=tu_clave_secreta_fuerte
      GEMINI_API_KEY=tu_clave_de_api_de_gemini
      ```

6.  **Ejecuta el servidor backend:**
    ```bash
    uvicorn api.main:app --reload
    ```
    La API estará disponible en `http://127.0.0.1:8000`.

### Configuración del Frontend

- No se requiere ningún paso de compilación. Simplemente abre el archivo `fron/index.html` en tu navegador web.
- El frontend está configurado para comunicarse con el backend en `http://127.0.0.1:8000`.

## Endpoints de la API

### Autenticación (`/auth`)
- `POST /auth/register`: Crea un nuevo usuario.
- `POST /auth/login`: Autentica a un usuario y establece una cookie `access_token_cookie`.
- `POST /auth/logout`: Elimina la cookie de autenticación.

### Rutas Protegidas
- `/users/*`: Rutas específicas para usuarios. Requiere un JWT válido.
- `/admin/*`: Rutas específicas para administradores. Requiere un JWT válido con rol de administrador.