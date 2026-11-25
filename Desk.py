class Item:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def prazo_dias(self):
        return 7

    def multa_por_dia(self):
        return 1.0

    def descricao(self):
        return f"{self.titulo} - {self.autor}"


class Livro(Item):
    def prazo_dias(self):
        return 14

    def multa_por_dia(self):
        return 0.5


class Revista(Item):
    def prazo_dias(self):
        return 3

    def multa_por_dia(self):
        return 2.0

    def descricao(self):
        return f"[Revista] {super().descricao()}"


class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def limite_emprestimos(self):
        return 2


class Leitor(Usuario):
    def limite_emprestimos(self):
        return 2


class Bibliotecario(Usuario):
    def limite_emprestimos(self):
        return 5

    # Dependência: usa a Biblioteca só como parâmetro do método
    def cadastrar_item(self, biblioteca, tipo, titulo, autor):
        if tipo == "livro":
            biblioteca.cadastrar_livro(titulo, autor)
        elif tipo == "revista":
            biblioteca.cadastrar_revista(titulo, autor)
        else:
            print(f"Tipo '{tipo}' inválido.")


class Emprestimo:
    # Associação: liga um Usuario a um Item
    def __init__(self, usuario, item):
        self.usuario = usuario
        self.item = item


class Multa:
    # Dependência: só é usada dentro de um método da Biblioteca
    def calcular(self, item, dias_atraso):
        return dias_atraso * item.multa_por_dia()


class Biblioteca:
    def __init__(self):
        self.itens = []
        self.emprestimos = []

    # Composição: a Biblioteca cria os itens do próprio acervo
    def cadastrar_livro(self, titulo, autor):
        self.itens.append(Livro(titulo, autor))
        print(f"Livro cadastrado: {titulo}")

    def cadastrar_revista(self, titulo, autor):
        self.itens.append(Revista(titulo, autor))
        print(f"Revista cadastrada: {titulo}")

    def listar_itens(self):
        print("\n--- Acervo ---")
        for item in self.itens:
            situacao = "Disponível" if item.disponivel else "Emprestado"
            print(f"{item.descricao()} - {situacao}")
        print()

    def buscar_item(self, titulo):
        for item in self.itens:
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
        qtd = sum(1 for e in self.emprestimos if e.usuario == usuario)
        if qtd >= usuario.limite_emprestimos():
            print(f"{usuario.nome} atingiu o limite de {usuario.limite_emprestimos()} empréstimos.")
            return
        item.disponivel = False
        self.emprestimos.append(Emprestimo(usuario, item))
        print(f"{usuario.nome} pegou emprestado: {item.titulo} (prazo: {item.prazo_dias()} dias)")

    def devolver(self, usuario, titulo, dias_atraso=0):
        for emp in self.emprestimos:
            if emp.usuario == usuario and emp.item.titulo == titulo:
                emp.item.disponivel = True
                self.emprestimos.remove(emp)
                print(f"{usuario.nome} devolveu: {titulo}")
                if dias_atraso > 0:
                    valor = Multa().calcular(emp.item, dias_atraso)
                    print(f"Multa por {dias_atraso} dia(s) de atraso: R$ {valor:.2f}")
                return
        print(f"{usuario.nome} não possui o item '{titulo}'.")


# ---------- Teste de todas as funcionalidades ----------
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
biblioteca.emprestar(lucas, "Dom Casmurro")         # já emprestado
biblioteca.emprestar(manu, "Livro inexistente")     # não cadastrado

# 4. Limite do leitor (2)
biblioteca.emprestar(manu, "Percy Jackson")
biblioteca.emprestar(manu, "Superinteressante")     # passou do limite

# 5. Bibliotecário pega emprestado (limite maior)
biblioteca.emprestar(lucas, "Superinteressante")
biblioteca.emprestar(lucas, "Recreio")

biblioteca.listar_itens()

# 6. Devoluções (com e sem multa)
biblioteca.devolver(manu, "Dom Casmurro", dias_atraso=3)
biblioteca.devolver(lucas, "Recreio", dias_atraso=2)   # revista: multa maior
biblioteca.devolver(lucas, "Superinteressante")
biblioteca.devolver(manu, "Superinteressante")         # não possui

biblioteca.listar_itens()