class Terminal:
    """Funções de entrada de dados pelo terminal (métodos estáticos)."""

    @staticmethod
    def ask(mensagem):

        return input(mensagem).strip()


    @staticmethod
    def ask_int(mensagem, padrao=0):

        valor = Terminal.ask(mensagem)
        if valor.isdigit():
            return int(valor)
        print(f"Valor inválido, usando {padrao}.")
        return padrao
