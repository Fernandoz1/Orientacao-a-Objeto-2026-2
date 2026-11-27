class Multa:

    @staticmethod
    def calcular(item, dias_atraso):

        return dias_atraso * item.multa_por_dia()
