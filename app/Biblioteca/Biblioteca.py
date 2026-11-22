from app.Cadastro_Livro.Cadastro_livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []
        self.proximo_ID = 1

    def cadastrar_livro(self, titulo, autor, ano, pg):
        livro = Livro(self.proximo_ID, titulo, autor, ano, pg)
        self.livros.append(livro)
        self.proximo_ID += 1

    def listar_livros(self):
        for i in self.livros:
            print(f"Livros: ")

    def buscar_livros(self):
        pass 
