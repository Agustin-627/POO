"""2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener
como miembros:
o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
o Un atributo para el estado (lleno o vacío).
o Un atributo n, que indica la cantidad máxima de cebadas.
o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
“Advertencia: el mate está lavado.” pero no se debe lanzar una excepción."""

class Mate:
    def __init__(self, n):
        self.cebadas_restantes = n
        self.estado = 'vacío'
        self.n = n

    def cebar(self):
        if self.estado == 'lleno':
            print("¡Cuidado! ¡Te quemaste!")
            return
        self.estado = 'lleno'

    def beber(self):
        if self.estado == 'vacío':
            print("¡El mate está vacío!")
            return

        self.estado = 'vacío'

        if self.cebadas_restantes > 0:
            self.cebadas_restantes -= 1
        else:
            print("Advertencia: el mate está lavado.")
