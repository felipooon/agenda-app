# 📅 Agenda App

Sistema web de gestión de agenda y pacientes desarrollado con Django.

---

# 🚀 Descripción

Aplicación web para administrar:

- Pacientes
- Reservas de horas
- Agenda diaria y semanal
- Asistencia de citas
- Reportes básicos

Diseñada como un MVP funcional con base sólida para escalar a un sistema tipo agenda clínica.

---

# 🧠 Arquitectura

- **Framework:** Django 5.x
- **Backend:** Python
- **Base de datos:** SQLite (desarrollo)
- **Frontend:** HTML + CSS + JavaScript vanilla
- **Patrón:** MVT (Model - View - Template)

Estructura del proyecto:
config/        → configuración del proyecto agenda/        → gestión de agenda y reservas pacientes/     → gestión de pacientes templates/     → vistas HTML static/        → CSS y JS reutilizable

---

# ⚙️ Funcionalidades actuales

## 📅 Agenda
- Vista diaria de reservas
- Vista semanal por bloques horarios
- Creación de reservas
- Validación de solapamiento de horarios
- Marcado de asistencia (asistió / no asistió)
- Navegación entre días y semanas

---

## 👥 Pacientes
- Creación de pacientes
- Listado general
- Búsqueda con autocomplete
- Datos: nombre, apellido, teléfono, email, notas, fecha de nacimiento

---

## 📊 Reportes
- Total de pacientes
- Total de reservas
- Asistencias
- No asistencias

---

# 🌐 Endpoints principales
/agenda/                 → vista diaria /semana/                 → vista semanal /reserva/nueva/          → crear reserva /pacientes/              → listado de pacientes /pacientes/nuevo/        → crear paciente /buscar-pacientes/       → API autocomplete /reportes/               → reportes generales

---

# 🎨 UI / UX

- Diseño mobile-first
- Layout tipo aplicación móvil
- Cards para información
- Vista semanal en formato grilla
- Autocomplete en formularios
- Navegación superior + navegación móvil

---

# 🧩 Estado actual del sistema

✔ MVP funcional  
✔ Agenda diaria operativa  
✔ Vista semanal implementada  
✔ Autocomplete funcional  
✔ Código modularizado (base.html + static files)  
✔ Navegación en evolución  

---

# ⚠️ Limitaciones actuales

- Base de datos SQLite (no persistente en producción)
- Autenticación básica/incompleta
- Sin edición/eliminación completa en todos los módulos
- Sin drag & drop en agenda semanal
- UI en proceso de refinamiento

---

# 🛣️ Próximos pasos

- Migración a PostgreSQL
- Drag & drop en vista semanal
- Reservas con duración dinámica
- Mejora de navegación (sidebar / bottom nav responsive)
- Sistema de usuarios y permisos
- Mejoras UI tipo dashboard profesional

---

# 📌 Notas

Proyecto en desarrollo activo orientado a sistema de gestión de agenda clínica escalable.