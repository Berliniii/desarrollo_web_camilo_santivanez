package com.tarea4.tarea4.controllers;

import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;

import com.tarea4.tarea4.services.ApiService;
import com.tarea4.tarea4.dto.ActividadDTO;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api")
public class ApiController {
    private final ApiService apiService;
    public ApiController(ApiService apiService) {
        this.apiService = apiService;
    }

    // Devuelve actividades realizadas (DTO)
    @GetMapping("/actividades")
    public List<ActividadDTO> getActividades() {
        return apiService.getActividadesRealizadas();
    }

    // Agrega una nota a una actividad y retorna el nuevo promedio
    @PostMapping("/actividad/{id}/nota")
    public ResponseEntity<Map<String, Object>> agregarNota(
            @PathVariable Integer id,
            @RequestBody Map<String, Integer> body) {
        Integer nota = body.get("nota");
        if (nota == null || nota < 1 || nota > 7) {
            return ResponseEntity.badRequest().body(Map.of("error", "Nota fuera de rango (1-7)"));
        }
        Double nuevoPromedio = apiService.agregarNotaYObtenerPromedio(id, nota);
        if (nuevoPromedio == null) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(Map.of("error", "Actividad no encontrada"));
        }
        return ResponseEntity.ok(Map.of("notaPromedio", nuevoPromedio));
    }
}