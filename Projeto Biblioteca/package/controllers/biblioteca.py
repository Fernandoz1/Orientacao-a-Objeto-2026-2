from package.models.livro import Livro
from package.models.revista import Revista
from package.models.emprestimo import Emprestimo
from package.models.multa import Multa


class Biblioteca:

    def __init__(self):

        self.__itens = []
        self.__emprestimos = []


    # Composição: a Biblioteca cria os itens do próprio acervo
    def cadastrar_livro(self, titulo, autor):

        self.__itens.append(Livro(titulo, autor))
        print(f"Livro cadastrado: {titulo}")


    def cadastrar_revista(self, titulo, autor):

        self.__itens.append(Revista(titulo, autor))
        print(f"Revista cadastrada: {titulo}")


    def listar_itens(self):

        print("\n--- Acervo ---")
        if not self.__itens:
            print("(acervo vazio)")
        for item in self.__itens:
            situacao = "Disponível" if item.disponivel else "Emprestado"
            print(f"{item.descricao()} - {situacao}")
        print()


    def buscar_item(self, titulo):

        for item in self.__itens:
            if item.titulo == titulo:
                return item
        return None


    def emprestar(self, usuario, titulo):

        item = self.buscar_item(titulo)

        if item is None:
            print(f"O item '{titulo}' não está cadastrado.")
            return
        if not item.disponivel:
            print(f"{item.titulo} já está emprestado.")
            return

        qtd = sum(1 for e in self.__emprestimos if e.usuario == usuario)
        if qtd >= usuario.limite_emprestimos():
            print(f"{usuario.nome} atingiu o limite de {usuario.limite_emprestimos()} empréstimos.")
            return

        item.disponivel = False
        # Composição: a Biblioteca cria e guarda o Emprestimo
        self.__emprestimos.append(Emprestimo(usuario, item))
        print(f"{usuario.nome} pegou emprestado: {item.titulo} (prazo: {item.prazo_dias()} dias)")


    def devolver(self, usuario, titulo, dias_atraso=0):

        for emp in self.__emprestimos:
            if emp.usuario == usuario and emp.item.titulo == titulo:
                emp.item.disponivel = True
                self.__emprestimos.remove(emp)
                print(f"{usuario.nome} devolveu: {titulo}")
                if dias_atraso > 0:
                    # Dependência: Multa é usada apenas dentro deste método
                    valor = Multa.calcular(emp.item, dias_atraso)
                    print(f"Multa por {dias_atraso} dia(s) de atraso: R$ {valor:.2f}")
                return

        print(f"{usuario.nome} não possui o item '{titulo}'.")
