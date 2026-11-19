from app.Cadastro_Livro.Cadastro_livro import *
from app.Cadastro_Usuario.Cadastro_usuario import *

c1 = Livro(1, "Diário de um banana", "Matheus Silva", 2018, 275)
c1.informacao_livro()

c2 = Usuario(1, "Uanderson", 21, "uanderson@gmail.com", 17_98541.1253, "Rua bernadino gonçal")
c2.informacao_usuario()
