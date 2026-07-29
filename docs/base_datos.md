# Base de Datos

## 1. Descripción

ChickenBot Delivery utiliza una base de datos relacional **PostgreSQL** para almacenar la información de usuarios, productos, pedidos, categorías y repartidores.

La persistencia de datos se implementó mediante **SQLAlchemy ORM**, permitiendo representar las tablas como modelos de Python y facilitando las operaciones CRUD. La evolución del esquema de la base de datos se administra mediante **Alembic**, lo que permite mantener un historial de migraciones controlado.

---

# 2. Tecnologías

| Componente | Tecnología |
|------------|------------|
| Sistema Gestor de Base de Datos | PostgreSQL |
| ORM | SQLAlchemy |
| Migraciones | Alembic |

---

# 3. Modelo de Datos

La base de datos está compuesta por las siguientes entidades principales:

- User
- Category
- Product
- Order
- OrderDetail
- Delivery

---

# 4. Diagrama simplificado de relaciones

```text
User
 │
 │ 1:N
 ▼
Order
 │
 │ 1:N
 ▼
OrderDetail
 ▲
 │
 │ N:1
Product
 ▲
 │
 │ N:1
Category

Delivery
   │
   └── Gestiona la entrega de los pedidos
```

---

# 5. Descripción de las tablas

## 5.1 User

Almacena la información de los clientes registrados mediante el bot de Telegram.

### Campos principales

| Campo | Tipo | Descripción |
|--------|------|-------------|
| id | Integer | Identificador del usuario |
| username | String | Nombre de usuario de Telegram |
| full_name | String | Nombre completo del cliente |

### Relaciones

- Un usuario puede realizar múltiples pedidos.

---

## 5.2 Category

Agrupa los productos disponibles dentro del sistema.

### Campos principales

| Campo | Tipo |
|--------|------|
| id | Integer |
| name | String |

### Relaciones

- Una categoría contiene múltiples productos.

---

## 5.3 Product

Representa cada producto disponible para la venta.

### Campos principales

| Campo | Tipo |
|--------|------|
| id | Integer |
| name | String |
| description | String |
| price | Float |
| stock | Integer |
| category_id | Integer |

### Relaciones

- Pertenece a una categoría.
- Puede estar asociado a múltiples pedidos mediante la tabla **OrderDetail**.

---

## 5.4 Order

Representa un pedido realizado por un cliente.

### Campos principales

| Campo | Tipo |
|--------|------|
| id | Integer |
| status | String |
| created_at | DateTime |
| updated_at | DateTime |
| user_id | Integer |
| delivery_latitude | Float |
| delivery_longitude | Float |
| delivery_photo | String |

### Relaciones

- Pertenece a un usuario.
- Contiene uno o varios registros en **OrderDetail**.

### Estados del pedido

Los pedidos pueden pasar por los siguientes estados:

- Pendiente
- Pagado
- En camino
- Entregado

---

## 5.5 OrderDetail

Almacena el detalle de los productos incluidos en cada pedido.

### Campos principales

| Campo | Tipo |
|--------|------|
| id | Integer |
| quantity | Integer |
| subtotal | Float |
| order_id | Integer |
| product_id | Integer |

### Relaciones

- Pertenece a un pedido.
- Hace referencia a un producto.

Esta tabla permite que un mismo pedido contenga varios productos con cantidades diferentes.

---

## 5.6 Delivery

Almacena la información de los repartidores registrados.

### Campos principales

| Campo | Tipo |
|--------|------|
| id | Integer |
| full_name | String |
| telegram_username | String |
| access_code | String |
| is_active | Boolean |

### Función

Los repartidores registrados pueden ser activados o desactivados desde el panel administrativo para participar en el proceso de entrega.

---

# 6. Relaciones entre entidades

Las relaciones implementadas en el sistema son:

- Un usuario puede realizar muchos pedidos.
- Un pedido pertenece a un único usuario.
- Una categoría agrupa múltiples productos.
- Un producto pertenece a una categoría.
- Un pedido puede contener varios productos mediante **OrderDetail**.
- Cada detalle corresponde a un único producto.
- Los repartidores participan en el proceso de entrega de los pedidos.

---

# 7. Persistencia de datos

El acceso a la base de datos se realiza mediante sesiones de SQLAlchemy obtenidas con `Depends(get_db)`.

Todas las operaciones de creación, consulta, actualización y eliminación utilizan el ORM, reduciendo la necesidad de escribir consultas SQL manuales y facilitando el mantenimiento del código.

---

# 8. Migraciones

Las modificaciones del esquema de la base de datos son administradas mediante Alembic.

Durante el desarrollo del proyecto se realizaron migraciones para:

- Crear las tablas principales.
- Incorporar el campo `delivery_photo` para almacenar la evidencia de entrega.
- Agregar el campo `updated_at` para registrar la última modificación de un pedido.

---

# 9. Integridad de los datos

La consistencia de la información se garantiza mediante:

- Llaves primarias.
- Llaves foráneas.
- Relaciones entre modelos.
- Restricciones de nulidad (`nullable`).
- SQLAlchemy ORM.

Estas características permiten mantener la integridad referencial y asegurar que la información almacenada sea consistente durante la operación del sistema.

---

# 10. Conclusión

La estructura de la base de datos fue diseñada para soportar el funcionamiento integrado del bot de Telegram y del panel administrativo, permitiendo gestionar de forma organizada la información de usuarios, productos, pedidos y repartidores mediante un modelo relacional implementado en PostgreSQL.