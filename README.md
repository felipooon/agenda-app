# 🧠 Agenda App — Sistema de Gestión para Profesionales

## 📌 Descripción

Este proyecto es una **práctica guiada de desarrollo web**, pero con un enfoque claro:

> 👉 Construir un sistema real, usable y potencialmente vendible.

No es un proyecto académico típico.
Es un **producto en construcción**, pensado para resolver un problema real.

---

# 🎯 Objetivo del proyecto

Desarrollar una aplicación web que permita a un profesional (ej: terapeuta):

* Gestionar su agenda diaria
* Administrar pacientes
* Registrar asistencia
* Controlar pagos
* (Posteriormente) permitir reservas online

---

# 🧠 Enfoque del proyecto

Este proyecto combina:

## 🟢 Práctica técnica

* Aprender Django en contexto real
* Uso de Git en equipo
* Modelado de datos
* Flujo de desarrollo profesional

## 🔵 Producto real

* Uso por una persona real
* Feedback constante
* Iteración basada en uso

---

# 📦 Conceptos clave

## 🚀 MVP (Minimum Viable Product)

Es la versión mínima del sistema que ya entrega valor.

👉 En este proyecto:

* Crear pacientes
* Crear reservas
* Ver agenda diaria

✔ Funcional
✔ Usable
❌ No completo
❌ No perfecto

---

## ☁️ SaaS (Software as a Service)

Modelo donde el sistema:

* Se usa por internet
* Puede tener múltiples usuarios
* Se paga como servicio (mensual)

👉 Este proyecto puede evolucionar a un SaaS

---

# 🧩 Alcance del proyecto

## 🟢 Fase 1 — Panel interno (PRIORIDAD)

Sistema usable por la profesional:

* Gestión de pacientes
* Gestión de reservas
* Agenda diaria
* Registro de asistencia

---

## 🟡 Fase 2 — Gestión avanzada

* Control de pagos
* Historial de pacientes
* Reportes básicos

---

## 🔵 Fase 3 — Parte pública

* Página informativa
* Reserva online de horas
* Integración con agenda

---

# 🏗️ Stack tecnológico

## Backend

* Django

## Frontend

* HTML + Bootstrap (mobile-first)

## Base de datos

* SQLite (desarrollo)
* PostgreSQL (futuro)

## Control de versiones

* Git
* GitHub

---

# 📁 Estructura del proyecto

```bash id="cbb4t4"
agenda_app/
├── config/        # configuración Django
├── agenda/        # reservas
├── pacientes/     # pacientes
├── pagos/         # pagos (futuro)
├── public/        # parte pública (futuro)
├── templates/
├── static/
├── manage.py
```

---

# 🗃️ Modelos principales

## Paciente

* nombre
* teléfono
* email
* notas

## Reserva

* paciente
* fecha
* hora
* estado (reservado / asistió / no asistió)

## Pago (futuro)

* paciente
* monto
* fecha
* estado

---

# 🔐 Autenticación

* Uso del sistema de usuarios de Django
* Acceso restringido al panel interno

---

# 🔄 Flujo principal del sistema

1. Crear paciente
2. Crear reserva
3. Visualizar agenda
4. Marcar asistencia
5. (Opcional) Registrar pago

---

# 🧪 Metodología de desarrollo

## Orden de desarrollo

```text id="u7fltf"
Modelos → Admin → Vistas → Templates → UI
```

---

## Uso del admin de Django

El admin se usa como:

> 🧪 Backend temporal para validar lógica

Permite:

* Crear datos
* Probar relaciones
* Detectar errores temprano

---

# 👥 Trabajo en equipo

## Flujo básico

```bash id="yg3s0y"
git checkout -b feature-nombre
git add .
git commit -m "mensaje claro"
git push origin feature-nombre
```

---

## Reglas

* No trabajar directamente en `main`
* Hacer commits pequeños
* Describir bien los cambios

---

# ⚙️ Instalación

## 1. Clonar repositorio

```bash id="3ofxf5"
git clone https://github.com/TU_USUARIO/agenda-app.git
cd agenda-app
```

---

## 2. Crear entorno virtual

```bash id="4rbv0o"
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Instalar dependencias

```bash id="j7mb1l"
pip install -r requirements.txt
```

---

## 4. Migraciones

```bash id="0yx8sp"
python manage.py migrate
```

---

## 5. Crear usuario admin

```bash id="9l6fxo"
python manage.py createsuperuser
```

---

## 6. Ejecutar servidor

```bash id="l6ckq9"
python manage.py runserver
```

---

# 📱 Diseño UX

Principios:

* Mobile-first
* Uso rápido
* Interfaz simple
* Botones grandes

---

# 📊 Reportes (futuro)

El sistema permitirá generar:

* Ingresos por periodo
* Pacientes atendidos
* Historial de atención
* Métricas de uso

👉 Depende de cómo se estructuren los datos desde el inicio

---

# 🚀 Deploy

Plataforma sugerida:

* Render

---

# ⚠️ Riesgos del proyecto

* Sobreingeniería
* No validar con usuario real
* Enfocarse en diseño antes de funcionalidad

---

# 🎯 Filosofía

```text id="y2rtj2"
Primero funciona
Luego es usable
Después es bonito
```

---

# 📈 Proyección

Este proyecto puede evolucionar a:

* Sistema reutilizable
* Producto SaaS
* Fuente de ingresos

---

# 📌 Estado actual

✔ Setup inicial
✔ Modelos básicos
✔ Admin funcional

---

# 🔥 Próximos pasos

* Crear panel interno (agenda del día)
* Crear vista de pacientes
* Permitir crear reservas fuera del admin

---

# 🤝 Contribución

Proyecto colaborativo.

* Comunicación constante
* Validación continua
* Iteración rápida

---

# 🧠 Nota final

Este proyecto no es solo práctica.

> Es el primer paso para construir software real.

---
