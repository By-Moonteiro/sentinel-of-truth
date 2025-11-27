# Sentinel of Truth

`projeto da faculdade` = `Concluído`

**Status:** `✅ Completo - Funcional`

**Descrição do Projeto/Problema:** É preciso construir um sistema simples, direto e eficiente para organizar o banco de dados
de notícias que serão analisadas por jornalistas. Precisam de um programa direto ao ponto, que
funcione no terminal, para cadastrar links, classificar o conteúdo e fazer buscas rápidas.
O mais importante: esse sistema precisa ser confiável. Nenhuma informação pode se perder, mesmo
que o programa seja fechado. Ao abrir novamente, tudo tem que estar lá, intacto.

## 📚 Sobre o projeto

Este projeto foi desenvolvido com o objetivo de **Cadastrar links, classificar o conteúdo e fazer buscas rápidas**.

Ele faz parte do meu aprendizado contínuo em **Python** e boas práticas de programação.

## 🧠 Tecnologias e Conceitos

- `Python 3.13.7`
- `Programação Orientada a Objetos (POO)`
- `Módulos e Pacotes`
- `Persistência de dados`
- `Estrutura de projeto modular`
- `SQLite`
- `ABC (Abstract Classes)`

## 🏗️ Estrutura do Projeto

```
sentinel-of-truth/
│
├── main.py                              # Ponto de entrada do programa
├── requirements.txt                     # Dependências do projeto (vazio)
├── README.md
├── .gitignore
│
├── data/                                # Arquivos persistidos (DB, relatórios)
│   ├── relatorio.txt
│   └── news.db
│
├── src/                                 # Código-fonte principal do sistema
│   ├── __init__.py
│   │
│   ├── controllers/                     # Orquestram o fluxo do programa; 
│   │   ├── __init__.py
│   │   └── news_controller.py
│   │
│   ├── models/                          # Modelos/Entidades que representam objetos do domínio
│   │   ├── __init__.py
│   │   └── news.py            
│   │
│   ├── repository/                      # Camada de  acesso a dados (CRUD no SQLite)
│   │   ├── __init__.py
│   │   ├── abstract_repository.py
│   │   └── sqlite_news_repository.py
│   │
│   ├── services/                        # Lógica de negócio independente de I/O
│   │   ├── __init__.py
│   │   ├── report_generator.py          # Geração e processamento de relatórios
│   │
│   ├── ui/                              # Interface do usuário (menus, input e exibição)
│   │   ├── __init__.py
│   │   ├── display.py
│   │   ├── input_service.py   
│   │   └── menu.py
│   │
│   └── utils/                           # Funções utilitárias e configurações gerais
│       ├── __init__.py
│       ├── config.py
│       └── helpers.py
│
└── tests/                               # Testes automatizados (vazio)
    └── test.py

```

## 🚀 Como Executar

```bash
# 1️⃣ Clone este repositório
git clone <https://github.com/By-Moonteiro/sentinel-of-truth.git>

# 2️⃣ Entre na pasta do projeto
cd sentinel-of-truth

# 4️⃣ Execute o projeto
python main.py

```

## 📈 Futuros Passos

- [ ]  ...
- [ ]  ...
- [ ]  ...
- [ ]  ...

## 🧩 O que aprendi

- [X] POO
- [X] Docstring
- [X] Manipulação de Arquivos .json | Geração de arquivos .txt
- [X] CRUD
- [X] Type hints
- [X] SQLite
- [X] ABC (Abstract Classes)
- [X] Princípios SOLID (S/O/D)
