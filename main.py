# main.py
"""Entry point for AprendeKids Python educational app.

- Handles user login (student name).
- Manages navigation between the main menu and subject frames.
- Displays current score (stars) in the top‑right corner.
"""
import json
import os
import tkinter as tk
from tkinter import messagebox

# Import local modules
from estado import Estado
from ui_utilidades import crear_boton_grande
from matematicas import MatematicasFrame
from lenguaje import LenguaFrame
from ciencias_naturales import CienciasNaturalesFrame
from ciencias_sociales import CienciasSocialesFrame
from ingles import InglesFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AprendeKids")
        self.geometry("800x600")
        self.resizable(False, False)
        self.configure(bg="#f0f8ff")  # fondo azul claro

        # Estado persistente (carga o crea archivo JSON)
        self.estado = Estado()
        self.current_user = None

        # Contenedor principal donde se cargarán los frames
        self.container = tk.Frame(self, bg=self.cget("bg"))
        self.container.pack(fill="both", expand=True)

        self.show_login()

    def show_login(self):
        """Pantalla inicial para introducir el nombre del estudiante."""
        for widget in self.container.winfo_children():
            widget.destroy()
        frame = tk.Frame(self.container, bg=self.cget("bg"))
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text="¡Bienvenido a AprendeKids!", font=("Helvetica", 24, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=40)
        tk.Label(frame, text="Introduce tu nombre:", font=("Helvetica", 16), bg=self.cget("bg"), fg="#333").pack(pady=10)
        entry = tk.Entry(frame, font=("Helvetica", 16))
        entry.pack(pady=5)
        def continuar():
            nombre = entry.get().strip()
            if not nombre:
                messagebox.showwarning("Nombre requerido", "Por favor escribe tu nombre.")
                return
            self.current_user = nombre
            self.estado.cargar_usuario(nombre)
            self.show_menu()
        crear_boton_grande(frame, "Continuar", command=continuar).pack(pady=20)

    def show_menu(self):
        """Menú principal con botones grandes para cada materia."""
        for widget in self.container.winfo_children():
            widget.destroy()
        # barra de puntuación
        barra = tk.Frame(self.container, bg=self.cget("bg"))
        barra.pack(fill="x", side="top")
        self.puntos_label = tk.Label(barra, text=f"Estrellas: {self.estado.obtener_estrellas()} ⭐", font=("Helvetica", 14), bg=self.cget("bg"), fg="#ff8c00")
        self.puntos_label.pack(side="right", padx=10, pady=5)
        # título
        tk.Label(self.container, text=f"Hola, {self.current_user}! Elige una materia:", font=("Helvetica", 20, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=30)
        # botones de materias
        materias = [
            ("Matemáticas", MatematicasFrame),
            ("Lengua Castellana", LenguaFrame),
            ("Ciencias Naturales", CienciasNaturalesFrame),
            ("Ciencias Sociales", CienciasSocialesFrame),
            ("Inglés", InglesFrame),
        ]
        for nombre, clase in materias:
            crear_boton_grande(self.container, nombre, command=lambda c=clase: self.mostrar_materia(c)).pack(pady=8, ipadx=10, ipady=5)

    def mostrar_materia(self, frame_class):
        """Cambia al frame de la materia seleccionada."""
        for widget in self.container.winfo_children():
            widget.destroy()
        frame = frame_class(self.container, self)
        frame.pack(fill="both", expand=True)

    def actualizar_puntos(self):
        """Actualiza la etiqueta de estrellas después de una actividad."""
        self.puntos_label.config(text=f"Estrellas: {self.estado.obtener_estrellas()} ⭐")

    def volver_al_menu(self):
        self.show_menu()


if __name__ == "__main__":
    app = App()
    app.mainloop()
