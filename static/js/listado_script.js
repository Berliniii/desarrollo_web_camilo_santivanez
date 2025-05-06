const actividades = [
    {
      inicio: "2025-04-01 10:30",
      termino: "2025-04-01 13:00",
      comuna: "Santiago",
      sector: "Centro",
      tema: "Reciclaje Comunitario",
      organizador: "Fundación Verde",
      fotos: 3
    },
    {
      inicio: "2025-03-20 09:00",
      termino: "2025-03-20 11:30",
      comuna: "La Florida",
      sector: "Sur",
      tema: "Charlas de Salud Mental",
      organizador: "Municipalidad de La Florida",
      fotos: 5
    },
    {
      inicio: "2025-02-10 15:00",
      termino: "2025-02-10 17:00",
      comuna: "Providencia",
      sector: "Norte",
      tema: "Talleres de Compostaje",
      organizador: "EcoVida",
      fotos: 2
    },
    {
      inicio: "2025-04-04 08:00",
      termino: "2025-04-04 12:00",
      comuna: "Ñuñoa",
      sector: "Oriente",
      tema: "Capacitación en Energía Solar",
      organizador: "Soluciones Sustentables",
      fotos: 4
    },
    {
      inicio: "2025-03-15 14:30",
      termino: "2025-03-15 16:30",
      comuna: "Maipú",
      sector: "Poniente",
      tema: "Huertas Urbanas",
      organizador: "Red Agroecológica",
      fotos: 1
    }
  ];
  
  const cuerpoTabla = document.getElementById('cuerpo-tabla');
  const detalle = document.getElementById('detalle');
  const detalleLista = document.getElementById('detalle-lista');
  const tabla = document.getElementById('tabla');
  
  // Llenar tabla
  actividades.forEach((actividad, index) => {
    const fila = document.createElement('tr');
    fila.innerHTML = `
      <td>${actividad.inicio}</td>
      <td>${actividad.termino}</td>
      <td>${actividad.comuna}</td>
      <td>${actividad.sector}</td>
      <td>${actividad.tema}</td>
      <td>${actividad.organizador}</td>
      <td>${actividad.fotos}</td>
    `;
    fila.onclick = () => mostrarDetalle(index);
    cuerpoTabla.appendChild(fila);
  });
  
  function mostrarDetalle(index) {
    const act = actividades[index];
    detalleLista.innerHTML = `
      <li><strong>Inicio:</strong> ${act.inicio}</li>
      <li><strong>Término:</strong> ${act.termino}</li>
      <li><strong>Comuna:</strong> ${act.comuna}</li>
      <li><strong>Sector:</strong> ${act.sector}</li>
      <li><strong>Tema:</strong> ${act.tema}</li>
      <li><strong>Nombre del Organizador:</strong> ${act.organizador}</li>
      <li><strong>Total de Fotos:</strong> ${act.fotos}</li>
    `;
    tabla.style.display = "none";
    detalle.style.display = "block";
  }
  
  function volverListado() {
    detalle.style.display = "none";
    tabla.style.display = "table";
  }
  