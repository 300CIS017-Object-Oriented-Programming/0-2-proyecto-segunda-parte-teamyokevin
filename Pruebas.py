# class Celular:
#     def __init__(self, marca, modelo, camara):
#         self.marca = marca
#         self.modelo = modelo
#         self.camara = camara
#
#     def llamar(self):
#         print(self.marca, self.modelo, self.camara)
#
#     def cortar(self):
#         print(f'Cortaste la llamada desde tu: {self.modelo}')
#
# celular_1 = Celular("Apple", "15_Pro_max", "48MP")
# celular_1.llamar()
#
# # Nueva línea al final
#
# class Estudiante:
#     def __init__(self, nombre, edad, grado):
#         self.nombre = nombre
#         self.edad = edad
#         self.grado = grado
#
#     def estudiar(self):
#         print("El estudiante", self.nombre, "de grado", self.grado, "está estudiando")
#
# nombre = input("Ingrese su nombre: ")
# edad = input("Ingrese su edad: ")
# grado = input("Ingrese su grado: ")
#
# estudiante_1 = Estudiante(nombre, edad, grado)
# estudiante_1.estudiar()

# Herencia

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print("Mi habilidad es:",self.habilidad)

class EmpleadoArtista(Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        return f"{super().mostrar_habilidad()}" #Con super(). siempre accedo a la clase padre para hacer uso del metodo con self llamo a un metodo reescrito

roberto = EmpleadoArtista("Roberto",43,"Argentino", "Cantar", 100000,"ProgramadoresSA")

roberto.presentarse()

herencia = issubclass(EmpleadoArtista, Persona) #Como saber de que clase esta heredando EmpleadoArtista

instancia = isinstance(roberto, EmpleadoArtista)

print(instancia)

