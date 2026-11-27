from package.models.usuario import Usuario


class Leitor(Usuario):

    def limite_emprestimos(self):

        return 2
