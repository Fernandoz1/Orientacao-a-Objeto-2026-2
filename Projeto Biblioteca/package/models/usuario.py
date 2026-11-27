class Usuario:
    """Classe mãe das pessoas que usam a biblioteca.

    O limite de empréstimos é definido apenas aqui; cada subclasse
    informa o seu valor ao chamar super().__init__.
    """

    def __init__(self, nome, limite=2):

        self.__nome = nome
        self.__limite = limite


    @property
    def nome(self):

        return self.__nome


    def limite_emprestimos(self):

        return self.__limite
