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

## 🏗️ Estrutura do Projeto

```
sentinel-of-truth/
│
├── main.py                 # Ponto de entrada do programa
├── requirements.txt        # Dependências do projeto (vazio)
├── README.md
├── .gitignore
│
├── data/                      # Dados salvos
│   ├── relatorio.txt          # <- relatório gerado      
│   └── salved_news.json       # <- Notícias salvas
│
├── src/
│   ├── __init__.py
│   ├── logic/               # Classes e lógica principal
│   │   ├── __init__.py
│   │   ├── manager.py
│   │   ├── report.py
│   │   └── news.py
│   └── utils/              # Funções auxiliares
│       ├── __init__.py
│       ├── config.py
│       ├── validation.py
│       └── json_handler.py
│
└── tests/                  # Testes automatizados
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

- [ ]  Adicionar mais requisitos
- [ ]  ...
- [ ]  ...
- [ ]  ...

## 🧩 O que aprendi

- [X] POO
- [X] Docstring
- [X] Manipulação de Arquivos .json | Geração de arquivos .txt
- [X] CRUD simples
- [X] Tipagem