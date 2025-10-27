import json


def save_date(noticias: dict, dados: str) -> None:
    """
    Salva notícias em arquivo JSON

    Args:
        noticias(dict): Dicionário com as noticias
        dados(str): Caminho do arquivo pra salvar

    Returns:
        None: Salva com sucesso
    """
    try:
        with open(dados, "a", encoding="utf-8") as arquivo:  # Tenta escrever a notícia
            json.dump(noticias, arquivo, ensure_ascii=False, indent=2)

    except (
        PermissionError,
        FileNotFoundError,
    ):  # Caso nao consiga ele cria um arquivo para salvar as notícias novas
        print("Falha ao sobrescrever o arquivo salved_news.json..")
        with open("data/salved_news_backup", "w", encoding="utf-8") as backup:
            json.dump(noticias, backup, ensure_ascii=False, indent=2)

    except Exception as e:
        print(f"Erro inesperado: {e}")


def load_date(arquivo: str) -> dict:
    """
    Transforma o arquivo JSON para dicionario

    Args:
        arquivo(str): caminho do arquivo

    Returns:
        dict: Dicionário com as notícias
    """
    try:
        with open(arquivo, "r") as dados:
            noticias = json.load(dados)  # noqa: F841

    except (
        FileNotFoundError,
        json.JSONDecodeError,
    ):  # Caso o arquivo não exista/esteja corrompido
        print("Arquivo não encontrado. Criando novo:")
        return {}  # <- Cria um dicionario vazio


def update_date():
    pass


def generate_report():
    pass
