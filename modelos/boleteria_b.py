
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
    def __init__(self, nombre, apellido, edad, correo, telefono, direccion, boletas, numero_boletas_compradas, total_compra):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__correo = correo
        self.__telefono = telefono
        self.__direccion = direccion
        self.__boletas = boletas
        self.__numero_boletas_compradas = numero_boletas_compradas
        self.__total_compra = total_compra

    def __str__(self):
        return f"Comprador: {self.__nombre} {self.__apellido}, Edad: {self.__edad}, Correo: {self.__correo}, Telefono: {self.__telefono}, Direccion: {self.__direccion}, Boletas: {self.__boletas}, Numero de boletas compradas: {self.__numero_boletas_compradas}, Total de la compra: {self.__total_compra}"

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
    def boletas(self):
        return self.__boletas

    @property
    def numero_boletas_compradas(self):
        return self.__numero_boletas_compradas


    @property
    def total_compra(self):
        return self.__total_compra

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



    @boletas.setter
    def boletas(self, boletas):
        self.__boletas = boletas

    @numero_boletas_compradas.setter
    def numero_boletas_compradas(self, numero_boletas_compradas):
        self.__numero_boletas_compradas = numero_boletas_compradas

    @total_compra.setter
    def total_compra(self, total_compra):
        self.__total_compra = total_compra


class Patrocinador:
    def __init__(self,nombre,valor_aportado):
        self.__nombre = nombre
        self.__valor_aportado = valor_aportado

    #Getters
    @property
    def nombre(self):
        return self.__nombre

    @property
    def valor_aportado(self):
        return self.__valor_aportado

    #Setters

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @valor_aportado.setter
    def valor_aportado(self,valor_aportado):
        self.__valor_aportado = valor_aportado

class ReporteVenta:
    def __init__(self, boletas_vendidas_vip, boletas_vendidas_intermedio, boletas_vendidas_general, ventas, total_ventas_regular,total_ventas_preventa):
        self.__boletas_vendidas_vip = boletas_vendidas_vip
        self.__boletas_vendidas_intermedio = boletas_vendidas_intermedio
        self.__boletas_vendidas_general = boletas_vendidas_general
        self.__ventas = ventas
        self.__total_ventas_preventa = total_ventas_preventa
        self.__total_venta_regular = total_ventas_regular

    def __str__(self):
        return f"Boletas vendidas VIP: {self.__boletas_vendidas_vip}, Boletas vendidas Intermedio: {self.__boletas_vendidas_intermedio}, Boletas vendidas General: {self.__boletas_vendidas_general}, Ventas: {self.__ventas}, Total de ventas preventa: {self.__total_ventas_preventa}, Total de ventas regular: {self.__total_venta_regular}"


class ReporteFinanciero:
    def __init__(self, compradores, patrocinadores, reporte_venta):
        self.__compradores = compradores
        self.__patrocinadores = patrocinadores
        self.__reporte_venta = reporte_venta



