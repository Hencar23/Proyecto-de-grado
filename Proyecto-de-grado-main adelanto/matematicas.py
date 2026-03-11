# matematicas.py
"""Módulo de la materia Matemáticas.
Incluye una pantalla con explicación, tres actividades interactivas y un quiz.
"""
import tkinter as tk
from tkinter import messagebox
from ui_utilidades import crear_boton_grande, reproducir_sonido, animar_respuesta
from estado import Estado

class MatematicasFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=app.cget("bg"))
        self.app = app
        self.estado = app.estado
        self._mostrar_menu()

    def _mostrar_menu(self):
        """Muestra el menú de la materia con opciones de actividades."""
        tk.Label(self, text="Matemáticas 🔢", font=("Comic Sans MS", 28, "bold"), bg=self.cget("bg"), fg="#E91E63").pack(pady=20)
        crear_boton_grande(self, "Explicación", command=self._explicacion).pack(pady=5)
        crear_boton_grande(self, "Juego 1: Sumas", command=self._juego_sumas).pack(pady=5)
        crear_boton_grande(self, "Juego 2: Restas", command=self._juego_restas).pack(pady=5)
        crear_boton_grande(self, "Juego 3: Secuencias", command=self._juego_secuencias).pack(pady=5)
        crear_boton_grande(self, "Quiz", command=self._quiz).pack(pady=5)
        crear_boton_grande(self, "Volver al Menú", command=self.app.volver_al_menu).pack(pady=15)

    def _explicacion(self):
        """Muestra una explicación simple de sumas y restas."""
        self._limpiar()
        tk.Label(self, text="Explicación", font=("Helvetica", 20, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=10)
        texto = (
            "En matemáticas, la suma combina dos números para obtener otro número.\n"
            "Ejemplo: 3 + 2 = 5.\n\n"
            "La resta quita un número de otro.\n"
            "Ejemplo: 5 - 2 = 3."
        )
        tk.Label(self, text=texto, font=("Comic Sans MS", 16), bg=self.cget("bg"), fg="#333", justify="center").pack(pady=10)
        crear_boton_grande(self, "Volver", command=self._mostrar_menu).pack(pady=20)

    def _juego_sumas(self):
        """Juego de suma con opciones múltiples."""
        self._limpiar()
        tk.Label(self, text="Juego: Sumas", font=("Helvetica", 20, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=10)
        pregunta = "¿Cuánto es 4 + 3?"
        opciones = ["5", "6", "7", "8"]
        respuesta_correcta = "7"
        self._presentar_pregunta(pregunta, opciones, respuesta_correcta)

    def _juego_restas(self):
        """Juego de resta con opciones múltiples."""
        self._limpiar()
        tk.Label(self, text="Juego: Restas", font=("Helvetica", 20, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=10)
        pregunta = "¿Cuánto es 9 - 4?"
        opciones = ["3", "4", "5", "6"]
        respuesta_correcta = "5"
        self._presentar_pregunta(pregunta, opciones, respuesta_correcta)

    def _juego_secuencias(self):
        """Juego de completar secuencias numéricas."""
        self._limpiar()
        tk.Label(self, text="Juego: Secuencias", font=("Helvetica", 20, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=10)
        pregunta = "Completa la secuencia: 2, 4, 6, __"
        opciones = ["7", "8", "9", "10"]
        respuesta_correcta = "8"
        self._presentar_pregunta(pregunta, opciones, respuesta_correcta)

    def _presentar_pregunta(self, pregunta, opciones, respuesta_correcta):
        """Muestra una pregunta y verifica la respuesta del niño."""
        lbl = tk.Label(self, text=pregunta, font=("Helvetica", 16), bg=self.cget("bg"), wraplength=600)
        lbl.pack(pady=10)
        var = tk.StringVar(value="")
        for opt in opciones:
            crear_boton_grande(self, opt, command=lambda o=opt: self._verificar(o, respuesta_correcta, lbl)).pack(pady=5)
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
        # volver al menú de la materia
        self._mostrar_menu()

    def _quiz(self):
        """Quiz corto de 3 preguntas con calificación automática."""
        self._limpiar()
        tk.Label(self, text="🌟 Quiz Divertido 🌟", font=("Comic Sans MS", 24, "bold"), bg=self.cget("bg"), fg="#E91E63").pack(pady=10)
        preguntas = [
            ("5 + 2 = ?", "7"),
            ("10 - 3 = ?", "7"),
            ("¿Cuál sigue? 1, 3, 5, __", "7"),
        ]
        self.puntuacion = 0
        self.indice = 0
        self.preguntas = preguntas
        self._mostrar_pregunta_quiz()

    def _mostrar_pregunta_quiz(self):
        if self.indice >= len(self.preguntas):
            # Quiz terminado
            estrellas_ganadas = self.puntuacion
            self.estado.agregar_estrella(estrellas_ganadas)
            self.app.actualizar_puntos()
            messagebox.showinfo("Resultado", f"Obtuviste {self.puntuacion}/{len(self.preguntas)} respuestas correctas.\nHas ganado {estrellas_ganadas} estrellas.")
            self._mostrar_menu()
            return
        pregunta, correcta = self.preguntas[self.indice]
        self._limpiar()
        tk.Label(self, text=pregunta, font=("Comic Sans MS", 18, "bold"), bg=self.cget("bg"), fg="#2196F3", wraplength=600).pack(pady=10)
        entry = tk.Entry(self, font=("Helvetica", 14))
        entry.pack(pady=5)
        def comprobar():
            respuesta = entry.get().strip()
            es_correcto = (respuesta == correcta)
            
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
