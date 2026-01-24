"""3) Botella y Sacacorchos
 Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
destapada.
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
sacacorchos ya contiene un corcho.
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
un corcho."""

class Corcho:
    def __init__(self, bodega):
        self.bodega = bodega

class Botella:
    def __init__(self, corcho=None):
        self.corcho = corcho

class Sacacorchos:
    def __init__(self):
        self.corcho = None

    def destapar(self, botella):
        if botella.corcho == None:
            print("La botella ya está destapada.")
            return False
        if self.corcho != None:
            print("El sacacorchos ya contiene un corcho.")
            return False

        self.corcho = botella.corcho
        botella.corcho = None
        print("Botella destapada con éxito.")
        return True

    def limpiar(self):
        if self.corcho == None:
            print("No hay corcho en el sacacorchos.")
            return False

        self.corcho = None
        print("Sacacorchos limpio.")
        return True