from package.models.item import Item


class Livro(Item):

    def prazo_dias(self):

        return 14


    def multa_por_dia(self):

        return 0.5
