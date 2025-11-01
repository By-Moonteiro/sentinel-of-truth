import os
from pathlib import Path

# Caminhos para os arquivos
DADOS = Path(__file__).parent.parent.parent / "data" / "saved_news.json"
DADOS_BACKUP = Path(__file__).parent.parent.parent / "data"
RELATORIO = Path(__file__).parent.parent.parent

# Status
STATUS = {"1": "Verdadeiro", "2": "Falso", "3": "Não Checado"}

# Função para limpar o terminal
def clear_screen():
    """
        Limpa o terminal

        Returns:
            SO (comando): Caso seja windows: "cls", caso seja outro: "clear"
    """
    os.system("cls" if os.name == "nt" else "clear")