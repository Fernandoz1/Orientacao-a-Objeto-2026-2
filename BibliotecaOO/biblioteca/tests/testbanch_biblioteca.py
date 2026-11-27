from package.controllers.biblioteca import Biblioteca
from package.models.leitor import Leitor
from package.models.bibliotecario import Bibliotecario


def workspace():

    biblioteca = Biblioteca()

    manu = Leitor("Manu")
    lucas = Bibliotecario("Lucas")

    # 1. Bibliotecário cadastra itens
    lucas.cadastrar_item(biblioteca, "livro", "Dom Casmurro", "Machado de Assis")
    lucas.cadastrar_item(biblioteca, "livro", "Percy Jackson", "Rick Riordan")
    lucas.cadastrar_item(biblioteca, "revista", "Superinteressante", "Editora Abril")
    lucas.cadastrar_item(biblioteca, "revista", "Recreio", "Editora Abril")

    # 2. Listar acervo
    biblioteca.listar_itens()

    # 3. Empréstimos (sucesso, já emprestado, inexistente)
    biblioteca.emprestar(manu, "Dom Casmurro")
    biblioteca.emprestar(lucas, "Dom Casmurro")
    biblioteca.emprestar(manu, "Livro inexistente")

    # 4. Limite do leitor (2)
    biblioteca.emprestar(manu, "Percy Jackson")
    biblioteca.emprestar(manu, "Superinteressante")

    # 5. Bibliotecário pega emprestado (limite maior)
    biblioteca.emprestar(lucas, "Superinteressante")
    biblioteca.emprestar(lucas, "Recreio")

    biblioteca.listar_itens()

    # 6. Devoluções (com e sem multa)
    biblioteca.devolver(manu, "Dom Casmurro", dias_atraso=3)
    biblioteca.devolver(lucas, "Recreio", dias_atraso=2)
    biblioteca.devolver(lucas, "Superinteressante")
    biblioteca.devolver(manu, "Superinteressante")

    biblioteca.listar_itens()


if __name__ == "__main__":

    workspace()
