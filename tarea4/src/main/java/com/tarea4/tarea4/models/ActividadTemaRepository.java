package com.tarea4.tarea4.models;

import java.util.List;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ActividadTemaRepository extends JpaRepository<ActividadTema, Integer> {
    List<ActividadTema> findByActividad(Actividad actividad);
}
