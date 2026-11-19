class Livro:
    def __init__(self, ide, titulo, autor, ano, pg):
        self.id = ide
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.paginas = pg
        self.disponibilidade = True

    # O "bool" ele serve para avisar que este método vai devolver um valor booleano (True ou False)
    def consul_disponi(self) -> bool:
        return self.disponibilidade

    def informacao_livro(self):
        print(f"Id : {self.id}")
        print(f"Nome : {self.titulo}")
        print(f"Autor : {self.autor}")
        print(f"Ano : {self.ano}")
        print(f"Páginas : {self.paginas}")
