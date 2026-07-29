# Manual Técnico del Sistema

## 1. Introducción

### Objetivo

Este documento describe la instalación, configuración, estructura y despliegue del sistema ChickenBot Delivery.

Está dirigido a desarrolladores y administradores responsables del mantenimiento del proyecto.

---

# 2. Requisitos del sistema

## Software requerido

- Python 3.12 o superior
- PostgreSQL
- Git
- Visual Studio Code (opcional)

## Librerías

Las dependencias del proyecto se encuentran en:

```
requirements.txt
```

Se instalan con:

```bash
pip install -r requirements.txt
```

---

# 3. Instalación

## Clonar el repositorio

```bash
git clone https://github.com/FernandoMF17/chickenbot-delivery.git
cd chickenbot-delivery
```

## Crear un entorno virtual

```bash
python -m venv .venv
```

Activar:

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# 4. Configuración

El proyecto utiliza variables de entorno para almacenar información sensible.

Ejemplo:

```env
DATABASE_URL=postgresql://usuario:password@localhost/chickenbot
BOT_TOKEN=xxxxxxxxxxxxxxxx
SECRET_KEY=xxxxxxxxxxxxxxxx
```

---

# 5. Base de datos

Crear la base de datos en PostgreSQL.

Ejecutar las migraciones:

```bash
alembic upgrade head
```

---

# 6. Estructura del proyecto

```text
app/
├── admin/
├── bot/
├── database/
├── models/
├── routers/
├── services/
├── static/
├── templates/
└── main.py

docs/

alembic/

requirements.txt
```

---

# 7. Ejecución

Iniciar el servidor:

```bash
uvicorn app.main:app --reload
```

La aplicación estará disponible en:

```
http://localhost:8000
```

---

# 8. Despliegue

Para producción se recomienda:

- Ejecutar FastAPI mediante Uvicorn.
- Utilizar PostgreSQL como base de datos.
- Configurar variables de entorno.
- Mantener las migraciones sincronizadas mediante Alembic.

---

# 9. Arquitectura

El sistema está compuesto por tres módulos principales:

- Bot de Telegram
- Panel administrativo
- Base de datos PostgreSQL

Flujo general:

```text
Usuario
   │
Telegram
   │
Bot
   │
FastAPI
   │
SQLAlchemy
   │
PostgreSQL
```

---

# 10. Mantenimiento

Las tareas de mantenimiento incluyen:

- Aplicar nuevas migraciones.
- Actualizar dependencias.
- Revisar registros de errores.
- Realizar copias de seguridad de la base de datos.

---

# 11. Conclusión

El manual técnico proporciona la información necesaria para instalar, configurar, ejecutar y mantener ChickenBot Delivery, facilitando futuras actualizaciones y el trabajo colaborativo.