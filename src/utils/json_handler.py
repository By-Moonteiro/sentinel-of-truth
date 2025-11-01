import json

from .config import DATA, DATA_BACKUP


class Handler:
    def save_date(noticias: dict) -> None:
        """
        Salva notícias em arquivo JSON

        Args:
            noticias(dict): Dicionário com as noticias

        Returns:
            None: Salva com sucesso
        """
        try:
            with open(
                DATA, "w", encoding="utf-8"
            ) as arquivo:  # Tenta escrever a notícia
                json.dump(noticias, arquivo, ensure_ascii=False, indent=2)
            print("Salvo com sucesso!")

        # Caso nao consiga ele cria um arquivo para salvar as notícias novas
        except (
            PermissionError,
            FileNotFoundError,
        ):
            print("Falha ao sobrescrever o arquivo salved_news.json..")
            # Cria Backup
            with open(DATA_BACKUP, "w", encoding="utf-8") as backup:
                json.dump(noticias, backup, ensure_ascii=False, indent=2)

        except Exception as e:
            print(f"Erro inesperado: {e}")

    def load_date() -> dict:
        """
        Transforma o arquivo JSON para dicionario

        Args:
            arquivo(str): caminho do arquivo

        Returns:
            dict: Dicionário com as notícias
        """
        try:
            with open(DATA, "r", encoding="utf-8") as dados:
                return json.load(dados)

        # Caso o arquivo não exista/esteja corrompido
        except (
            FileNotFoundError,
            json.JSONDecodeError,
        ):
            print("Arquivo vazio...")
            return {}  # <- Cria um dicionario vazio
