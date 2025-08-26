function mostrarRegistro() {
    document.getElementById('loginSection').classList.add('oculto');
    document.getElementById('registroSection').classList.remove('oculto');
    document.getElementById('nombre').value = "";
    document.getElementById('correo').value = "";
    document.getElementById('contraseña').value = "";
}

function mostrarLogin() {
    document.getElementById('registroSection').classList.add('oculto');
    document.getElementById('loginSection').classList.remove('oculto');
    document.getElementById("correoInicio").value = "";
    document.getElementById("contraseñaInicio").value = "";
}
function registrarUsuario(nombre, correo, contraseña) {
    fetch('http://127.0.0.1:8000/auth/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nombre, correo, contraseña })
    })
    .then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            throw new Error('Error en el registro del usuario');
        }
    })
    .then(data => {
        alert(`${data.mensaje}\nBienvenido: ${data.nombre}`);
        mostrarLogin()
        
    })
    .catch(error => {
        console.error('Error:', error);
        alert('No se pudo registrar el usuario. Por favor, inténtalo de nuevo.');
    });
}

function procesarUsuarioRegistrar() {
    const nombre = document.getElementById('nombre').value;
    const email = document.getElementById('correo').value;
    const password = document.getElementById('contraseña').value;

    if (!nombre || !email || !password) {
        alert('Por favor, completa todos los campos.');
        return false;
    }
    else{
        registrarUsuario(nombre, email, password);
    }
}

function iniciarSesion(correo, contraseña){
    fetch('http://127.0.0.1:8000/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({correo, contraseña }),
        credentials: 'include'
    })
    .then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            throw new Error('Error en el inicio de sesion');
        }
    })
    .then(data => {
        if(data.datos){
            alert("Bienvenido: "+data.nombre);
            localStorage.setItem("usuarioLogueado", "true");
            window.location.href = "chat/chat.html";
        }else{
            alert(data.mensaje);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('No se pudo iniciar sesion. Por favor, inténtalo de nuevo.');
    });
}

function procesarUsuarioIniciar(){
    const correo = document.getElementById("correoInicio").value;
    const contraseña = document.getElementById("contraseñaInicio").value;

    if (!correo || !contraseña){
        alert("Por favor Ingrese Usuario y contraseña.")
        return false;
    }else{
        iniciarSesion(correo, contraseña)
    }

}