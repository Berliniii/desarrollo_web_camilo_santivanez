document.addEventListener('DOMContentLoaded', async function(){
  try{
    const response = await fetch('/get-stats-data');
    const data = await response.json();

    // Gráfico de líneas: Actividades por día
    const ctxLineas = document.getElementById("graficoLineas");
    new Chart(ctxLineas, {
      type: "line",
      data: {
        labels: data.por_dia.labels,
        datasets: [{
          label: "Cantidad de Actividades",
          data: data.por_dia.datos,
          borderColor: "blue",
          fill: false,
          tension: 0.3
        }]
      }
    });

    // Gráfico de torta: Actividades por tipo
    const ctxTorta = document.getElementById("graficoTorta");
    new Chart(ctxTorta, {
      type: "pie",
      data: {
        labels: data.por_tipo.labels,
        datasets: [{
          label: "Actividades por Tipo",
          data: data.por_tipo.datos,
          backgroundColor: [
            "#4BC0C0", "#FF6384", "#FFCE56", "#36A2EB",
            "#FF9F40", "#9966FF", "#C9CBCF", '#2BB673',
            "#B399FF", "#FF7F7F"
          ]
        }]
      }
    });

    // Gráfico de barras: Actividades por horario y mes
    const ctxBarras = document.getElementById("graficoBarras");
    new Chart(ctxBarras, {
      type: "bar",
      data: {
        labels: data.por_horario.labels,
        datasets: [
          {
            label: "Mañana",
            data: data.por_horario.mañana,
            backgroundColor: "#36A2EB"
          },
          {
            label: "Mediodía",
            data: data.por_horario.mediodia,
            backgroundColor: "#FFCE56"
          },
          {
            label: "Tarde",
            data: data.por_horario.tarde,
            backgroundColor: "#FF6384"
          }
        ]
      }
    });
  } catch(error) {
    console.error('Error al cargar las estadísticas')
  }
});  