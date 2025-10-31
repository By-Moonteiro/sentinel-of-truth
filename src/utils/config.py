from pathlib import Path

# Caminhos para os arquivos
DADOS = Path(__file__).parent.parent.parent / "data" / "saved_news.json"
DADOS_BACKUP = Path(__file__).parent.parent.parent / "data"

# Status
STATUS = {"1": "Verdadeiro", "2": "Falso", "3": "Não Checado"}
