# # MRO(Metodo de resolución de orden) es el orden en el que se resuelven los metodos en la herencia
# # print(EmpleadoArtista.mro()) <- Con esto puedo ver el orden en el que se resuelven los metodos en la herencia
#
# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
#
#     def mostrar_datos(self):
#         print("Nombre:", self.nombre)
#         print("Edad:", self.edad)
#
# class Estudiante(Persona):
#     def __init__(self, nombre, edad, grado):
#         super().__init__(nombre, edad)
#         self.grado = grado
#
#     def grado_mostrar(self):
#         print("El estudiante se encuentra en el grado: ", self.grado)
#
# Estudiante1 = Estudiante("Kevin", 15, "Noveno")
#
# Estudiante1.mostrar_datos()
# Estudiante1.grado_mostrar()


##Poliformismo El mismo metodo pero usado de manera distinta dependiendo de la clase


##Encapsulamiento es la capacidad de ocultar los datos de una clase y solo permitir el acceso a ellos a traves de metodos
##Setters y getters son metodos que permiten modificar y obtener los valores de los atributos de una clase
##Para hacer un atributo privado se debe poner un guion bajo antes del atributo _atributo
##Para hacer un atributo protegido se debe poner dos guiones bajos antes del atributo __atributo
##Para hacer un atributo publico no se pone nada
##Para hacer un metodo privado se debe poner un guion bajo antes del metodo _metodo
##Para hacer un metodo protegido se debe poner dos guiones bajos antes del metodo __metodo
##Para hacer un metodo publico no se pone nada
##Para hacer un metodo estatico se debe poner un decorador @staticmethod antes de la definicion del metodo
##Para hacer un metodo de clase se debe poner un decorador @classmethod antes de la definicion del metodo
##Para hacer un metodo de instancia no se pone nada
##Para hacer un metodo de instancia se debe poner un decorador @property antes de la definicion del metodo
##Para hacer un metodo de instancia se debe poner un decorador @metodo.setter antes de la definicion del metodo
##Para hacer un metodo de instancia se debe poner un decorador @metodo.deleter antes de la definicion del metodo
