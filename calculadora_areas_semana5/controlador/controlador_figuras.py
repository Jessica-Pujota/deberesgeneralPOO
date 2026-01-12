"""
Controlador: ControladorFiguras
Descripción: Coordina la lógica entre el modelo y la vista.
"""

from modelo.figuras import Rectangulo, Circulo, Triangulo
from vista.vista_figuras import VistaFiguras


class ControladorFiguras:

    def __init__(self):
        self.vista = VistaFiguras()

    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu()

            if opcion == 1:
                base, altura = self.vista.solicitar_datos_rectangulo()
                figura = Rectangulo(base, altura)

            elif opcion == 2:
                radio = self.vista.solicitar_datos_circulo()
                figura = Circulo(radio)

            elif opcion == 3:
                base, altura = self.vista.solicitar_datos_triangulo()
                figura = Triangulo(base, altura)

            elif opcion == 4:
                print("Saliendo del programa...")
                break

            else:
                print("Opción inválida.")
                continue

            area = figura.calcular_area()
            self.vista.mostrar_resultado(area)
