from package.models.usuario import Usuario


class Leitor(Usuario):

    def __init__(self, nome):

        super().__init__(nome, limite=2)
