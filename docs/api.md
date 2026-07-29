# Documentación de la API

## 1. Descripción

ChickenBot Delivery implementa una API web desarrollada con **FastAPI**, utilizada para administrar el sistema mediante un panel web y dar soporte a la integración con el bot de Telegram.

La aplicación combina el uso de rutas que renderizan vistas HTML mediante **Jinja2** y operaciones de acceso a la base de datos utilizando **SQLAlchemy ORM**.

---

# 2. Tecnologías

| Componente | Tecnología |
|------------|------------|
| Framework Backend | FastAPI |
| Motor de plantillas | Jinja2 |
| ORM | SQLAlchemy |
| Base de datos | PostgreSQL |
| Servidor ASGI | Uvicorn |

---

# 3. Autenticación

El acceso al panel administrativo requiere autenticación mediante sesión.

La autenticación utiliza:

- SessionMiddleware
- Cookies de sesión

Las rutas administrativas verifican que exista una sesión válida antes de permitir el acceso. Si el usuario no está autenticado, es redirigido automáticamente al formulario de inicio de sesión.

---

# 4. Resumen de Endpoints

| Método | Ruta | Descripción |
|---------|------|-------------|
| GET | /login | Mostrar formulario de inicio de sesión |
| POST | /login | Validar credenciales |
| GET | /dashboard | Mostrar panel principal |
| GET | /categories | Listar categorías |
| GET | /categories/new | Formulario de nueva categoría |
| POST | /categories/new | Registrar categoría |
| GET | /categories/{id}/edit | Editar categoría |
| POST | /categories/{id}/edit | Actualizar categoría |
| POST | /categories/{id}/delete | Eliminar categoría |
| GET | /products | Listar productos |
| GET | /products/new | Formulario de nuevo producto |
| POST | /products/new | Registrar producto |
| GET | /products/{id}/edit | Editar producto |
| POST | /products/{id}/edit | Actualizar producto |
| POST | /products/{id}/delete | Eliminar producto |
| GET | /orders | Listar pedidos |
| GET | /orders/{id}/edit | Editar pedido |
| POST | /orders/{id}/edit | Actualizar estado del pedido |
| GET | /deliveries | Listar repartidores |
| GET | /deliveries/new | Formulario de nuevo repartidor |
| POST | /deliveries/new | Registrar repartidor |
| GET | /deliveries/{id}/edit | Editar repartidor |
| POST | /deliveries/{id}/edit | Actualizar repartidor |
| POST | /deliveries/{id}/toggle | Activar o desactivar repartidor |
| GET | /logout | Cerrar sesión |

---

# 5. Descripción de los Endpoints

## Login

### GET /login

Muestra el formulario de autenticación del administrador.

### POST /login

Valida las credenciales ingresadas por el usuario.

**Parámetros**

- username
- password

**Resultado**

- Acceso concedido y redirección al panel administrativo.
- Permanencia en el formulario si las credenciales son incorrectas.

---

## Dashboard

### GET /dashboard

Muestra el panel principal del sistema.

Desde esta vista el administrador puede acceder a todas las funcionalidades disponibles.

---

## Gestión de Categorías

Permite administrar las categorías de los productos.

Operaciones disponibles:

- Crear categoría.
- Consultar categorías.
- Modificar categoría.
- Eliminar categoría.

---

## Gestión de Productos

Permite administrar el catálogo de productos.

Operaciones disponibles:

- Crear producto.
- Consultar productos.
- Modificar producto.
- Eliminar producto.

Durante el registro y edición se valida:

- Precio mayor o igual a cero.
- Stock mayor o igual a cero.

---

## Gestión de Pedidos

Permite visualizar los pedidos realizados por los clientes.

El administrador puede:

- Consultar pedidos.
- Modificar el estado del pedido.
- Realizar el seguimiento del proceso de atención.

---

## Gestión de Repartidores

Permite administrar los repartidores registrados.

Operaciones disponibles:

- Registrar repartidores.
- Editar información.
- Activar o desactivar repartidores.

---

## Logout

### GET /logout

Finaliza la sesión activa del administrador y elimina la información almacenada en la sesión antes de redirigir al formulario de inicio de sesión.

---

# 6. Seguridad

Las rutas administrativas del sistema están protegidas mediante autenticación basada en sesiones.

Antes de ejecutar cualquier operación administrativa, el sistema verifica que exista una sesión válida. En caso contrario, el usuario es redirigido automáticamente al formulario de inicio de sesión.

Además, durante las pruebas funcionales se verificó la protección de las rutas administrativas para impedir el acceso directo mediante URL sin autenticación.

---

# 7. Consideraciones

La API implementada permite administrar las principales entidades del sistema mediante operaciones CRUD y constituye el núcleo del panel administrativo de ChickenBot Delivery.

Su integración con FastAPI, SQLAlchemy y PostgreSQL proporciona una arquitectura modular, organizada y fácil de mantener.