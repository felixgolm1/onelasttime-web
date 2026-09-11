# REGLAS DEL PROYECTO: SENSIBLES WEB

## 1. MODIFICACIONES DE FRONTEND (COPY Y LAYOUT)
- Toda modificación de copys, tamaños, posicionamiento o animaciones asume por defecto que es **exclusivamente para la vista móvil (`@media (max-width: 768px)` o condicionales JS de móvil)**.
- **PROHIBIDO** alterar la estructura de etiquetas HTML, los saltos de línea (como los divs `.flt-line`) o el CSS general de la vista Desktop, a menos que el usuario especifique explícitamente "cambiar también en desktop".
- La vista Desktop se considera sagrada y estable. No la desordenes.
