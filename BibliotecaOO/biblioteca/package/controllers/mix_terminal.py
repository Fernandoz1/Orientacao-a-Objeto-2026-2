class MixTerminal:
    """Mixin com funções de entrada de dados pelo terminal."""

    def ask(self, mensagem):

        return input(mensagem).strip()


    def ask_int(self, mensagem, padrao=0):

        valor = self.ask(mensagem)
        if valor.isdigit():
            return int(valor)
        print(f"Valor inválido, usando {padrao}.")
        return padrao
