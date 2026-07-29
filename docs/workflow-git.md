# Flujo de Trabajo con Git

## 1. Objetivo

Durante el desarrollo del proyecto se utilizó Git y GitHub para controlar versiones, organizar el trabajo y mantener un historial de cambios.

---

# 2. Estrategia de ramas

Se utilizó una rama principal de desarrollo (`develop`) y ramas independientes para cada funcionalidad o corrección.

Ejemplo:

```text
develop
   │
   ├── feature/login
   ├── feature/products
   ├── feature/orders
   ├── feature/deliveries
   ├── docs/41-technical-documentation
   └── fix/40-admin-authentication
```

---

# 3. Flujo de trabajo

Para cada tarea se siguió el siguiente proceso:

1. Actualizar la rama `develop`.
2. Crear una nueva rama para la funcionalidad o corrección.
3. Implementar los cambios.
4. Realizar pruebas.
5. Registrar los cambios mediante un commit.
6. Publicar la rama en GitHub (`push`).
7. Crear un Pull Request.
8. Revisar y fusionar los cambios en `develop`.

---

# 4. Convención de commits

Se utilizaron mensajes descriptivos siguiendo una estructura sencilla, por ejemplo:

- `feat: add delivery management`
- `fix: protect delivery routes with admin session validation`
- `docs: add technical documentation`
- `style: improve admin interface with Bootstrap`

---

# 5. Beneficios

El uso de Git permitió:

- Mantener un historial de cambios.
- Trabajar por funcionalidades.
- Facilitar la revisión mediante Pull Requests.
- Reducir el riesgo de conflictos.
- Organizar el desarrollo del proyecto.

---

# Conclusión

El flujo de trabajo basado en Git y GitHub permitió desarrollar el proyecto de manera ordenada, facilitando la integración de nuevas funcionalidades, la corrección de errores y la documentación del sistema.