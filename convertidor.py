import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import os

def seleccionar_imagen():
    ruta_archivo = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[
            ("Archivos de imagen", "*.jpg *.jpeg *.png *.gif *.webp *.bmp *.ico *.JPG *.JPEG *.PNG *.WEBP"),
            ("Todos los archivos", "*.*")
        ]
    )
    if ruta_archivo:
        etiqueta_ruta.config(text=os.path.basename(ruta_archivo), fg="#1a73e8")
        app.ruta_archivo = ruta_archivo

def convertir_imagen():
    if not hasattr(app, 'ruta_archivo') or not app.ruta_archivo:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una imagen primero.")
        return

    formato_seleccionado = variable_formato.get()
    formato_destino = "ico" if "Favicon" in formato_seleccionado else formato_seleccionado.lower()
    
    try:
        img = Image.open(app.ruta_archivo)
        ruta_base = os.path.splitext(app.ruta_archivo)[0]
        nueva_ruta = f"{ruta_base}_convertida.{formato_destino}"

        if formato_destino == 'ico':
            img = img.resize((32, 32), Image.Resampling.LANCZOS)
        elif formato_destino in ['jpg', 'jpeg', 'bmp']:
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                fondo = Image.new("RGB", img.size, (255, 255, 255))
                img_rgba = img.convert("RGBA")
                fondo.paste(img_rgba, mask=img_rgba.split()[3])
                img = fondo
            elif img.mode != 'RGB':
                img = img.convert('RGB')

        formato_pil = 'JPEG' if formato_destino == 'jpg' else formato_destino.upper()
        img.save(nueva_ruta, format=formato_pil)
        
        messagebox.showinfo("¡Éxito!", f"Imagen convertida y guardada como:\n{os.path.basename(nueva_ruta)}")
    
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo convertir la imagen:\n{e}")

# 'convertidor' en minúsculas para coincidir exactamente con el escritorio de GNOME
app = tk.Tk(className="convertidor")
app.title("Convertidor Rápido de Imágenes")
app.geometry("430x290")
app.resizable(False, False)

# Intentar cargar el ícono morado del sistema directamente en la ventana
icon_paths = [
    "/usr/share/icons/Yaru/256x256/mimetypes/image-x-generic.png",
    "/usr/share/icons/Yaru/128x128/mimetypes/image-x-generic.png",
    "/usr/share/icons/Yaru/64x64/mimetypes/image-x-generic.png",
    "/usr/share/icons/Yaru/48x48/mimetypes/image-x-generic.png"
]
for path in icon_paths:
    if os.path.exists(path):
        try:
            icono = tk.PhotoImage(file=path)
            app.iconphoto(True, icono)
            break
        except Exception:
            pass

tk.Label(app, text="Convertidor para Blogger", font=("Arial", 15, "bold")).pack(pady=18)

btn_abrir = tk.Button(app, text="1. Abrir Imagen", command=seleccionar_imagen, font=("Arial", 10), width=24, height=1)
btn_abrir.pack(pady=6)

etiqueta_ruta = tk.Label(app, text="(Ninguna imagen seleccionada)", fg="gray", font=("Arial", 10))
etiqueta_ruta.pack(pady=2)

frame_formato = tk.Frame(app)
frame_formato.pack(pady=18)

tk.Label(frame_formato, text="2. Convertir a:", font=("Arial", 10)).pack(side=tk.LEFT)
formatos_disponibles = ["png", "jpg", "webp", "ico (Favicon)", "gif", "bmp"]
variable_formato = tk.StringVar(value="png")
menu_desplegable = ttk.Combobox(frame_formato, textvariable=variable_formato, values=formatos_disponibles, state="readonly", width=14, font=("Arial", 10))
menu_desplegable.pack(side=tk.LEFT, padx=8)

btn_convertir = tk.Button(app, text="3. ¡Convertir!", command=convertir_imagen, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), width=24, height=1)
btn_convertir.pack(pady=8)

app.mainloop()
