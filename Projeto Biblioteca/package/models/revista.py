from package.models.item import Item


class Revista(Item):

    def prazo_dias(self):

        return 3


    def multa_por_dia(self):

        return 2.0


    def descricao(self):

        return f"[Revista] {super().descricao()}"
