class Conta:

        def __init__(self, numero, titular, saldo, limite):
            print("Construindo objeto...{}".format(self))
            self.__numero = numero
            self.__titular = titular
            self.__saldo = saldo
            self.__limite = limite


        def extrato(self):
            print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

        def deposita(self, valor):
            self.__saldo += valor

        def saca(self, valor):
            if (valor <= (self.__saldo + self.limite)):
                self.__saldo -= valor
            else:
                print(" O valor {} passou o limite".format(valor))

        def transfere(self, valor, origem, destino):
            origem.saca(valor)
            destino.deposita(valor)

        @property
        def saldo(self):
            return self.__saldo

        @property
        def titular(self):
            return self.__titular

        @property
        def limite(self):
            return self.__limite

        @limite.setter
        def limite(self, valor_limite):
            self.__limite = valor_limite

        @staticmethod
        def codigo_banco():
            return "001"