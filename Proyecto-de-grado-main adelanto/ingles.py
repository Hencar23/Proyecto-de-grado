# ingles.py
"""Módulo de la materia Inglés.
Incluye explicación, tres actividades interactivas y un quiz.
"""
import tkinter as tk
from tkinter import messagebox
from ui_utilidades import crear_boton_grande, reproducir_sonido, animar_respuesta

class InglesFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=app.cget("bg"))
        self.app = app
        self.estado = app.estado
        self._mostrar_menu()

    def _mostrar_menu(self):
        tk.Label(self, text="Inglés 🔤", font=("Comic Sans MS", 28, "bold"), bg=self.cget("bg"), fg="#E91E63").pack(pady=20)
        crear_boton_grande(self, "Explicación", command=self._explicacion).pack(pady=5)
        crear_boton_grande(self, "Juego 1: Colores", command=self._juego_colores).pack(pady=5)
        crear_boton_grande(self, "Juego 2: Números", command=self._juego_numeros).pack(pady=5)
        crear_boton_grande(self, "Juego 3: Animales", command=self._juego_animales).pack(pady=5)
        crear_boton_grande(self, "Quiz", command=self._quiz).pack(pady=5)
        crear_boton_grande(self, "Volver al Menú", command=self.app.volver_al_menu).pack(pady=15)

    def _explicacion(self):
        self._limpiar()
        tk.Label(self, text="Explicación", font=("Helvetica", 20, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=10)
        texto = (
            "Aprender inglés es divertido.\n\n"
            "Colores: Red (Rojo), Blue (Azul), Yellow (Amarillo).\n"
            "Números: One (Uno), Two (Dos), Three (Tres).\n"
            "Animales: Dog (Perro), Cat (Gato), Bird (Pájaro)."
        )
        tk.Label(self, text=texto, font=("Comic Sans MS", 16), bg=self.cget("bg"), fg="#333", justify="center").pack(pady=10)
        crear_boton_grande(self, "Volver", command=self._mostrar_menu).pack(pady=20)

    def _juego_colores(self):
        self._limpiar()
        tk.Label(self, text="Juego: Colores", font=("Helvetica", 20, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=10)
        pregunta = "¿Qué significa 'Blue'?"
        opciones = ["Rojo", "Verde", "Azul", "Amarillo"]
        respuesta_correcta = "Azul"
        self._presentar_pregunta(pregunta, opciones, respuesta_correcta)

    def _juego_numeros(self):
        self._limpiar()
        tk.Label(self, text="Juego: Números", font=("Helvetica", 20, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=10)
        pregunta = "¿Cómo se dice 'Dos' en inglés?"
        opciones = ["One", "Two", "Three", "Four"]
        respuesta_correcta = "Two"
        self._presentar_pregunta(pregunta, opciones, respuesta_correcta)

    def _juego_animales(self):
        self._limpiar()
        tk.Label(self, text="Juego: Animales", font=("Helvetica", 20, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=10)
        pregunta = "¿Qué animal es 'Dog'?"
        opciones = ["Gato", "Perro", "Pájaro", "Pez"]
        respuesta_correcta = "Perro"
        self._presentar_pregunta(pregunta, opciones, respuesta_correcta)

    def _presentar_pregunta(self, pregunta, opciones, correcta):
        tk.Label(self, text=pregunta, font=("Comic Sans MS", 18, "bold"), bg=self.cget("bg"), fg="#2196F3", wraplength=600).pack(pady=10)
        for opt in opciones:
            crear_boton_grande(self, opt, command=lambda o=opt: self._verificar(o, correcta, lbl)).pack(pady=5)
        crear_boton_grande(self, "Volver", command=self._mostrar_menu).pack(pady=15)

    def _verificar(self, seleccion, correcta, label):
        es_correcto = (seleccion == correcta)
        reproducir_sonido(es_correcto)
        animar_respuesta(label, es_correcto, self.cget("bg"))
        if es_correcto:
            messagebox.showinfo("¡Correcto!", "¡Respuesta correcta! 🎉")
            self.estado.agregar_estrella(1)
            self.app.actualizar_puntos()
        else:
            messagebox.showerror("Incorrecto", "Inténtalo de nuevo.")
        self._mostrar_menu()

    def _quiz(self):
        self._limpiar()
        tk.Label(self, text="🌟 Quiz Divertido 🌟", font=("Comic Sans MS", 24, "bold"), bg=self.cget("bg"), fg="#E91E63").pack(pady=10)
        preguntas = [
            ("¿Cómo se escribe 'Rojo' en inglés?", "Red"),
            ("¿Qué número es 'Three'?", "3"),
            ("¿Gato en inglés es 'Cat'? (Sí/No)", "Sí"),
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
            messagebox.showinfo("Resultado", f"Obtuviste {self.puntuacion}/{len(self.preguntas)} correctas.\nGanaste {estrellas} estrellas.")
            self._mostrar_menu()
            return
        pregunta, correcta = self.preguntas[self.indice]
        self._limpiar()
        tk.Label(self, text=pregunta, font=("Comic Sans MS", 18, "bold"), bg=self.cget("bg"), fg="#2196F3", wraplength=600).pack(pady=10)
        entry = tk.Entry(self, font=("Helvetica", 14))
        entry.pack(pady=5)
        def comprobar():
            resp = entry.get().strip().lower()
            es_correcto = False
            if (resp == "sí" and correcta == "Sí") or (resp == "si" and correcta == "Sí") or resp == correcta.lower():
                es_correcto = True
            
            reproducir_sonido(es_correcto)
            animar_respuesta(label, es_correcto, self.cget("bg"))
            
            if es_correcto:
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
