from package.models.item import Item
from package.models.usuario import Usuario
from package.models.livro import Livro
from package.models.revista import Revista
from package.models.leitor import Leitor
from package.models.bibliotecario import Bibliotecario


def workspace():

    # Classes abstratas não podem ser instanciadas
    for classe in (Item, Usuario):
        try:
            classe("teste") if classe is Usuario else classe("teste", "teste")
        except TypeError:
            print(f"{classe.__name__} é abstrata: não pode ser instanciada.")

    itens = [Livro("Dom Casmurro", "Machado de Assis"),
             Revista("Recreio", "Editora Abril")]

    for item in itens:
        print(f"{item.descricao()} -> prazo: {item.prazo_dias()} dias, "
              f"multa: R$ {item.multa_por_dia():.2f}/dia")

    usuarios = [Leitor("Manu"), Bibliotecario("Lucas")]

    for usuario in usuarios:
        print(f"{type(usuario).__name__} {usuario.nome} -> "
              f"limite: {usuario.limite_emprestimos()} itens")


if __name__ == "__main__":

    workspace()
