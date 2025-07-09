# 📚 Estudo OOP - Biblioteca

Este projeto é um exercício prático de Programação Orientada a Objetos (OOP) com Python. A proposta é desenvolver uma aplicação simples para gerenciar uma biblioteca, utilizando classes e organização em arquivos separados.

## 🧠 Objetivo

O objetivo principal é praticar a criação de classes, atributos, métodos e a separação do código em módulos organizados. A aplicação permite adicionar, remover, listar e buscar livros em uma biblioteca virtual.

## 🛠️ Estrutura do Projeto

O projeto é dividido em três arquivos principais:

- `livro.py`: Define a classe `Livro`, representando um livro com seus atributos.
- `biblioteca.py`: Define a classe `Biblioteca`, responsável por armazenar e gerenciar os livros.
- `main.py`: Script principal que utiliza as classes e executa operações básicas da biblioteca.

## 📦 Classes e Funcionalidades

### 📘 Classe `Livro`
A classe `Livro` possui os seguintes atributos:

- `titulo` (string)
- `autor` (string)
- `ano` (int)
- `isbn` (string)

Método especial:

- `__str__`: Retorna uma string formatada com as informações do livro.

### 🗃️ Classe `Biblioteca`
Responsável por gerenciar uma coleção de livros. Funcionalidades:

- Armazenamento de uma lista de objetos do tipo `Livro`
- `adicionar_livro(livro)`: Adiciona um novo livro à biblioteca
- `remover_livro(isbn)`: Remove um livro com base no ISBN
- `listar_livros()`: Lista todos os livros cadastrados
- `buscar_por_titulo(palavra)`: Busca livros que contenham a palavra informada no título

## 🧪 Testes e Uso

No arquivo `main.py` você pode:

- Criar livros e adicioná-los à biblioteca
- Listar todos os livros disponíveis
- Buscar livros por título
- Remover livros pelo ISBN
- 
   git clone https://github.com/mat2809/proj_biblioteca.git

  autor: Matheus Colaço
   
