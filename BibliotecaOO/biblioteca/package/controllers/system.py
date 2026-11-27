from package.controllers.biblioteca import Biblioteca
from package.controllers.mix_terminal import MixTerminal
from package.models.leitor import Leitor
from package.models.bibliotecario import Bibliotecario


class System(MixTerminal):

    def __init__(self):

        self.__biblioteca = Biblioteca()

        # dicionário de usuários cadastrados (chave: nome)
        self.__usuarios = {}

        self.__running = True

        self.__options = {
            'cadastrar usuario': self.new_user,
            'cadastrar item': self.new_item,
            'listar acervo': self.list_items,
            'emprestar': self.lend,
            'devolver': self.give_back,
            'sair': self.exit
        }


    def find_user(self, nome):

        usuario = self.__usuarios.get(nome)
        if usuario is None:
            print(f"Usuário '{nome}' não cadastrado.")
        return usuario


    def new_user(self):

        nome = self.ask("Nome do usuário: ")
        tipo = self.ask("Tipo (leitor/bibliotecario): ").lower()

        if nome in self.__usuarios:
            print("Esse usuário já existe.")
        elif tipo == "leitor":
            self.__usuarios[nome] = Leitor(nome)
            print(f"Leitor {nome} cadastrado.")
        elif tipo == "bibliotecario":
            self.__usuarios[nome] = Bibliotecario(nome)
            print(f"Bibliotecário {nome} cadastrado.")
        else:
            print("Tipo inválido.")


    def new_item(self):

        nome = self.ask("Nome do bibliotecário: ")
        usuario = self.find_user(nome)

        if usuario is None:
            return
        if not isinstance(usuario, Bibliotecario):
            print("Apenas bibliotecários podem cadastrar itens.")
            return

        tipo = self.ask("Tipo (livro/revista): ").lower()
        titulo = self.ask("Título: ")
        autor = self.ask("Autor/Editora: ")
        usuario.cadastrar_item(self.__biblioteca, tipo, titulo, autor)


    def list_items(self):

        self.__biblioteca.listar_itens()


    def lend(self):

        nome = self.ask("Nome do usuário: ")
        usuario = self.find_user(nome)
        if usuario is None:
            return
        titulo = self.ask("Título do item: ")
        self.__biblioteca.emprestar(usuario, titulo)


    def give_back(self):

        nome = self.ask("Nome do usuário: ")
        usuario = self.find_user(nome)
        if usuario is None:
            return
        titulo = self.ask("Título do item: ")
        dias = self.ask_int("Dias de atraso (0 se não houve): ")
        self.__biblioteca.devolver(usuario, titulo, dias)


    def start(self):

        while self.__running:
            self.menu()

        self.shutdown()


    def menu(self):

        nomes = list(self.__options)

        print("\n=== Biblioteca Pública ===")
        for i, nome in enumerate(nomes, 1):
            print(f"  {i} - {nome}")

        escolha = self.ask("Escolha uma opção (número): ")

        if escolha.isdigit() and 1 <= int(escolha) <= len(nomes):
            self.__options[nomes[int(escolha) - 1]]()
        else:
            print("Opção inválida.")


    def exit(self):

        self.__running = False


    def shutdown(self):

        print("O sistema encerrou as suas atividades.")
