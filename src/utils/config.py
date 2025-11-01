import os
from pathlib import Path

# Caminhos para os arquivos
DATA = Path(__file__).parent.parent.parent / "data" / "saved_news.json"
DATA_BACKUP = Path(__file__).parent.parent.parent / "data" / "saved_news_backup.json"
REPORT = Path(__file__).parent.parent.parent / "data" / "relatorio.txt"

# Status
STATUS = {"1": "Verdadeiro", "2": "Falso", "3": "Não Checado"}


# Função para limpar o terminal
def clear_screen() -> None:
    """
    Limpa o terminal

    Returns:
        None: Caso seja windows usa o comando: "cls", caso seja outro: "clear"
    """
    os.system("cls" if os.name == "nt" else "clear")
