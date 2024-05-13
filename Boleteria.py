class PrecioBoleta:
    def __init__(self, categoria, fase_venta, precio, descuento):
        self.__categoria = categoria
        self.__fase_venta = fase_venta
        self.__precio = precio
        self.__descuento = descuento

    #Getters
    @property
    def categoria(self):
        return self.__categoria

    @property
    def fase_venta(self):
        return self.__fase_venta

    @property
    def precio(self):
        return self.__precio

    #Setters

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @fase_venta.setter
    def fase_venta(self, fase_venta):
        self.__fase_venta = fase_venta

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

class comprador:
    def __init__(self, nombre, apellido, edad, correo, telefono, direccion, ciudad, boletas):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__correo = correo
        self.__telefono = telefono
        self.__direccion = direccion
        self.__ciudad = ciudad
        self.__boletas = boletas

    #Getters
    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def edad(self):
        return self.__edad

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    @property
    def direccion(self):
        return self.__direccion

    @property
    def ciudad(self):
        return self.__ciudad

    @property
    def boletas(self):
        return self.__boletas

    #Setters

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    @correo.setter
    def correo(self, correo):
        self.__correo = correo

    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    @ciudad.setter
    def ciudad(self, ciudad):
        self.__ciudad = ciudad

    @boletas.setter
    def boletas(self, boletas):
        self.__boletas = boletas


class Patrocinador:
    pass

class Reportes:
    pass
