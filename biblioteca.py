from livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []  # lista que vai guardar os livros

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                self.livros.remove(livro)
                return True
        return False

    def listar_livros(self):
        return self.livros

    def buscar_livro(self, termo_titulo):
        return [livro for livro in self.livros if termo_titulo.lower() in livro.titulo.lower()]
