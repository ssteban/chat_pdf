function mostrarRegistro() {
    document.getElementById('loginSection').classList.add('oculto');
    document.getElementById('registroSection').classList.remove('oculto');
}

function mostrarLogin() {
    document.getElementById('registroSection').classList.add('oculto');
    document.getElementById('loginSection').classList.remove('oculto');
}
function registrarUsuario(nombre, correo, contraseña) {
    fetch('http://127.0.0.1:8000/registro', {
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
        alert('Usuario registrado correctamente');
        mostrarLogin()
        
    })
    .catch(error => {
        console.error('Error:', error);
        alert('No se pudo registrar el usuario. Por favor, inténtalo de nuevo.');
    });
}

function procesarUsuario() {
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