# hand\_scan

Transform Gestures into Instant Interactive Experiences

---

## Overview

**hand\_scan** es una herramienta para desarrolladores que permite la detección de manos y reconocimiento de gestos en tiempo real usando una webcam.

El sistema superpone una plantilla para alinear la mano y desencadena acciones multimedia (como reproducir un video) cuando detecta la posición correcta. Utiliza MediaPipe para la detección de landmarks y OpenCV para el procesamiento de imágenes.

### ¿Por qué usar hand\_scan?

* 🔵 **Detección en tiempo real**: Rastreo continuo de una mano con mínima latencia.
* 🟢 **Activación de gestos**: Ejecuta acciones al detectar posiciones específicas de la mano.
* 🟡 **Plantilla de alineación**: Ayuda al usuario a colocar la mano correctamente.
* 🔣 **Integración con MediaPipe**: Detección precisa basada en landmarks.
* 🟠 **Procesamiento con OpenCV**: Fluidez y eficiencia en la imagen.

---

## Getting Started

### Prerequisitos

* Python 3.8 o superior
* Conda (gestor de entornos)

### Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/CristhianTorrezSilva/hand_scan
```

2. Navegar al directorio del proyecto:

```bash
cd hand_scan
```

3. Instalar dependencias con Conda:

```bash
conda env create -f conda.yml
```

---

## Uso

1. Activar el entorno:

```bash
conda activate hand_scan_env
```

2. Ejecutar el proyecto:

```bash
python main.py
```

---

## Testing

Este proyecto utiliza `pytest` como framework de pruebas. Para correr el test suite:

```bash
conda activate hand_scan_env
pytest
```

---

## Licencia

MIT License © 2025 Cristhian Torrez Silva

---

## Agradecimientos

* [MediaPipe](https://google.github.io/mediapipe/)
* [OpenCV](https://opencv.org/)
   
