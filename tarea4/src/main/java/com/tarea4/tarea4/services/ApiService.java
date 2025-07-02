package com.tarea4.tarea4.services;

import java.time.LocalDateTime;
import java.util.Optional;
import java.util.List;
import java.util.stream.Collectors;

import org.springframework.stereotype.Service;

import com.tarea4.tarea4.models.Actividad;
import com.tarea4.tarea4.models.ActividadTema;
import com.tarea4.tarea4.models.Nota;
import com.tarea4.tarea4.models.NotasRepository;
import com.tarea4.tarea4.dto.ActividadDTO;
import com.tarea4.tarea4.models.ActividadRepository;
import com.tarea4.tarea4.models.ActividadTemaRepository;

@Service
public class ApiService {
    private final NotasRepository notasRepository;
    private final ActividadRepository actividadRepository;
    private final ActividadTemaRepository actividadTemaRepository;

    public ApiService(
        NotasRepository notasRepository,
        ActividadRepository actividadRepository,
        ActividadTemaRepository actividadTemaRepository
    ) {
        this.notasRepository = notasRepository;
        this.actividadRepository = actividadRepository;
        this.actividadTemaRepository = actividadTemaRepository;
    }

    // Devuelve actividades realizadas (terminadas), con tema y promedio de notas
    public List<ActividadDTO> getActividadesRealizadas() {
    LocalDateTime ahora = LocalDateTime.now();
    List<Actividad> actividades = actividadRepository.findByDiaHoraTerminoBefore(ahora);

    return actividades.stream().map(actividad -> {
        // Buscar todos los temas asociados
        List<ActividadTema> temas = actividadTemaRepository.findByActividad(actividad);
        String tema = temas.isEmpty()
            ? "-"
            : temas.stream()
                   .map(t -> t.getTema().name())
                   .reduce((a, b) -> a + ", " + b)
                   .orElse("-");
        // Calcular promedio de notas
        List<Nota> notas = notasRepository.findByActividad(actividad);
        Double promedio = notas.isEmpty() ? null :
            notas.stream().mapToInt(Nota::getNota).average().orElse(0.0);

        return new ActividadDTO(
            actividad.getId(),
            actividad.getDiaHoraInicio(),
            actividad.getSector(),
            actividad.getNombre(),
            tema,
            promedio
        );
    }).collect(Collectors.toList());
    }

    public Double agregarNotaYObtenerPromedio(Integer actividadId, Integer notaValor) {
    Optional<Actividad> actividadOpt = actividadRepository.findById(actividadId);
    if (actividadOpt.isEmpty()) {
        return null;
    }
    Actividad actividad = actividadOpt.get();
    if (notaValor < 1 || notaValor > 7) {
        return null;
    }
    Nota nota = new Nota();
    nota.setActividad(actividad);
    nota.setNota(notaValor);
    notasRepository.save(nota);

    List<Nota> notas = notasRepository.findByActividad(actividad);
    return notas.stream().mapToInt(Nota::getNota).average().orElse(0.0);
    }
}