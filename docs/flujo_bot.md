# Flujo de Conversación del Bot

## 1. Descripción

ChickenBot Delivery utiliza un bot de Telegram para permitir que los clientes consulten el menú disponible, realicen pedidos, compartan su ubicación de entrega y consulten el estado de sus pedidos. La interacción se realiza mediante mensajes, botones en línea (InlineKeyboard) y el envío de ubicación.

---

# 2. Flujo principal

```text
                     /start
                        │
                        ▼
               Menú principal
                        │
      ┌─────────────────┼─────────────────┐
      │                 │                 │
      ▼                 ▼                 ▼
 Ver categorías    Ver carrito     Estado del pedido
      │                 │                 │
      ▼                 ▼                 ▼
Seleccionar      Confirmar pedido   Consultar estado
categoría              │
      │                ▼
      ▼        Compartir ubicación
Mostrar productos       │
      │                 ▼
      ▼          Registrar pedido
Agregar al carrito      │
      │                 ▼
      └──────────► Esperar confirmación
                          │
                          ▼
                 Seguimiento del pedido
                          │
                          ▼
                    Pedido entregado
```

---

# 3. Flujo alternativo

Durante la conversación pueden presentarse distintas situaciones que el bot debe manejar.

### Cancelación

En cualquier momento el usuario puede cancelar el proceso mediante el comando:

```text
/cancelar
```

El bot elimina el contexto de la conversación y vuelve al menú principal.

---

### Producto sin stock

Si un producto ya no tiene disponibilidad:

- El bot informa que el producto no está disponible.
- Solicita seleccionar otro producto.

---

### Cantidad inválida

Si el usuario ingresa una cantidad incorrecta:

- El bot solicita nuevamente una cantidad válida.
- No continúa hasta recibir un valor correcto.

---

### Ubicación no enviada

Si el usuario intenta confirmar el pedido sin compartir su ubicación:

- El bot solicita enviar la ubicación mediante la función de Telegram.
- El pedido no se registra hasta recibir la ubicación.

---

### Pedido confirmado

Una vez registrado correctamente el pedido:

- Se almacena en la base de datos.
- El cliente recibe la confirmación.
- El pedido queda disponible para ser gestionado desde el panel administrativo.

---

# 4. Estados principales

El flujo conversacional contempla los siguientes estados:

- Inicio.
- Menú principal.
- Selección de categoría.
- Selección de producto.
- Carrito de compras.
- Confirmación del pedido.
- Recepción de ubicación.
- Pedido registrado.
- Espera de procesamiento.
- Pedido entregado.

---

# 5. Validaciones

Durante la conversación el sistema verifica:

- Existencia del usuario registrado.
- Disponibilidad del producto.
- Stock suficiente.
- Cantidad válida.
- Existencia de productos en el carrito.
- Recepción de la ubicación de entrega.
- Confirmación del pedido antes de registrarlo.

Si alguna validación falla, el bot informa el error y solicita nuevamente la información correspondiente sin perder el contexto de la conversación.

---

# 6. Beneficios del flujo

El flujo conversacional fue diseñado para que el usuario pueda realizar un pedido de forma sencilla y guiada.

Las principales ventajas son:

- Navegación mediante botones de Telegram.
- Validación de entradas incorrectas.
- Registro automático del pedido.
- Integración con el panel administrativo.
- Seguimiento del estado del pedido desde Telegram.