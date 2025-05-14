document.addEventListener('DOMContentLoaded', function() {
    const regionSelect = document.getElementById("select-region");
    const comunaSelect = document.getElementById("select-comuna");

    regionSelect.addEventListener("change", function() {
        const regionId = this.value;
        comunaSelect.innerHTML = '<option value="">Seleccione una Comuna</option>';
        if (regionId) {
            fetch(`/api/comunas/${regionId}`)
                .then(response => response.json())
                .then(comunas => {
                    comunas.forEach(comuna => {
                        const option = document.createElement("option");
                        option.value = comuna.id;
                        option.textContent = comuna.nombre;
                        comunaSelect.appendChild(option);
                    });
                });
        }
    });
});


