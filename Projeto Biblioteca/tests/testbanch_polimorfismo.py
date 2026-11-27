from package.models.item import Item
from package.models.livro import Livro
from package.models.revista import Revista
from package.models.leitor import Leitor
from package.models.bibliotecario import Bibliotecario


def workspace():

    # Classe abstrata não pode ser instanciada
    try:
        Item("teste", "teste")
    except TypeError:
        print("Item é abstrata: não pode ser instanciada.")

    # Polimorfismo: o mesmo método, resultados diferentes por subclasse
    itens = [Livro("Dom Casmurro", "Machado de Assis"),
             Revista("Recreio", "Editora Abril")]

    for item in itens:
        print(f"{item.descricao()} -> prazo: {item.prazo_dias()} dias, "
              f"multa: R$ {item.multa_por_dia():.2f}/dia")

    # limite_emprestimos() existe só em Usuario; cada subclasse informa o valor
    usuarios = [Leitor("Manu"), Bibliotecario("Lucas")]

    for usuario in usuarios:
        print(f"{type(usuario).__name__} {usuario.nome} -> "
              f"limite: {usuario.limite_emprestimos()} itens")


if __name__ == "__main__":

    workspace()
