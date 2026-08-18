<div align="center">
  <img src="assets/logo.jpg" alt="RPA UC FACYT Logo" width="300"/>

  # Taller de RPA: Sistema de Tracking por Fechas
  **Universidad de Carabobo (UC) | FACYT**  
  **Materia:** Sistemas de Información | **Semestre:** 7mo
</div>

---

## 🤖 ¿Qué es un RPA (Robotic Process Automation)?

La **Automatización Robótica de Procesos (RPA)** es una tecnología que permite crear "robots de software" diseñados para emular las acciones de un ser humano interactuando con sistemas digitales.

En lugar de requerir complejas integraciones a nivel de API, los RPAs a menudo interactúan con la interfaz de usuario, leen archivos locales, extraen información y toman decisiones basadas en reglas de negocio predefinidas. 
**En este taller**, nuestro RPA actúa como un *Data Processor* que automatiza el seguimiento y conciliación de archivos físicos (`.csv`, `.xlsx`) distribuidos en estructuras de directorios por fechas, garantizando que ninguna solicitud se quede sin procesar.

---

## 🎯 Objetivo del Proyecto

El objetivo de este proyecto es construir un sistema de tracking altamente eficiente para el procesamiento masivo de datos diarios. En lugar de utilizar bases de datos pesadas o prefijos de archivos complejos, este sistema implementa **Teoría de Conjuntos** mediante el uso de `Dataclasses` inmutables en Python.

### ¿Cómo funciona?
1. **Entrada (Input):** Una carpeta estructurada dinámicamente como `data/input/YYYY/MM/DD/` donde se arrojan archivos brutos.
2. **Salida (Output):** Una estructura espejo `data/output/YYYY/MM/DD/` donde se guardan los archivos tras ser procesados por el robot.
3. **Tracking Inteligente:** El RPA calcula dinámicamente la diferencia de conjuntos (`inputs - outputs`) comparando la ruta relativa de cada archivo, identificando en milisegundos qué archivos aún faltan por procesar.

---

## ⚙️ Arquitectura Técnica

- **Lenguaje:** Python 3.10+
- **Paradigmas aplicados:** Programación Orientada a Objetos, Hashing y Diferencia de Conjuntos (`__eq__`, `__hash__`).
- **Librerías principales:**
  - `pathlib`: Para manipulación segura y recursiva de rutas del sistema operativo (`rglob`).
  - `dataclasses`: Para estructuras de datos ligeras, hashables y eficientes.

---

## 🚀 Cómo Ejecutar el Proyecto

### 1. Clonar y preparar el entorno

Clona este repositorio o asegúrate de tener los archivos en tu máquina. Te recomendamos usar un entorno virtual:

```bash
# Crear entorno virtual (Opcional pero recomendado)
python -m venv venv
venv\Scripts\activate  # En Windows

# Instalar dependencias (si aplica según pdm.lock / requirements)
pip install -r requirements.txt 
```

### 2. Estructura de Directorios

El bot espera encontrar o creará las carpetas de datos en la raíz del proyecto. Asegúrate de anexar tus archivos dentro de subcarpetas organizadas por fecha:

```text
/data/input/2028/01/15/solicitudes.csv
/data/input/2028/01/16/reclamos.xlsx
```

### 3. Prueba rápida del Tracker

El proyecto incluye un script de validación que crea un entorno de prueba en tiempo real, genera archivos ficticios y demuestra cómo el algoritmo de conjuntos detecta los archivos pendientes sin modificar tus datos reales.

Para ejecutar esta prueba demostrativa:

```bash
python probar_tracking.py
```

### 4. Integración Principal

Para correr el bot completo en tu entorno de producción (una vez configurados los conectores y servicios):

```bash
python src/taller_rpm_uc/main.py
```

---
<div align="center">
  <i>Desarrollado para fines académicos en la Facultad Experimental de Ciencias y Tecnología (FACYT).</i>
</div>
