class Emprestimo:
    """Associação: liga um Usuario a um Item (empréstimo ativo)."""

    def __init__(self, usuario, item):

        self.__usuario = usuario
        self.__item = item


    @property
    def usuario(self):

        return self.__usuario


    @property
    def item(self):

        return self.__item
