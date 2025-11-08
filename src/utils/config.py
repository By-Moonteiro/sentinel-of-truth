from pathlib import Path

# Caminhos para os arquivos

DATA = (  # <- Caminho pra Salvar as Notícias
    Path(__file__).parent.parent.parent / "data" / "news.db"
)

REPORT = (  # <- Caminho pro Relatório
    Path(__file__).parent.parent.parent / "data" / "relatorio.txt"
)


# Status
STATUS = {1: "Verdadeiro", 2: "Falso", 3: "Não Checado"}
