if (localStorage.getItem("usuarioLogueado") !== "true") {
    window.location.href = "../index.html";
}

function toggleDropdown() {
    const menu = document.getElementById("dropdownMenu");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}

function cerrarSesion() {
    localStorage.clear();
    fetch('http://127.0.0.1:8000/auth/logout', {
        method: 'POST',
        credentials: 'include'
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al cerrar la sesión');
        }
        return response.json();
    })
    .then(data => {
        alert(data.mensaje);
        window.location.href = "../index.html";
    })
    .catch(error => {
        console.error('Error:', error);
    });
    
}

// Ocultar el menú si se hace clic fuera
window.addEventListener('click', function (e) {
    const menu = document.getElementById("dropdownMenu");
    const icon = document.querySelector('.user-icon');
    if (!icon.contains(e.target) && !menu.contains(e.target)) {
        menu.style.display = "none";
    }
});

function cargarPdf() {

    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    if (file) {
        // Mostrar el modal de carga
        const modal = document.querySelector('.modalCarga');
        modal.style.display = 'flex';
        if (file.type === 'application/pdf') {
            const formData = new FormData();
            formData.append('pdf', file);

            fetch('http://127.0.0.1:8000/montar_pdf', {
                method: 'POST',
                body: formData
            })
                .then(response => response.json())
                .then(data => {
                    console.log('Éxito:', data);
                    // Ocultar el modal de carga
                    modal.style.display = 'none';
                    alert("PDF cargado exitosamente.");
                })
                .catch((error) => {
                    console.error('Error:', error);
                    modal.style.display = 'none';
                    alert("Error al cargar el PDF.");
                });
        } else {
            modal.style.display = 'none';
            alert("Por favor, selecciona un archivo PDF.");
        }
    } else {
        alert("Por favor, selecciona un archivo.");
    }
}
function cargarMensaje() {

}