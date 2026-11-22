class Usuario:
    def __init__(self, ide, nome, idade, email, telefone, endereco):
        self.id = ide
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def informacao_usuario(self):
        print("\n==========DADOS DO USUÁRIO==========")
        print(f"Id : {self.id}")
        print(f"Nome : {self.nome}")
        print(f"Idade : {self.idade}")
        print(f"E-mail : {self.email}")
        print(f"Telefone : {self.telefone}")
        print(f"Endereço : {self.endereco}")

    def consultar_emprestimo(self):
        pass