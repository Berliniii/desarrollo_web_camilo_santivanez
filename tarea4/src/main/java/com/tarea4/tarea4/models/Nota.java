package com.tarea4.tarea4.models;

import jakarta.persistence.Entity;
import jakarta.persistence.ForeignKey;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotNull;

@Entity
@Table(name="nota", schema = "tarea2")
public class Nota {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @NotNull
    private Integer nota;

    @NotNull
    @ManyToOne(optional=false)
    @JoinColumn(
        name = "actividad_id",
        foreignKey = @ForeignKey(name="fk_nota_actividad1")
    )
    private Actividad actividad;

    public Nota(){}

    public Nota(Integer id, Actividad actividad, Integer nota) {
        this.id = id;
        this.actividad = actividad;
        this.nota = nota;
    }

    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }

    public Integer getNota() { return nota; }
    public void setNota(Integer nota) { this.nota = nota; }

    public Actividad getActividad() { return actividad; }
    public void setActividad(Actividad actividad) { this.actividad = actividad; }

    //Validación
    public static Boolean validateNota(Integer nota){
        return nota >= 1 && nota <= 7;
    }
    
}
