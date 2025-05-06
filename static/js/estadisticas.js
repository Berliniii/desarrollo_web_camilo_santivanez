// Gráfico de líneas: Actividades por día
const ctxLineas = document.getElementById("graficoLineas");
new Chart(ctxLineas, {
  type: "line",
  data: {
    labels: ["7 Abr", "8 Abr", "9 Abr", "10 Abr", "11 Abr"],
    datasets: [{
      label: "Cantidad de Actividades",
      data: [3, 5, 2, 4, 1],
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
    labels: ["Reciclaje", "Charlas", "Deporte", "Voluntariado"],
    datasets: [{
      label: "Actividades por Tipo",
      data: [4, 3, 2, 1],
      backgroundColor: ["#4BC0C0", "#FF6384", "#FFCE56", "#36A2EB"]
    }]
  }
});

// Gráfico de barras: Actividades por horario y mes
const ctxBarras = document.getElementById("graficoBarras");
new Chart(ctxBarras, {
  type: "bar",
  data: {
    labels: ["Enero", "Febrero", "Marzo", "Abril"],
    datasets: [
      {
        label: "Mañana",
        data: [2, 3, 1, 4],
        backgroundColor: "#36A2EB"
      },
      {
        label: "Mediodía",
        data: [1, 2, 2, 1],
        backgroundColor: "#FFCE56"
      },
      {
        label: "Tarde",
        data: [2, 1, 3, 2],
        backgroundColor: "#FF6384"
      }
    ]
  }
});