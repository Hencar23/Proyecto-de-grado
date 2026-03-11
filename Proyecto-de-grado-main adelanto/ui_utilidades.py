# ui_utilidades.py
"""Utility functions for the AprendeKids GUI.
Provides a helper to create large, colorful buttons suitable for children.
"""
import tkinter as tk
from tkinter import font
import winsound

def crear_boton_grande(parent, texto, command=None, bg_color="#FF9800", fg_color="white"):
    """Crea un botón grande, colorido y llamativo.

    Args:
        parent: widget contenedor donde se colocará el botón.
        texto (str): texto que aparecerá en el botón.
        command (callable, optional): función a ejecutar al pulsar el botón.
        bg_color (str): color de fondo principal del botón.
        fg_color (str): color del texto.
    """
    # Fuente aún más grande y juguetona
    fuente = font.Font(family="Comic Sans MS", size=20, weight="bold")
    
    # Intentar usar colores variados si no se especifica uno
    if bg_color == "#FF9800" and hasattr(parent, 'btn_color_idx'):
        colores = ["#FF5722", "#4CAF50", "#2196F3", "#9C27B0", "#FFC107", "#E91E63"]
        bg_color = colores[parent.btn_color_idx % len(colores)]
        parent.btn_color_idx += 1
    elif bg_color == "#FF9800":
        parent.btn_color_idx = 0
        bg_color = "#FF5722"

    # Botón con estilo "Flat" moderno pero colorido
    boton = tk.Button(
        parent,
        text=texto,
        command=command,
        font=fuente,
        bg=bg_color,
        fg=fg_color,
        activebackground="#FFB74D", # Color cuando se presiona
        activeforeground="white",
        relief=tk.FLAT, # Plano para que luzca más moderno
        bd=0, # Sin borde estándar de windows
        padx=15,
        pady=10,
        cursor="hand2" # Cambia el cursor para indicar que es clickeable
    )
    # Tamaño base
    boton.configure(width=22, height=1)
    return boton


def reproducir_sonido(es_correcto):
    """Reproduce un sonido de acierto o error usando winsound."""
    try:
        if es_correcto:
            # Tono agudo y corto para acierto
            winsound.Beep(1000, 200)
            winsound.Beep(1200, 200)
        else:
            # Tono grave para error
            winsound.Beep(300, 400)
    except Exception:
        # Falla silenciosamente si no se puede reproducir (ej. en Mac/Linux sin winsound)
        pass

def animar_respuesta(widget, es_correcto, color_original):
    """Cambia temporalmente el color de fondo de un widget para indicar acierto o error."""
    color_nuevo = "#a8e6cf" if es_correcto else "#ff8b94" # Verde pastel o Rojo pastel
    widget.config(bg=color_nuevo)
    widget.after(500, lambda: widget.config(bg=color_original))
