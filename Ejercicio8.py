""""8) Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings
con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta
clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use
el método para mostrar privilegios."""

class Usuario:
    def __init__(self, nombre, apellido, edad, correo, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.ciudad = ciudad

    def describir_usuario(self):
        print(f"Nombre completo: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Correo: {self.correo}")
        print(f"Ciudad: {self.ciudad}")

    def saludar_usuario(self):
        print(f"Hola {self.nombre}, bienvenido de nuevo.")


class Privilegios:
    def __init__(self, privilegios):
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        print("Privilegios del administrador:")
        for p in self.privilegios:
            print(f"- {p}")


class Admin(Usuario):
    def __init__(self, nombre, apellido, edad, correo, ciudad, privilegios):
        super().__init__(nombre, apellido, edad, correo, ciudad)
        self.privilegios = Privilegios(privilegios)


admin1 = Admin(
    "Laura",
    "Fernández",
    38,
    "laura.fernandez@mail.com",
    "Rosario",
    ["puede postear en el foro", "puede borrar un post", "puede banear usuario"]
)

admin1.describir_usuario()
admin1.saludar_usuario()
admin1.privilegios.mostrar_privilegios()