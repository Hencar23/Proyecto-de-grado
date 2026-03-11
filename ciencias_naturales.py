# ciencias_naturales.py
"""Módulo de la materia Ciencias Naturales.
Incluye explicación, tres actividades interactivas y un quiz.
"""
import tkinter as tk
from tkinter import messagebox
from ui_utilidades import crear_boton_grande

class CienciasNaturalesFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=app.cget("bg"))
        self.app = app
        self.estado = app.estado
        self._mostrar_menu()

    def _mostrar_menu(self):
        tk.Label(self, text="Ciencias Naturales", font=("Helvetica", 22, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=20)
        crear_boton_grande(self, "Explicación", command=self._explicacion).pack(pady=5)
        crear_boton_grande(self, "Juego 1: Vivo vs Inerte", command=self._juego_vivo_inerte).pack(pady=5)
        crear_boton_grande(self, "Juego 2: Vertebrados vs Invertebrados", command=self._juego_vertebrados).pack(pady=5)
        crear_boton_grande(self, "Juego 3: Partes de la Planta", command=self._juego_partes_planta).pack(pady=5)
        crear_boton_grande(self, "Quiz", command=self._quiz).pack(pady=5)
        crear_boton_grande(self, "Volver al Menú", command=self.app.volver_al_menu).pack(pady=15)

    def _explicacion(self):
        self._limpiar()
        tk.Label(self, text="Explicación", font=("Helvetica", 20, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=10)
        texto = (
            "Los seres vivos pueden ser clasificados como "
            "vivos o inertes. Los seres vivos crecen, se alimentan y se reproducen.\n"
            "Ejemplos de seres vivos: plantas, animales, humanos.\n"
            "Ejemplos de cosas inertes: piedras, agua, aire."
        )
        tk.Label(self, text=texto, font=("Helvetica", 14), bg=self.cget("bg"), justify="left").pack(pady=10)
        crear_boton_grande(self, "Volver", command=self._mostrar_menu).pack(pady=20)

    def _juego_vivo_inerte(self):
        self._limpiar()
        tk.Label(self, text="Juego: Vivo o Inerte", font=("Helvetica", 20, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=10)
        pregunta = "¿El árbol es vivo o inerte?"
        opciones = ["Vivo", "Inerte"]
        respuesta_correcta = "Vivo"
        self._presentar_pregunta(pregunta, opciones, respuesta_correcta)

    def _juego_vertebrados(self):
        self._limpiar()
        tk.Label(self, text="Juego: Vertebrados vs Invertebrados", font=("Helvetica", 20, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=10)
        pregunta = "¿La mariposa es vertebrado o invertebrado?"
        opciones = ["Vertebrado", "Invertebrado"]
        respuesta_correcta = "Invertebrado"
        self._presentar_pregunta(pregunta, opciones, respuesta_correcta)

    def _juego_partes_planta(self):
        self._limpiar()
        tk.Label(self, text="Juego: Partes de la Planta", font=("Helvetica", 20, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=10)
        pregunta = "¿Cuál de estas es una raíz?"
        opciones = ["Hoja", "Tallo", "Raíz", "Flor"]
        respuesta_correcta = "Raíz"
        self._presentar_pregunta(pregunta, opciones, respuesta_correcta)

    def _presentar_pregunta(self, pregunta, opciones, correcta):
        tk.Label(self, text=pregunta, font=("Helvetica", 16), bg=self.cget("bg"), wraplength=600).pack(pady=10)
        for opt in opciones:
            crear_boton_grande(self, opt, command=lambda o=opt: self._verificar(o, correcta)).pack(pady=5)
        crear_boton_grande(self, "Volver", command=self._mostrar_menu).pack(pady=15)

    def _verificar(self, seleccion, correcta):
        if seleccion == correcta:
            messagebox.showinfo("¡Correcto!", "Respuesta correcta! 🎉")
            self.estado.agregar_estrella(1)
            self.app.actualizar_puntos()
        else:
            messagebox.showerror("Incorrecto", "Inténtalo de nuevo.")
        self._mostrar_menu()

    def _quiz(self):
        self._limpiar()
        tk.Label(self, text="Quiz de Ciencias Naturales", font=("Helvetica", 20, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=10)
        preguntas = [
            ("¿El agua es un ser vivo?", "No"),
            ("¿Los peces son vertebrados?", "Sí"),
            ("¿La raíz pertenece a la planta?", "Sí"),
        ]
        self.puntuacion = 0
        self.indice = 0
        self.preguntas = preguntas
        self._mostrar_pregunta_quiz()

    def _mostrar_pregunta_quiz(self):
        if self.indice >= len(self.preguntas):
            estrellas = self.puntuacion
            self.estado.agregar_estrella(estrellas)
            self.app.actualizar_puntos()
            messagebox.showinfo("Resultado", f"Obtuviste {self.puntuacion}/{len(self.preguntas)} correctas. Ganaste {estrellas} estrellas.")
            self._mostrar_menu()
            return
        pregunta, correcta = self.preguntas[self.indice]
        self._limpiar()
        tk.Label(self, text=pregunta, font=("Helvetica", 16), bg=self.cget("bg"), wraplength=600).pack(pady=10)
        entry = tk.Entry(self, font=("Helvetica", 14))
        entry.pack(pady=5)
        def comprobar():
            resp = entry.get().strip().lower()
            if (resp == "sí" and correcta == "Sí") or (resp == "si" and correcta == "Sí") or resp == correcta.lower():
                self.puntuacion += 1
                messagebox.showinfo("¡Correcto!", "Respuesta correcta.")
            else:
                messagebox.showerror("Incorrecto", f"La respuesta era {correcta}.")
            self.indice += 1
            self._mostrar_pregunta_quiz()
        crear_boton_grande(self, "Comprobar", command=comprobar).pack(pady=5)
        crear_boton_grande(self, "Cancelar", command=self._mostrar_menu).pack(pady=5)

    def _limpiar(self):
        for widget in self.winfo_children():
            widget.destroy()
