# Arquitectura del Sistema

## 1. Descripción general

ChickenBot Delivery es un sistema para la gestión de pedidos de un restaurante, compuesto por dos aplicaciones integradas:

- Un bot de Telegram para clientes y repartidores.
- Un panel de administración web desarrollado con FastAPI.

Ambos componentes comparten una única base de datos PostgreSQL, garantizando la sincronización de la información en tiempo real.

---

# 2. Arquitectura general

```text
                    +----------------------+
                    |      Cliente         |
                    |      Telegram        |
                    +----------+-----------+
                               |
                               |
                      Telegram Bot API
                               |
                               |
                  +------------v-------------+
                  | Bot de Telegram          |
                  | python-telegram-bot      |
                  +------------+-------------+
                               |
                               |
                               |
                  +------------v-------------+
                  | FastAPI                  |
                  | Backend del sistema      |
                  +------+-----------+-------+
                         |           |
                         |           |
          +--------------+           +----------------+
          |                                   |
          |                                   |
+---------v---------+              +----------v---------+
| Panel Web         |              | SQLAlchemy ORM     |
| Jinja2 + Bootstrap|              +----------+---------+
+-------------------+                         |
                                              |
                                     +--------v--------+
                                     | PostgreSQL      |
                                     | Base de Datos   |
                                     +-----------------+
```

---

# 3. Componentes del sistema

## 3.1 Bot de Telegram

El bot constituye la interfaz principal para clientes y repartidores.

Funciones principales:

- Mostrar el menú.
- Registrar pedidos.
- Administrar el carrito.
- Solicitar la ubicación.
- Notificar cambios de estado.
- Gestionar el flujo de entrega por parte del repartidor.

Tecnología utilizada:

- python-telegram-bot

---

## 3.2 Backend

El backend fue desarrollado utilizando FastAPI.

Se encarga de:

- Procesar solicitudes del panel.
- Gestionar la autenticación del administrador.
- Administrar productos.
- Administrar categorías.
- Administrar repartidores.
- Administrar pedidos.
- Comunicarse con la base de datos.

Tecnologías utilizadas:

- FastAPI
- Starlette
- SQLAlchemy

---

## 3.3 Panel Administrativo

El panel web permite administrar completamente el sistema.

Incluye:

- Inicio de sesión.
- Dashboard.
- Gestión de categorías.
- Gestión de productos.
- Gestión de pedidos.
- Gestión de repartidores.

Tecnologías:

- Jinja2
- Bootstrap 5

---

## 3.4 Base de Datos

Toda la información del sistema se almacena en PostgreSQL.

La persistencia es realizada mediante SQLAlchemy ORM.

La base de datos almacena:

- Usuarios
- Categorías
- Productos
- Pedidos
- Detalles del pedido
- Repartidores

---

# 4. Flujo de funcionamiento

El funcionamiento general del sistema es el siguiente:

1. El cliente inicia una conversación con el bot.
2. El bot consulta los productos disponibles.
3. El cliente arma su pedido.
4. Se registra la ubicación.
5. El administrador asigna un repartidor.
6. El repartidor recibe el pedido.
7.  El repartidor inicia la entrega.
8.  El repartidor confirma la entrega mediante una fotografía.
9.  El pedido cambia al estado **Entregado**.

---

# 5. Tecnologías utilizadas

| Tecnología | Uso |
|------------|-----|
| Python 3 | Lenguaje de programación |
| FastAPI | Backend |
| PostgreSQL | Base de datos |
| SQLAlchemy | ORM |
| Alembic | Migraciones |
| Jinja2 | Plantillas HTML |
| Bootstrap 5 | Interfaz gráfica |
| python-telegram-bot | Bot de Telegram |
| Uvicorn | Servidor ASGI |

---

# 6. Ventajas de la arquitectura

La arquitectura implementada presenta las siguientes ventajas:

- Separación entre bot, panel web y base de datos.
- Fácil mantenimiento del código.
- Escalabilidad para incorporar nuevas funcionalidades.
- Persistencia centralizada de la información.
- Integración entre el bot de Telegram y el panel administrativo.