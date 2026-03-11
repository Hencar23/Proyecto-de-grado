# lenguaje.py
"""Módulo de la materia Lengua Castellana.
Incluye explicación, tres actividades interactivas y un quiz.
"""
import tkinter as tk
from tkinter import messagebox
from ui_utilidades import crear_boton_grande, reproducir_sonido, animar_respuesta

class LenguaFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=app.cget("bg"))
        self.app = app
        self.estado = app.estado
        self._mostrar_menu()

    def _mostrar_menu(self):
        tk.Label(self, text="Lengua Castellana 📖", font=("Comic Sans MS", 28, "bold"), bg=self.cget("bg"), fg="#E91E63").pack(pady=20)
        crear_boton_grande(self, "Explicación", command=self._explicacion).pack(pady=5)
        crear_boton_grande(self, "Juego 1: Vocal vs Consonante", command=self._juego_vocal_consonante).pack(pady=5)
        crear_boton_grande(self, "Juego 2: Armado de Sílabas", command=self._juego_silabas).pack(pady=5)
        crear_boton_grande(self, "Juego 3: Adivinanzas", command=self._juego_adivinanzas).pack(pady=5)
        crear_boton_grande(self, "Quiz", command=self._quiz).pack(pady=5)
        crear_boton_grande(self, "Volver al Menú", command=self.app.volver_al_menu).pack(pady=15)

    def _explicacion(self):
        self._limpiar()
        tk.Label(self, text="Explicación", font=("Helvetica", 20, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=10)
        texto = (
            "En lengua castellana, una vocal es una letra que se pronuncia sin obstrucción del aire.\n"
            "Las vocales son: a, e, i, o, u.\n\n"
            "Una consonante es cualquier letra que no es vocal."
        )
        tk.Label(self, text=texto, font=("Comic Sans MS", 16), bg=self.cget("bg"), fg="#333", justify="center").pack(pady=10)
        crear_boton_grande(self, "Volver", command=self._mostrar_menu).pack(pady=20)

    def _juego_vocal_consonante(self):
        self._limpiar()
        tk.Label(self, text="Juego: Vocal o Consonante", font=("Helvetica", 20, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=10)
        pregunta = "¿La letra 'b' es vocal o consonante?"
        opciones = ["Vocal", "Consonante"]
        respuesta_correcta = "Consonante"
        self._presentar_pregunta(pregunta, opciones, respuesta_correcta)

    def _juego_silabas(self):
        self._limpiar()
        tk.Label(self, text="Juego: Armado de Sílabas", font=("Helvetica", 20, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=10)
        pregunta = "¿Cuál es la sílaba correcta para completar la palabra 'ca-___'?"
        opciones = ["ma", "na", "ra", "ta"]
        respuesta_correcta = "ma"
        self._presentar_pregunta(pregunta, opciones, respuesta_correcta)

    def _juego_adivinanzas(self):
        self._limpiar()
        tk.Label(self, text="Juego: Adivinanzas", font=("Helvetica", 20, "bold"), bg=self.cget("bg"), fg="#2e8b57").pack(pady=10)
        pregunta = "Soy una palabra que empieza con 'p', termina con 'a' y tiene 'ap' en medio. ¿Qué soy?"
        opciones = ["papa", "pata", "pala", "pira"]
        respuesta_correcta = "papa"
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
            messagebox.showinfo("¡Correcto!", "Respuesta correcta! 🎉")
            self.estado.agregar_estrella(1)
            self.app.actualizar_puntos()
        else:
            messagebox.showerror("Incorrecto", "Inténtalo de nuevo.")
        self._mostrar_menu()

    def _quiz(self):
        self._limpiar()
        tk.Label(self, text="🌟 Quiz Divertido 🌟", font=("Comic Sans MS", 24, "bold"), bg=self.cget("bg"), fg="#E91E63").pack(pady=10)
        preguntas = [
            ("¿Cuál es una vocal?", "a"),
            ("¿La letra 'c' es vocal o consonante?", "Consonante"),
            ("Completa la palabra: 'sol___' (sol + sílaba)", "ar"),
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
        tk.Label(self, text=pregunta, font=("Comic Sans MS", 18, "bold"), bg=self.cget("bg"), fg="#2196F3", wraplength=600).pack(pady=10)
        entry = tk.Entry(self, font=("Helvetica", 14))
        entry.pack(pady=5)
        def comprobar():
            resp = entry.get().strip()
            es_correcto = (resp.lower() == correcta.lower())
            
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
