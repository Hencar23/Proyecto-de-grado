# estado.py
"""Módulo de gestión de estado persistente.
Guarda y carga el progreso del estudiante en un archivo JSON.
"""
import json
import os

class Estado:
    def __init__(self, archivo='progreso.json'):
        self.archivo = archivo
        self.datos = {}
        # Si el archivo no existe, lo crea vacío
        if not os.path.exists(self.archivo):
            self._guardar()
        else:
            self._cargar()

    def _cargar(self):
        """Carga los datos del archivo JSON a la variable self.datos."""
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                self.datos = json.load(f)
        except Exception:
            self.datos = {}

    def _guardar(self):
        """Guarda self.datos en el archivo JSON."""
        with open(self.archivo, 'w', encoding='utf-8') as f:
            json.dump(self.datos, f, ensure_ascii=False, indent=4)

    def cargar_usuario(self, nombre):
        """Selecciona o crea la entrada del estudiante.
        Si el estudiante no existe, se crea con 0 estrellas.
        """
        if nombre not in self.datos:
            self.datos[nombre] = {"estrellas": 0}
            self._guardar()
        self.usuario_actual = nombre

    def obtener_estrellas(self):
        """Devuelve la cantidad de estrellas del usuario actual."""
        return self.datos.get(self.usuario_actual, {}).get('estrellas', 0)

    def agregar_estrella(self, cantidad=1):
        """Incrementa las estrellas del usuario actual y guarda el archivo."""
        if hasattr(self, 'usuario_actual') and self.usuario_actual:
            self.datos[self.usuario_actual]['estrellas'] = self.datos[self.usuario_actual].get('estrellas', 0) + cantidad
            self._guardar()
