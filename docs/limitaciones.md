# Limitaciones del Sistema

## 1. Objetivo

Este documento describe las limitaciones conocidas de la versión actual de ChickenBot Delivery, indicando los aspectos que podrían mejorarse en futuras versiones.

---

# 2. Limitaciones actuales

## 2.1 Un único administrador

Actualmente el sistema permite el acceso mediante un único usuario administrador configurado para gestionar el panel administrativo.

### Posible mejora

Implementar un sistema de usuarios con roles y permisos.

---

## 2.2 Pasarela de pagos

El sistema no integra una pasarela de pagos en línea.

El cliente realiza el pago utilizando los métodos definidos por el negocio y posteriormente continúa con el proceso del pedido.

### Posible mejora

Integrar servicios como:

- Stripe
- PayPal
- QR
- Otros medios electrónicos compatibles.

---

## 2.3 Seguimiento en tiempo real

La ubicación del repartidor no se actualiza continuamente durante la entrega.

Únicamente se registra la ubicación de destino del pedido.

### Posible mejora

Implementar seguimiento GPS en tiempo real.

---

## 2.4 Notificaciones

Las notificaciones del sistema se realizan mediante Telegram.

No existen notificaciones por correo electrónico o SMS.

### Posible mejora

Agregar canales adicionales de comunicación.

---

## 2.5 Reportes

El sistema no genera reportes estadísticos ni gráficos de ventas.

### Posible mejora

Incorporar un módulo de reportes con indicadores como:

- Ventas diarias.
- Productos más vendidos.
- Pedidos por fecha.
- Rendimiento de repartidores.

---

## 2.6 Escalabilidad

La aplicación está diseñada para pequeños y medianos negocios de comida.

No ha sido optimizada para soportar grandes volúmenes de usuarios concurrentes.

### Posible mejora

Implementar balanceo de carga, caché y optimizaciones para alta concurrencia.

---

## 2.7 Recuperación de contraseña

El sistema no dispone de un mecanismo para recuperar la contraseña del administrador.

### Posible mejora

Implementar recuperación mediante correo electrónico o autenticación multifactor.

---

# 3. Consideraciones

Las limitaciones descritas no afectan el funcionamiento esperado del proyecto dentro del alcance definido para esta versión.

El sistema cumple con los requisitos funcionales planteados para el proyecto académico y proporciona una base sólida para futuras mejoras.

---

# 4. Trabajo futuro

Entre las mejoras que podrían incorporarse en versiones posteriores se encuentran:

- Gestión de múltiples administradores.
- Reportes estadísticos.
- Pasarela de pagos en línea.
- Seguimiento en tiempo real de repartidores.
- Sistema de promociones y descuentos.
- Historial completo de pedidos por cliente.
- Panel de estadísticas con gráficos.
- API pública para integración con aplicaciones móviles.

---

# Conclusión

ChickenBot Delivery cumple con los objetivos establecidos para el proyecto, aunque existen oportunidades de mejora orientadas a incrementar la funcionalidad, la seguridad y la escalabilidad del sistema en futuras versiones.