# Bitácora de Decisiones Técnicas

## Proyecto

ChickenBot Delivery

---

# Objetivo

Este documento registra las principales decisiones técnicas tomadas durante el desarrollo del proyecto, indicando el motivo de cada elección y las alternativas consideradas.

---

# Decisión 1

## Framework Backend

### Decisión

Utilizar FastAPI como framework principal.

### Alternativas

- Flask
- Django

### Justificación

FastAPI ofrece un alto rendimiento, tipado mediante Pydantic, integración sencilla con SQLAlchemy y una estructura adecuada para aplicaciones REST.

---

# Decisión 2

## Base de datos

### Decisión

Utilizar PostgreSQL.

### Alternativas

- SQLite
- MySQL

### Justificación

PostgreSQL ofrece mayor robustez, soporte para múltiples conexiones y es apropiado para aplicaciones que requieren persistencia confiable.

---

# Decisión 3

## ORM

### Decisión

Utilizar SQLAlchemy.

### Alternativas

- Consultas SQL manuales

### Justificación

SQLAlchemy facilita el mantenimiento del código y permite trabajar mediante modelos orientados a objetos.

---

# Decisión 4

## Migraciones

### Decisión

Utilizar Alembic.

### Alternativas

- Crear tablas manualmente

### Justificación

Permite controlar la evolución del esquema de la base de datos mediante migraciones versionadas.

---

# Decisión 5

## Bot conversacional

### Decisión

Utilizar python-telegram-bot.

### Alternativas

- TeleBot
- Pyrogram

### Justificación

La librería posee buena documentación, integración con Telegram Bot API y soporte para conversaciones mediante handlers.

---

# Decisión 6

## Panel Administrativo

### Decisión

Implementar el panel utilizando FastAPI + Jinja2 + Bootstrap.

### Alternativas

- React
- Vue

### Justificación

Se buscó mantener una arquitectura sencilla utilizando renderizado del lado del servidor.

Bootstrap permitió mejorar rápidamente la interfaz del sistema.

---

# Decisión 7

## Gestión de autenticación

### Decisión

Implementar autenticación mediante sesiones utilizando SessionMiddleware.

### Justificación

Permite restringir el acceso al panel administrativo sin incorporar dependencias adicionales.

---

# Decisión 8

## Gestión de pedidos

### Decisión

Separar los pedidos de sus productos mediante la entidad OrderDetail.

### Justificación

Permite que un pedido contenga múltiples productos y cantidades diferentes.

---

# Decisión 9

## Confirmación de entrega

### Decisión

Solicitar una fotografía al repartidor como evidencia de entrega.

### Justificación

Permite verificar visualmente la entrega del pedido y registrar la evidencia dentro de la base de datos mediante el campo `delivery_photo`.

---

# Decisión 10

## Diseño del panel

### Decisión

Actualizar la interfaz utilizando Bootstrap 5.

### Justificación

Se buscó mejorar la experiencia de usuario mediante tablas responsivas, botones, tarjetas, iconografía y estilos modernos.

---

# Conclusión

Las decisiones técnicas adoptadas durante el desarrollo buscaron mantener una arquitectura sencilla, modular y fácil de mantener, garantizando la integración entre el bot de Telegram, el panel administrativo y la base de datos PostgreSQL.