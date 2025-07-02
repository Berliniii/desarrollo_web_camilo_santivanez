package com.tarea4.tarea4.dto;

import java.time.LocalDateTime;

public class ActividadDTO {
    private Integer id;
    private LocalDateTime diaHoraInicio;
    private String sector;
    private String nombre;
    private String tema;
    private Double notaPromedio;

    public ActividadDTO(Integer id, LocalDateTime diaHoraInicio, String sector, String nombre, String tema, Double notaPromedio) {
        this.id = id;
        this.diaHoraInicio = diaHoraInicio;
        this.sector = sector;
        this.nombre = nombre;
        this.tema = tema;
        this.notaPromedio = notaPromedio;
    }

    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }

    public LocalDateTime getDiaHoraInicio() { return diaHoraInicio; }
    public void setDiaHoraInicio(LocalDateTime diaHoraInicio) { this.diaHoraInicio = diaHoraInicio; }

    public String getSector() { return sector; }
    public void setSector(String sector) { this.sector = sector; }

    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }

    public String getTema() { return tema; }
    public void setTema(String tema) { this.tema = tema; }

    public Double getNotaPromedio() { return notaPromedio; }
    public void setNotaPromedio(Double notaPromedio) { this.notaPromedio = notaPromedio; }
}
