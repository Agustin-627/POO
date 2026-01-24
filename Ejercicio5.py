"""5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que
reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover
que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
 Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro
personaje, al que le debe hacer el daño indicado por el atributo ataque.
 Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que
devuelva la cantidad cosechada"""

class Personaje:
    def __init__(self, vida, posicion, velocidad):
        self.vida = vida
        self.posicion = posicion
        self.velocidad = velocidad

    def recibir_ataque(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            print("El personaje ha muerto.")
            return False
        print(f"Vida restante: {self.vida}")
        return True

    def mover(self, direccion):
        if direccion == "derecha":
            self.posicion += self.velocidad
        elif direccion == "izquierda":
            self.posicion -= self.velocidad
        else:
            print("Dirección no válida.")
            return False
        print(f"Posición actual: {self.posicion}")
        return True


class Soldado(Personaje):
    def __init__(self, vida, posicion, velocidad, ataque):
        super().__init__(vida, posicion, velocidad)
        self.ataque = ataque

    def atacar(self, otro_personaje):
        print(f"El soldado ataca causando {self.ataque} de daño.")
        return otro_personaje.recibir_ataque(self.ataque)


class Campesino(Personaje):
    def __init__(self, vida, posicion, velocidad, cosecha):
        super().__init__(vida, posicion, velocidad)
        self.cosecha = cosecha

    def cosechar(self):
        print(f"El campesino cosechó {self.cosecha} unidades.")
        return self.cosecha


soldado = Soldado(100, 0, 5, 20)
campesino = Campesino(50, 10, 2, 15)

soldado.mover("derecha")
campesino.mover("izquierda")
soldado.atacar(campesino)
campesino.recibir_ataque(40)
campesino.cosechar()
