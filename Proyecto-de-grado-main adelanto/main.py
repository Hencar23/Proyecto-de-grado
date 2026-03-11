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
        self.configure(bg="#E0F7FA")  # fondo azul cyan muy claro, más atractivo infantil

        # Opciones de Pantalla Completa
        self.is_fullscreen = False
        self.bind("<F11>", self.toggle_fullscreen)
        self.bind("<Escape>", self.exit_fullscreen)

        # Estado persistente (carga o crea archivo JSON)
        self.estado = Estado()
        self.current_user = None

        # Contenedor principal donde se cargarán los frames
        self.container = tk.Frame(self, bg=self.cget("bg"))
        self.container.pack(fill="both", expand=True)

        self.show_login()

    def toggle_fullscreen(self, event=None):
        self.is_fullscreen = not self.is_fullscreen
        self.attributes("-fullscreen", self.is_fullscreen)
        
    def exit_fullscreen(self, event=None):
        self.is_fullscreen = False
        self.attributes("-fullscreen", False)

    def show_login(self):
        """Pantalla inicial para introducir el nombre del estudiante."""
        for widget in self.container.winfo_children():
            widget.destroy()
        frame = tk.Frame(self.container, bg=self.cget("bg"))
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text="¡Bienvenido a AprendeKids!", font=("Comic Sans MS", 36, "bold"), bg=self.cget("bg"), fg="#FF5722").pack(pady=40)
        tk.Label(frame, text="Introduce tu nombre amiguito/a:", font=("Comic Sans MS", 18), bg=self.cget("bg"), fg="#333").pack(pady=10)
        entry = tk.Entry(frame, font=("Comic Sans MS", 18), bd=2, relief=tk.SOLID, justify="center")
        entry.pack(pady=5, ipadx=10, ipady=5)
        def continuar():
            nombre = entry.get().strip()
            if not nombre:
                messagebox.showwarning("Nombre requerido", "Por favor escribe tu nombre.")
                return
            self.current_user = nombre
            self.estado.cargar_usuario(nombre)
            self.show_menu()
        
        # Un botón naranja especial para continuar
        crear_boton_grande(frame, "¡Comenzar a Aprender!", command=continuar, bg_color="#FF9800", fg_color="white").pack(pady=30)

    def show_menu(self):
        """Menú principal con botones grandes para cada materia."""
        for widget in self.container.winfo_children():
            widget.destroy()
        # barra de puntuación y pantalla completa
        barra = tk.Frame(self.container, bg="#FFCC80", bd=0) # Barra de estado color naranja claro
        barra.pack(fill="x", side="top", ipady=10)
        
        btn_fs = tk.Button(barra, text="🖥️ Pantalla Completa (F11)", font=("Comic Sans MS", 10, "bold"), bg="#4CAF50", fg="white", cursor="hand2", command=self.toggle_fullscreen, relief=tk.FLAT)
        btn_fs.pack(side="left", padx=20)
        
        self.puntos_label = tk.Label(barra, text=f"🌟 Estrellas: {self.estado.obtener_estrellas()} 🌟", font=("Comic Sans MS", 16, "bold"), bg="#FFCC80", fg="#E65100")
        self.puntos_label.pack(side="right", padx=20)
        
        # título
        tk.Label(self.container, text=f"¡Hola, {self.current_user}!\nElige una materia divertida:", font=("Comic Sans MS", 26, "bold"), bg=self.cget("bg"), fg="#E91E63").pack(pady=20)
        
        # botones de materias (variarán en color por lógica en crear_boton_grande)
        self.container.btn_color_idx = 0
        materias = [
            ("Matemáticas 🔢", MatematicasFrame),
            ("Lengua Castellana 📖", LenguaFrame),
            ("Ciencias Naturales 🌿", CienciasNaturalesFrame),
            ("Ciencias Sociales 🌍", CienciasSocialesFrame),
            ("Inglés 🔤", InglesFrame),
        ]
        
        # Frame para centrar botones mejor (Marco de selección de materias)
        btn_frame = tk.Frame(self.container, bg="#FFFFFF", bd=5, relief=tk.RIDGE, padx=30, pady=20)
        btn_frame.pack(expand=True)
        
        for nombre, clase in materias:
            if "Lengua" in nombre:
                crear_boton_grande(btn_frame, nombre, command=lambda c=clase: self.mostrar_materia(c), bg_color="black").pack(pady=8, ipadx=10, ipady=5)
            else:
                crear_boton_grande(btn_frame, nombre, command=lambda c=clase: self.mostrar_materia(c)).pack(pady=8, ipadx=10, ipady=5)

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
