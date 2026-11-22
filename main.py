from app.Cadastro_Livro.Cadastro_livro import *
from app.Cadastro_Usuario.Cadastro_usuario import *
from app.Biblioteca.Biblioteca import *
from time import sleep


def main():
    while True:
        print("=" * 30)
        print("1 -Cadastro Livro")
        print("2 - Biblioteca")
        print("3 - Cadastro Usuario")
        print("4 - Emprestimo")
        print("5 - Sair")
        print("=" * 30)

        Escolha = input("Escolha uma opção: ")
        sleep(0.5)
        if Escolha == "5":
            break

        if Escolha == "1":
            print("==Você está cadastrando um livro==")

            while True:
                print("==========CADASTRO DE LIVRO==========")
                print("1 - Cadastrar um Livro: ")
                print("2 - Informações do Livro: ")
                print("3 - Disponibilidade do Livro: ")
                print("4 -Sair: ")

                op_interna = input("Escolha uma opção: ")

                if op_interna == "1":
                    print("\n==========CADASTRAR==========\n")
                    Titulo = input("Digite o Titulo: ")
                    Autor = input("Digite o Autor: ")
                    Ano = input("Digite o Ano: ")
                    Pg = input("Digite as Páginas: ")
                    Ide_input = input(
                        "ID (opcional - aperte enter para pular: )")

                    Ide = int(Ide_input) if Ide_input else None

                    livro = Livro(Titulo, Autor, Ano, Pg, Ide)
                    print("\n=====================================\n")

        elif Escolha == "2":
            print("==Você acessou a biblioteca==")
            while True:
                print("==========BIBLIOTECA==========")
                print("1 - Listar Livros: ")
                print("2 - Buscar Livros: ")
                print("3 -Sair: ")

                Escolha = input("Escolha uma opção: ")
                sleep(0.5)

                if Escolha == "3":
                    break


if __name__ == "__main__":
    main()
