from package.models.usuario import Usuario


class Bibliotecario(Usuario):

    def __init__(self, nome):

        super().__init__(nome, limite=5)


    # Dependência: recebe a Biblioteca como parâmetro, sem guardá-la
    def cadastrar_item(self, biblioteca, tipo, titulo, autor):

        if tipo == "livro":
            biblioteca.cadastrar_livro(titulo, autor)
        elif tipo == "revista":
            biblioteca.cadastrar_revista(titulo, autor)
        else:
            print(f"Tipo '{tipo}' inválido.")
