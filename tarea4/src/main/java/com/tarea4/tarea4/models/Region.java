package com.tarea4.tarea4.models;

import jakarta.persistence.*;

@Entity
@Table(name = "region", schema = "tarea2")
public class Region {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(length = 200, nullable = false)
    private String nombre;

    public Region() {}

    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }

    public String getNombre() { return nombre; }
}
