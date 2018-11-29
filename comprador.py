#autoria Marconi Maia
class Comprador:
    def __init__(self,nome,cpf,idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade
    def get_cpf(self):
        return self.idade