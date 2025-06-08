document.addEventListener('DOMContentLoaded', function() {
    const detalle = document.getElementById('detalle');
    const detalleLista = document.getElementById('detalle-lista');
    const tabla = document.getElementById('tabla');
    let actividadActualID = null

    function mostrarDetalle(index) {
        const actividad = window.actividadesData[parseInt(index)];
        actividadActualID = actividad.id;
        detalleLista.innerHTML = `
            <li><strong>Inicio:</strong> ${actividad.inicio}</li>
            <li><strong>Término:</strong> ${actividad.termino}</li>
            <li><strong>Comuna:</strong> ${actividad.comuna}</li>
            <li><strong>Sector:</strong> ${actividad.sector}</li>
            <li><strong>Tema:</strong> ${actividad.tema}</li>
            <li><strong>Nombre del Organizador:</strong> ${actividad.organizador}</li>
            <li><strong>Total de Fotos:</strong> ${actividad.fotos}</li>
        `;
        // Cargar comentarios de forma asíncrona
        cargarComentarios(actividad.id);    

        tabla.style.display = "none";
        detalle.style.display = "block";
    }

    async function cargarComentarios(actividadId) {
    try {
        const response = await fetch(`/comentarios/${actividadId}`);
        const comentarios = await response.json();
        
        const listaComentarios = document.getElementById('lista-comentarios');
        if (comentarios.length > 0) {
            listaComentarios.innerHTML = comentarios.map(c => `
                <div class="comentario">
                    <p class="comentario-meta">
                        <strong>${c.nombre}</strong> - 
                        <span class="fecha">${new Date(c.fecha).toLocaleString()}</span>
                    </p>
                    <p class="comentario-texto">${c.texto}</p>
                </div>
            `).join('');
        } else {
            listaComentarios.innerHTML = '<p>No hay comentarios para esta actividad.</p>';
        }
    } catch (error) {
        console.error('Error al cargar comentarios:', error);
        document.getElementById('lista-comentarios').innerHTML = 
            '<p class="error">Error al cargar los comentarios</p>';
    }
}

    function mostrarError(mensaje) {
        mensajeError.textContent = mensaje;
        mensajeError.style.display = 'block';
        // Ocultar el mensaje después de 3 segundos
        setTimeout(() => {
            mensajeError.style.display = 'none';
        }, 3000);
    }

    function volverListado() {
        detalle.style.display = "none";
        tabla.style.display = "table";
        actividadActualID = null
    }

    //Logica para manejar el envio del Comentario
    const comentarioForm = document.getElementById('comentario-form');
    const mensajeError = document.getElementById('mensaje-error');
    comentarioForm.addEventListener('submit', async function(e){
        e.preventDefault();
        mensajeError.style.display = 'none';

        const nombre = document.getElementById('nombre').value;
        const texto = document.getElementById('texto').value;

        // Validaciones
        if (nombre.length < 3 || nombre.length > 80) {
            mostrarError('El nombre debe tener entre 3 y 80 caracteres');
            return;
        }

        if (texto.length < 5) {
            mostrarError('El comentario debe tener al menos 5 caracteres');
            return;
        }

        const formData = {
            nombre: document.getElementById('nombre').value,
            texto: document.getElementById('texto').value,
            actividad_id: actividadActualID
        };
        
        try{
            const response = await fetch('/agregar_comentario',{
                method: "POST",
                body: JSON.stringify(formData),
                credentials: "include",
                cache: "no-cache",
                headers: {
                    "Content-Type": "application/json",
                },
            });
            if(!response.ok){
                throw new Error("Network response was not ok");
            }
            comentarioForm.reset();
            mostrarError('Comentario agregado exitosamente');
            mensajeError.style.backgroundColor = '#d4edda';
            mensajeError.style.color = '#155724';
            mensajeError.style.borderColor = '#c3e6cb';          
        }
        catch(error){
            console.error("There has been a problem with your fecth operation");
            error
        };
    })

    // Exponer la función mostrarDetalle globalmente
    window.mostrarDetalle = mostrarDetalle;
    window.volverListado = volverListado;
});
  