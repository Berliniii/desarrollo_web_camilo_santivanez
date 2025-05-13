-- Active: 1747094904497@@127.0.0.1@3306@tarea2

-- Crear la base de datos (si no existe)
CREATE DATABASE IF NOT EXISTS tarea2;

-- Crear el usuario (si no existe)
CREATE USER IF NOT EXISTS 'cc5002'@'localhost' IDENTIFIED BY 'programacionweb';

-- Dar permisos al usuario sobre la base de datos
GRANT ALL PRIVILEGES ON tarea2.* TO 'cc5002'@'localhost';

-- Aplicar los cambios
FLUSH PRIVILEGES;