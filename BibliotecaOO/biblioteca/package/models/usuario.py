from abc import ABC, abstractmethod


class Usuario(ABC):
    """Classe abstrata: pessoas que usam a biblioteca."""

    def __init__(self, nome):

        self.__nome = nome


    @property
    def nome(self):

        return self.__nome


    @abstractmethod
    def limite_emprestimos(self):
        pass
