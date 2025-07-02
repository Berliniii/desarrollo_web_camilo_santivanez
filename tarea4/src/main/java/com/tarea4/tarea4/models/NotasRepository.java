package com.tarea4.tarea4.models;

import org.springframework.data.domain.Page;
import java.util.List;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface NotasRepository extends JpaRepository<Nota, Integer> {
    Page<Nota> findAllByOrderByIdDesc(Pageable pageable);
    List<Nota> findByActividad(Actividad actividad);
}
