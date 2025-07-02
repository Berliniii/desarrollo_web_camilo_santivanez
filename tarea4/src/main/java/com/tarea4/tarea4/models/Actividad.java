package com.tarea4.tarea4.models;

import java.time.LocalDateTime;
import jakarta.persistence.*;

@Entity
@Table(name = "actividad", schema = "tarea2")
public class Actividad {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @ManyToOne(optional = false)
    @JoinColumn(
        name = "comuna_id",
        foreignKey = @ForeignKey(name = "fk_actividad_comuna1")
    )
    private Comuna comuna;

    @Column(length = 100)
    private String sector;

    @Column(length = 200, nullable = false)
    private String nombre;

    @Column(length = 100, nullable = false)
    private String email;

    @Column(length = 15)
    private String celular;

    @Column(name = "dia_hora_inicio", nullable = false)
    private LocalDateTime diaHoraInicio;

    @Column(name = "dia_hora_termino")
    private LocalDateTime diaHoraTermino;

    @Column(length = 500)
    private String descripcion;

    public Actividad() {}
    public Actividad(Integer id, Comuna comuna, String sector, String nombre, 
    String email, String celular, LocalDateTime diaHoraInicio, 
    LocalDateTime diaHoraTermino, String descripcion) {
        this.id = id;
        this.comuna = comuna;
        this.sector = sector;
        this.nombre = nombre;
        this.email = email;
        this.celular = celular;
        this.diaHoraInicio = diaHoraInicio;
        this.diaHoraTermino = diaHoraTermino;
        this.descripcion = descripcion;
    }

    public Integer getId() {
        return id;
    }
    public void setId(Integer id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public String getSector() {
        return sector;
    }
    
    public LocalDateTime getDiaHoraInicio() {
        return diaHoraInicio;
    }

    public LocalDateTime getDiaHoraTermino() {
        return diaHoraTermino;
    }

}
