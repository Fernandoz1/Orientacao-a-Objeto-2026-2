# Biblioteca Pública (POO em Python)

Sistema de biblioteca com herança, polimorfismo, composição, associação e
dependência, com menu interativo no terminal.

## Como rodar
    python main.py                              # menu interativo
    python -m tests.testbanch_biblioteca        # cenário completo de testes
    python -m tests.testbanch_polimorfismo      # polimorfismo e classes abstratas

## Estrutura
    main.py                 # ponto de entrada
    package/models/         # classes de domínio (uma por arquivo)
    package/controllers/    # regras de negócio e menu (Biblioteca, System, Terminal)
    tests/                  # testbanch_*.py
    docs/uml.mmd            # diagrama de classes (Mermaid)

## Relações (UML)
| Relação | Classes | Multiplicidade | Explicação |
|---|---|---|---|
| Herança | Livro, Revista -> Item; Leitor, Bibliotecario -> Usuario | - | subclasses reaproveitam e sobrescrevem a classe mãe (Item é abstrata; o limite de Usuario é definido só na classe mãe) |
| Composição | System -> Biblioteca, Usuario; Biblioteca -> Item, Emprestimo | 1 para 0..* | o todo cria e controla o ciclo de vida das partes |
| Associação | Emprestimo -> Usuario; Emprestimo -> Item | 0..* para 1; 0..1 para 1 | liga objetos que existem de forma independente |
| Dependência | System -> Terminal, Leitor, Bibliotecario; Biblioteca -> Multa, Livro, Revista; Bibliotecario -> Biblioteca | - | uso temporário, só dentro de um método (inclusive criar objetos) |
