import json
import sqlite3

from .config import DATA, DATA_BACKUP


class Handler:
    """Gerencia o Banco de dados

        Attributes:
            data_path: Caminho do arquivo
    """
    def __init__(self, data_path=DATA) -> None:
        """"
        Cria a tabela sempre que iniciar
        """
        self.data_path = data_path
        self.create_table()

    def _conectar(self) -> None:
        """
        Conecta o Banco de Dados e cria o Cursor para gerencia-lo

        Returns:
            tuple: tupla contendo conexão com o banco e o cursor 
        """

        conn = sqlite3.connect(self.data_path) # <- Conecta com o BD
        return conn, conn.cursor() # <- Cria um cursor para manipular o Banco
        

    def create_table(self):
        """Cria a tabela se não existir"""
        conn, cursor = self._conectar()

        try:
            with conn:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS noticias (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        url TEXT NOT NULL,
                        status TEXT NOT NULL   
                            )
                """)

        finally: # <- Fecha o BD, independente se funcionou o try
            conn.close()


    def save_date(self, noticias: dict) -> None:
        """
        Salva notícias em arquivo JSON

        Args:
            noticias(dict): Dicionário com as noticias

        Returns:
            None: Salva com sucesso
        """

        try:  # Tenta escrever a notícia
            with open(DATA, "w", encoding="utf-8") as arquivo:
                json.dump(noticias, arquivo, ensure_ascii=False, indent=2)
            print("Salvo com sucesso!")

        # Caso não consiga ele cria um backup para salvar as notícias novas
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

    def load_date(self) -> dict:
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

        # Caso o arquivo não exista / esteja corrompido
        except (
            FileNotFoundError,
            json.JSONDecodeError,
        ):
            print("Arquivo vazio...")
            return {}  # <- retorna um dicionario vazio
