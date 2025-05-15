document.addEventListener('DOMContentLoaded', function() {
    const detalle = document.getElementById('detalle');
    const detalleLista = document.getElementById('detalle-lista');
    const tabla = document.getElementById('tabla');

    function mostrarDetalle(index) {
        const actividad = window.actividadesData[parseInt(index)];
        detalleLista.innerHTML = `
            <li><strong>Inicio:</strong> ${actividad.inicio}</li>
            <li><strong>Término:</strong> ${actividad.termino}</li>
            <li><strong>Comuna:</strong> ${actividad.comuna}</li>
            <li><strong>Sector:</strong> ${actividad.sector}</li>
            <li><strong>Tema:</strong> ${actividad.tema}</li>
            <li><strong>Nombre del Organizador:</strong> ${actividad.organizador}</li>
            <li><strong>Total de Fotos:</strong> ${actividad.fotos}</li>
        `;
        tabla.style.display = "none";
        detalle.style.display = "block";
    }

    function volverListado() {
        detalle.style.display = "none";
        tabla.style.display = "table";
    }

    // Exponer la función mostrarDetalle globalmente
    window.mostrarDetalle = mostrarDetalle;
    window.volverListado = volverListado;
});
  