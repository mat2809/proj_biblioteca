from biblioteca import Biblioteca
from livro import Livro

def main():
    biblioteca = Biblioteca()

    # Criar alguns livros
    livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "1234567890")
    livro2 = Livro("Dom Quixote", "Miguel de Cervantes", 1605, "0987654321")
    livro3 = Livro("A Arte da Guerra", "Sun Tzu", -500, "1122334455")

    # Adicionar livros na biblioteca
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)

    # Listar todos os livros
    print("📚 Lista de livros:")
    for livro in biblioteca.listar_livros():
        print(livro)

    # Buscar livros que tenham 'Arte' no título
    print("\n🔍 Buscando livros com 'Arte' no título:")
    encontrados = biblioteca.buscar_livro("Arte")
    for livro in encontrados:
        print(livro)

    # Remover livro pelo ISBN
    isbn_remover = "0987654321"
    if biblioteca.remover_livro(isbn_remover):
        print(f"\n✅ Livro com ISBN {isbn_remover} removido!")
    else:
        print(f"\n❌ Livro com ISBN {isbn_remover} não encontrado!")

    # Listar livros atualizados
    print("\n📚 Lista de livros atualizada:")
    for livro in biblioteca.listar_livros():
        print(livro)

if __name__ == "__main__":
    main()