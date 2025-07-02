package com.tarea4.tarea4.controllers;

import java.util.List;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import com.tarea4.tarea4.services.ApiService;
import com.tarea4.tarea4.dto.ActividadDTO;

@Controller
public class AppController {
    private final ApiService apiService;

    public AppController(ApiService apiService) {
        this.apiService = apiService;
    }

    @GetMapping("/")
    public String indexRoute(Model model) {
        List<ActividadDTO> actividades = apiService.getActividadesRealizadas();
        model.addAttribute("actividades", actividades);
        return "index";
    }
}
