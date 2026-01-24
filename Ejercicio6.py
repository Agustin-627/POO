"""6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del
usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno."""

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


usuario1 = Usuario("Ana", "Pérez", 28, "ana.perez@mail.com", "Buenos Aires")
usuario2 = Usuario("Luis", "Gómez", 35, "luis.gomez@mail.com", "Córdoba")
usuario3 = Usuario("María", "López", 22, "maria.lopez@mail.com", "Salta")

usuarios = [usuario1, usuario2, usuario3]

for u in usuarios:
    u.describir_usuario()
    u.saludar_usuario()
    print()
