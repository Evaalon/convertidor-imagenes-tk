   # Convertidor de Imágenes (Python / Tkinter)

Utilidad de escritorio ligera creada en Python con Tkinter y Pillow para convertir formatos de imagen de forma local y rápida, además de generar favicons `.ico` de 32x32 listos para web.

## Características
* Convierte entre formatos comunes: **JPG, PNG, WebP, GIF y BMP**.
* Genera **favicons `.ico` de 32x32** con reescalado de alta calidad (Lanczos).
* Funciona 100% sin conexión desde una ventana de escritorio sencilla.

## Requisitos previos
* Python 3 instalado.
* En **Ubuntu / Debian**, instala Tkinter:

```bash
sudo apt update && sudo apt install python3-tk -y
```

## Instalación y uso

1. Clona este repositorio (o descárgalo como ZIP desde el botón verde **Code**):

```bash
git clone https://github.com/Evaalon/convertidor-imagenes-tk.git
cd convertidor-imagenes-tk
```

2. Instala la dependencia necesaria (`Pillow`):

```bash
pip install -r requirements.txt
```

3. Ejecuta el programa:

```bash
python3 convertidor.py
``` 
    
    
