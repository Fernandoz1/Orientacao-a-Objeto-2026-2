from abc import ABC, abstractmethod


class Item(ABC):
    """Classe abstrata: tudo o que a biblioteca empresta."""

    def __init__(self, titulo, autor):

        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = True


    @property
    def titulo(self):

        return self.__titulo


    @property
    def autor(self):

        return self.__autor


    @property
    def disponivel(self):

        return self.__disponivel


    @disponivel.setter
    def disponivel(self, valor):

        self.__disponivel = valor


    @abstractmethod
    def prazo_dias(self):
        pass


    @abstractmethod
    def multa_por_dia(self):
        pass


    def descricao(self):

        return f"{self.titulo} - {self.autor}"
