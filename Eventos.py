import Boleteria
import streamlit as st

class GestorEventos:
    def __init__(self):
        self.eventos = []

    def agregar_evento(self, evento):
        self.eventos.append(evento)


class Evento:
    def __init__(self, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, aforo_total, precio_boleta , artistas):
        self.__nombre = nombre
        self.__fecha = fecha
        self.__hora_apertura = hora_apertura
        self.__hora_show = hora_show
        self.__lugar = lugar
        self.__direccion = direccion
        self.__ciudad = ciudad
        self.__precio_boleta = precio_boleta
        self.__aforo_total = aforo_total
        self.__estado = estado
        self.__artistas = artistas

    def __str__(self):
        return f"Nombre: {self.__nombre}\nFecha: {self.__fecha}\nHora de apertura: {self.__hora_apertura}\nHora de show: {self.__hora_show}\nLugar: {self.__lugar}\nDireccion: {self.__direccion}\nCiudad: {self.__ciudad}\nPrecios: {self.__precio_boleta}\nAforo total: {self.__aforo_total}\nEstado: {self.__estado}\nArtistas: {self.__artistas}"

    #Define getters y setters

    # Getters
    @property
    def nombre(self):
        return self.__nombre

    @property
    def fecha(self):
        return self.__fecha

    @property
    def hora_apertura(self):
        return self.__hora_apertura

    @property
    def hora_show(self):
        return self.__hora_show

    @property
    def lugar(self):
        return self.__lugar

    @property
    def direccion(self):
        return self.__direccion

    @property
    def ciudad(self):
        return self.__ciudad

    @property
    def precio_boleta(self):
        return self.__precio_boleta

    @property
    def aforo_total(self):
        return self.__aforo_total

    @property
    def estado(self):
        return self.__estado

    @property
    def artistas(self):
        return self.__artistas

    # Setters
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @hora_apertura.setter
    def hora_apertura(self, hora_apertura):
        self.__hora_apertura = hora_apertura

    @hora_show.setter
    def hora_show(self, hora_show):
        self.__hora_show = hora_show

    @lugar.setter
    def lugar(self, lugar):
        self.__lugar = lugar

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    @ciudad.setter
    def ciudad(self, ciudad):
        self.__ciudad = ciudad

    @precio_boleta.setter
    def precio_boleta(self, precio_boleta):
        self.__precio_boleta = precio_boleta

    @aforo_total.setter
    def aforo_total(self, aforo_total):
        self.__aforo_total = aforo_total

    @estado.setter
    def estado(self, estado):
        if self.__estado == "realizado":
            raise ValueError("No se puede cambiar el estado de un evento que ya ha sido realizado")
        self.__estado = estado


    @artistas.setter
    def artistas(self, artistas):
        self.__artistas = artistas

    #Metodos



    def agregar_artista(self, *artistas):
        for artista in artistas:
            self.__artistas.append(artista)

    def eliminar_artista(self, artista):
        if artista in self.__artistas:
            self.__artistas.remove(artista)
        else:
            print(f"{artista} no se encuentra en la lista de artistas")

    def agregar_precio_boleta(self, *precios_boleta):
        #st.write(f"Boletas actuales: {precios_boleta}")
        for precio_boleta in precios_boleta:
            self.__precio_boleta.append(precio_boleta)
        #st.write(f"Boletas actuales: {self.__precio_boleta}")






class EventoBar(Evento):
    def __init__(self, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, aforo_total,precio_boleta, artistas):
        super().__init__(nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, aforo_total,precio_boleta, artistas)



    # Metodos

    def calcular_ingresos(self):
        if self.precio_boleta2 == []:
            raise ValueError("No se encontraron  boletas para el evento")

        suma_precios = sum(precio.precio for precio in self.precio_boleta2)

        print(suma_precios)

        if suma_precios <= 0:
            raise ValueError("No se encontraron  boletas para el evento")


class EventoTeatro(Evento):
    def __init__(self, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, aforo_total,precio_boleta, artistas):
        super().__init__(nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, aforo_total,precio_boleta, artistas)

    # Metodos

    def calcular_ingresos(self):
        if self.precio_boleta2 == []:
            raise ValueError("No se encontraron  boletas para el evento")

        suma_precios = sum(precio.precio for precio in self.precio_boleta2)

        print(suma_precios)

        if suma_precios <= 0:
            raise ValueError("No se encontraron  boletas para el evento")


class EventoFilantropico(Evento):
    pass











# Evento1 = EventoBar("Concierto", "12/12/2021", "6:00 PM", "8:00 PM", "Estadio", "Calle 123", "Bogota", "realizado", 1000, [Boleteria.PrecioBoleta("VIP", "Preventa", 100000), Boleteria.PrecioBoleta("General", "Preventa", 50000)],"Alberto")
#
# #Evento2 = Evento("Festival", "12/12/2021", "6:00 PM", "8:00 PM", "Estadio", "Calle 123", "Bogota", "realizado", 1000, [Boleteria.PrecioBoleta("VIP", "Preventa", 100000), Boleteria.PrecioBoleta("General", "Preventa", 50000)])
#
# Evento1.calcular_ingresos()




