import sqlite3

from src.utils.config import DATA

class ManageNews:
    """
    Gerencia o ciclo completo das notícias.

    Responsável por cadastrar, buscar, atualizar e exibir noticias

    Attributes:
        news (dict): Dicionário no formato {id: [url, status]}
    """

    def __init__(self, data_path=DATA) -> None:
        """"
        Cria a tabela se não existir, sempre que iniciar
        """
        self.data_path = data_path
        self.create_table()

    def _conectar(self) -> None:
        """
        Método interno para:  
         - Conectar o Banco de Dados
        """
        return sqlite3.connect(self.data_path)
        

    def create_table(self) -> None:
        """Cria a tabela se não existir"""

        with self._conectar() as conn:
            cursor = conn.cursor() # <- Cria o cursor para gerenciar o BD
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS noticias (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    url TEXT NOT NULL,
                    status TEXT NOT NULL   
                        )
            """)


    def add_news(self, url: str, status: str) -> bool:
        """
        Adiciona uma nova notícia ao gerenciador.

        Args:
            noticia: Objeto News contendo a url e status

        Returns:
            None: Cria o dicionário com o ID atribuído á notícia
        """
        with self._conectar() as conn:
            cursor = conn.cursor
            
            cursor.execute(
                "INSERT INTO noticias (url, status) VALUES (?, ?)", (url, status)
                )
            return True
            
    def update_news(self, new_status: str, news_id: int) -> bool:
        """
        Atualiza os status de uma notícia existente.

        Returns:
            bool: True se atualizou, False se não atualizou
        """
        try:
            with self._conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE noticias SET status = ? WHERE id = ?", (new_status, news_id)
                    )
                
            return True
        
        except:
            print("deu erro boy")
            return False
        
    def delete_news(self, news_id: int) -> bool:
        
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM noticias WHERE id = ?", (news_id,)
                )


    def search_status_news(self, status: str) -> dict:
        """
        Busca todas as notícias com um status especifico.

        Args:
            status: Status para filtrar (ex: "Verdadeiro", ... , "Não Checado".)

        Returns:
            dict: Dicionário de Noticias com o status especifico
        """
        
        
        with self._conectar as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM noticias WHERE status = ?", (status,)
                )
            
            return cursor.fetchall()

    def load_news(self):


        with self._conectar() as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM noticias")

            return cursor.fetchall() # <- Retorna todas as notícias


