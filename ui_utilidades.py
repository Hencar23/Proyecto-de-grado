# ui_utilidades.py
"""Utility functions for the AprendeKids GUI.
Provides a helper to create large, colorful buttons suitable for children.
"""
import tkinter as tk
from tkinter import font

def crear_boton_grande(parent, texto, command=None):
    """Crea un botón grande y colorido.

    Args:
        parent: widget contenedor donde se colocará el botón.
        texto (str): texto que aparecerá en el botón.
        command (callable, optional): función a ejecutar al pulsar el botón.
    """
    # Fuente grande y legible
    fuente = font.Font(family="Helvetica", size=18, weight="bold")
    # Botón con colores vivos y bordes redondeados (simulado con relief y borderwidth)
    boton = tk.Button(
        parent,
        text=texto,
        command=command,
        font=fuente,
        bg="#ffcc66",      # color naranja pastel
        fg="#000000",
        activebackground="#ffdd88",
        activeforeground="#000000",
        relief=tk.RAISED,
        bd=4,
        padx=10,
        pady=10,
    )
    # Aseguramos que el botón tenga un tamaño mínimo
    boton.configure(width=20, height=2)
    return boton
