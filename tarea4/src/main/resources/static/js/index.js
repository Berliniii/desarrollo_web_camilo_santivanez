document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.evaluar-btn').forEach(btn => {
        btn.addEventListener('click', function () {
            const actividadId = this.getAttribute('data-id');
            let nota = prompt('Ingrese una nota entre 1 y 7:');
            if (nota === null) return; // Cancelado
            nota = parseInt(nota);
            if (isNaN(nota) || nota < 1 || nota > 7) {
                alert('La nota debe ser un número entero entre 1 y 7.');
                return;
            }
            fetch(`/api/actividad/${actividadId}/nota`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ nota: nota })
            })
            .then(res => res.json())
            .then(data => {
                if (data.notaPromedio !== undefined) {
                    // Actualiza la celda de nota en la tabla
                    const tdNota = this.closest('tr').querySelector('td:nth-child(6)');
                    tdNota.textContent = data.notaPromedio.toFixed(2);
                } else if (data.error) {
                    alert(data.error);
                }
            })
            .catch(() => alert('Error al enviar la nota.'));
        });
    });
});