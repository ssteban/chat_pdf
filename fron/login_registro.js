function mostrarRegistro() {
    document.getElementById('loginSection').classList.add('oculto');
    document.getElementById('registroSection').classList.remove('oculto');
}

function mostrarLogin() {
    document.getElementById('registroSection').classList.add('oculto');
    document.getElementById('loginSection').classList.remove('oculto');
}