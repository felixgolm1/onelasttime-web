# Brain / Mapa del Proyecto: "One Last Time" Cinematic Web

Este documento actúa como el **Cerebro Central (Single Source of Truth - SSOT)** del proyecto. Aquí se recopila todo el conocimiento acumulado a lo largo de las distintas conversaciones, detalles de implementación, variables y timings de animación para que no se pierdan entre sesiones.

---

## 🚀 Información General

*   **Objetivo:** Crear una experiencia web 3D cinemática ultra-premium controlada por scroll, centrada en la unboxing experience y la neurociencia de la oxitocina.
*   **Servidor de Desarrollo (DEV):** `http://localhost:8000`
    *   **Ruta local:** `c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\`
    *   **Archivo de pruebas 3D:** `3d-test.html` (Toda la experimentación se hace AQUÍ).
*   **Servidor de Producción (PROD):** `http://localhost:8001`
    *   **Ruta local:** `c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web-produccion\`
    *   **Repositorio Git:** Limpio e independiente, conectado a `onelasttime-web-produccion` en GitHub.

---

## 🛡️ Reglas de Oro Inquebrantables

1.  **Producción es Sagrada:** NUNCA editar ni tocar directamente archivos en la carpeta de producción. Solo se modifica mediante el comando de despliegue/pase oficial.
2.  **El archivo `index.html` es INTOCABLE:** No pertenece a las pruebas 3D. Bajo ningún concepto debe ser modificado o sobrescrito por `3d-test.html`.
3.  **Sistema de Backups Automático (Git) en DEV:**
    *   **Antes de cualquier cambio en DEV:** Hacer commit de seguridad:
        ```powershell
        git add 3d-test.html && git commit -m "antes de: [descripción del cambio]"
        ```
    *   **Después de cualquier cambio en DEV:** Guardar y subir a la nube:
        ```powershell
        git add 3d-test.html && git commit -m "hecho: [descripción del cambio]" && git push origin main
        ```
4.  **Autonomía Total:** El asistente ejecuta los comandos y cambios de archivos directamente sin interrumpir pidiendo confirmación o permisos.
5.  **Carga Obligatoria de Memoria (Inicialización):** Al iniciar cualquier nueva conversación o sesión, el asistente debe leer obligatoriamente este archivo (`project-map.md`) en su totalidad para asimilar todas las reglas, timings, estado actual e historial del proyecto antes de realizar cualquier cambio o responder.

---

## 📈 Línea de Tiempo de Animaciones y Timings (SSOT)

| Elemento / Evento | Timing (Scroll Progress / Segundos) | Detalles de la Animación |
| :--- | :--- | :--- |
| **Expansión del Retrato** | `14.72` | Punto exacto de expansión del elemento portrait para sincronización cinemática. |
| **Zoom-in del Cerebro 3D** | `17.0` a `17.8` | Rango de zoom de la cámara 3D (controlado por `swapT`). |
| **Drift del Título** (`#oxitocina-title`) | `17.0` a `17.8` | Desplazamiento diagonal suave del título *"NO ES MAGIA, ES OXITOCINA"* desde el centro (`top: 67%`, `left: 50%`, `scale: 1`) hacia la derecha (`top: 27%`, `left: 72%`, `scale: 0.28`). Mantiene `translate(-50%, -50%)`. |
| **Aparición de Neuro-Card** | `17.43` a `17.58` | Fade-in ultra-rápido de la tarjeta de glassmorphism (duración: `0.15s`, mejorado un 50%). |
| **Animación de Texto (Oryzo)** | *Pendiente* | **Entrada:** Líneas suben desde abajo (`y: '100%'`) a través de una máscara invisible (`overflow:hidden`), staggered. <br>**Salida:** Las palabras se desvanecen (fade-out) en cascada desde la última línea hasta la primera (bottom-right a top-left). |

---

## 💬 Historial de Sesiones Clave

### 1. Sesión: Neural Wiring Cinematic Title Integration (`0dd48e66-c440-4094-9c6a-ecc2e769bc3f`)
*   **Logros:** Ajuste de tiempos para el efecto de "flicker" en reverse scroll y sincronización de la expansión del retrato en `14.72`.

### 2. Sesión: Local Dev Environment (`173650cd-98ba-42ec-8e22-ac60efb2f899`)
*   **Logros:** Configuración de los puertos locales en segundo plano (`8000` para DEV y `8001` para PROD).

### 3. Sesión: Venga sigamos desarrollando (`7f535f53-508c-421b-8353-220202516ddf`)
*   **Logros:** Implementación del movimiento diagonal del título con la oxitocina, optimización de la velocidad del fade-in de la neuro-card a `0.15s` de duración e inicio en `17.43`. Despliegue limpio a producción.

---

## 🛠️ Protocolo Exacto de Pase a Producción

Cuando se solicita *"pasar al entorno de producción"*, se ejecuta autónomamente:
1. Copiar `3d-test.html` y la carpeta `assets/` (si hay recursos nuevos) desde `sensibles-web` a `sensibles-web-produccion` usando `Copy-Item -Force`.
2. Sincronizar **DEV** a GitHub: `git push origin main` en la carpeta DEV.
3. Sincronizar **PROD** a GitHub: `git add .`, `git commit -m "hecho: pase a produccion"` y `git push origin main` en la carpeta PROD.
