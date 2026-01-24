"""4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:
restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un
método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase
Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los
sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
al método. """
class Restaurante:
    def __init__(self, restaurante_nombre, tipo_comida):
        self.restaurante_nombre = restaurante_nombre
        self.tipo_comida = tipo_comida

    def describir_restaurante(self):
        print(f"Nombre del restaurante: {self.restaurante_nombre}")
        print(f"Tipo de comida: {self.tipo_comida}")

    def abrir_restaurante(self):
        print(f"El restaurante {self.restaurante_nombre} ahora está abierto.")


class Heladeria(Restaurante):
    def __init__(self, restaurante_nombre, tipo_comida, sabores):
        super().__init__(restaurante_nombre, tipo_comida)
        self.sabores = sabores

    def mostrar_sabores(self):
        print("Sabores disponibles:")
        for sabor in self.sabores:
            print(f"- {sabor}")

mi_heladeria = Heladeria("Dulce Frío", "Postres", ["Chocolate", "Vainilla", "Frutilla", "Menta"])

mi_heladeria.describir_restaurante()
mi_heladeria.abrir_restaurante()
mi_heladeria.mostrar_sabores()