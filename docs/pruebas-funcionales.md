# Pruebas Funcionales del Sistema

## Proyecto

**ChickenBot Delivery**

---

# Objetivo

Verificar el correcto funcionamiento de todos los módulos implementados del sistema, comprobando que cumplen con los requisitos funcionales establecidos para el bot de Telegram, el panel de administración y la base de datos.

---

# Alcance

Las pruebas funcionales abarcan:

- Panel administrativo.
- Bot del cliente.
- Bot del repartidor.
- Base de datos.
- Integración entre todos los módulos.

---

# Entorno de pruebas

| Componente | Descripción |
|------------|-------------|
| Sistema operativo | Fedora Linux |
| Lenguaje | Python 3 |
| Framework Web | FastAPI |
| Base de datos | PostgreSQL |
| ORM | SQLAlchemy |
| Migraciones | Alembic |
| Bot | python-telegram-bot |
| Navegador | Google Chrome |
| Cliente móvil | Telegram Android |

---

# Casos de prueba

| ID | Módulo | Caso de prueba | Resultado esperado | Resultado |
|----|---------|----------------|--------------------|-----------|
| PF-01 | Panel | Inicio de sesión administrador | Acceso permitido | ✅ Correcto |
| PF-02 | Categorías | Crear categoría | Categoría registrada | ✅ Correcto |
| PF-03 | Categorías | Editar categoría | Datos actualizados | ✅ Correcto |
| PF-04 | Categorías | Eliminar categoría | Categoría eliminada | ✅ Correcto |
| PF-05 | Productos | Crear producto | Producto registrado | ✅ Correcto |
| PF-06 | Productos | Editar producto | Producto actualizado | ✅ Correcto |
| PF-07 | Productos | Eliminar producto | Producto eliminado | ✅ Correcto |
| PF-08 | Pedidos | Visualizar pedidos | Pedidos mostrados correctamente | ✅ Correcto |
| PF-09 | Pedidos | Cambiar estado del pedido | Estado actualizado | ✅ Correcto |
| PF-10 | Repartidores | Registrar repartidor | Repartidor registrado | ✅ Correcto |
| PF-11 | Repartidores | Editar repartidor | Datos actualizados | ✅ Correcto |
| PF-12 | Repartidores | Activar / Desactivar | Estado modificado correctamente | ✅ Correcto |
| PF-13 | Cliente | Mostrar menú | Menú obtenido desde la base de datos | ✅ Correcto |
| PF-14 | Cliente | Agregar productos al carrito | Productos agregados correctamente | ✅ Correcto |
| PF-15 | Cliente | Modificar cantidades | Cantidades actualizadas | ✅ Correcto |
| PF-16 | Cliente | Enviar ubicación | Ubicación registrada | ✅ Correcto |
| PF-17 | Administrador | Confirmar pago | Pedido actualizado | ✅ Correcto |
| PF-18 | Administrador | Asignar repartidor | Pedido asignado correctamente | ✅ Correcto |
| PF-19 | Repartidor | Inicio de sesión | Acceso autorizado | ✅ Correcto |
| PF-20 | Repartidor | Consultar pedidos pendientes | Lista obtenida correctamente | ✅ Correcto |
| PF-21 | Repartidor | Iniciar entrega | Estado "En camino" | ✅ Correcto |
| PF-22 | Repartidor | Confirmar entrega | Solicitud de evidencia fotográfica | ✅ Correcto |
| PF-23 | Repartidor | Enviar fotografía de entrega | Evidencia almacenada | ✅ Correcto |
| PF-24 | Base de datos | Registrar pedido | Información persistida | ✅ Correcto |
| PF-25 | Base de datos | Registrar ubicación | Coordenadas almacenadas | ✅ Correcto |
| PF-26 | Base de datos | Registrar comprobante | Imagen almacenada | ✅ Correcto |
| PF-27 | Base de datos | Registrar fotografía de entrega | Imagen almacenada | ✅ Correcto |
| PF-28 | Integración | Flujo completo del sistema | Pedido finalizado correctamente | ✅ Correcto |

---

# Flujo validado

Durante las pruebas se verificó el siguiente flujo completo:

1. El cliente inicia el bot mediante `/start`.
2. El sistema muestra el menú disponible.
3. El cliente selecciona uno o más productos.
4. Se genera el carrito de compras.
5. El cliente envía la ubicación de entrega.
6. El administrador asigna el pedido a un repartidor.
7.  El repartidor consulta los pedidos pendientes.
8.  El repartidor inicia la entrega.
9.  El sistema actualiza el estado del pedido.
10. El repartidor confirma la entrega.
11. El sistema solicita una fotografía como evidencia.
12. La fotografía queda almacenada en la base de datos.
13. El pedido cambia al estado **Entregado**.

---

# Resultados

Durante la ejecución de las pruebas:

- Todas las funcionalidades implementadas respondieron correctamente.
- La integración entre el bot y el panel administrativo fue satisfactoria.
- La información fue almacenada correctamente en la base de datos.
- No se detectaron errores críticos que impidan el funcionamiento del sistema.

---

# Evidencias


- Inicio de sesión del panel.
- Gestión de categorías.
- Gestión de productos.
- Gestión de repartidores.
- Flujo del bot del cliente.
- Asignación del repartidor.
- Inicio de entrega.
- Confirmación de entrega.
- Evidencia fotográfica almacenada.

---

# Conclusión

Las pruebas funcionales realizadas demuestran que el sistema **ChickenBot Delivery** cumple con los requisitos funcionales definidos para el MVP. La comunicación entre el bot de Telegram, el panel administrativo y la base de datos se realizó correctamente, permitiendo completar el flujo de atención desde la creación del pedido hasta la confirmación de la entrega.