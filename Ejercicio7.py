"""7) Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase
Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede
postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que
muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método."""

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


class Admin(Usuario):
    def __init__(self, nombre, apellido, edad, correo, ciudad, privilegios):
        super().__init__(nombre, apellido, edad, correo, ciudad)
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        print("Privilegios del administrador:")
        for p in self.privilegios:
            print(f"- {p}")


admin1 = Admin(
    "Carlos", 
    "Ramírez", 
    40, 
    "carlos.ramirez@mail.com", 
    "Buenos Aires", 
    ["puede postear en el foro", "puede borrar un post", "puede banear usuario"]
)

admin1.describir_usuario()
admin1.saludar_usuario()
admin1.mostrar_privilegios()