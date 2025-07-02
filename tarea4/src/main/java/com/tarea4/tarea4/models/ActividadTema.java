package com.tarea4.tarea4.models;

import jakarta.persistence.*;

@Entity
@Table(name = "actividad_tema", schema = "tarea2")
public class ActividadTema {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Enumerated(EnumType.STRING)
    @Column(length = 20, nullable = false)
    private Tema tema;

    @Column(name = "glosa_otro", length = 15)
    private String glosaOtro;

    @ManyToOne(optional = false)
    @JoinColumn(
        name = "actividad_id",
        foreignKey = @ForeignKey(name = "fk_actividad_tema_actividad1")
    )
    private Actividad actividad;

    public ActividadTema() {}

    public enum Tema {
        música, deporte, ciencias, religión, política, tecnología, juegos, baile, comida, otro
    }

    // Getters y setters omitidos por brevedad
    public Integer getId() {
        return id;
    }
    public void setId(Integer id) {
        this.id = id;
    }
    public Tema getTema() {
        return tema;
    }
    public void setTema(Tema tema) {
        this.tema = tema;
    }
    public String getGlosaOtro() {
        return glosaOtro;
    }   
}