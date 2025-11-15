import sqlite3

from src.utils.config import DATA


class ManageNews:
    """
    Gerencia o gerenciamento completo das notícias.

    Responsável por: cadastrar, buscar, atualizar e deletar as notícias

    Attributes:
        data_path(str): Caminho do arquivo para a criação do BD
    """

    def __init__(self, data_path=DATA) -> None:
        """ "
        Cria a tabela se não existir, sempre que iniciar
        """
        self.data_path = data_path
        self.create_table()

    def news(self, url: str, status: str) -> None:
        """Cria o objeto da notícia"""
        self.url = url
        self.status = status


    def _conectar(self) -> None:
        """
        Método interno para: Conectar ao Banco de Dados
        """
        return sqlite3.connect(self.data_path)

    def create_table(self) -> None:
        """Cria a tabela se não existir"""

        try:
            with self._conectar() as conn:
                cursor = conn.cursor()  # <- Cria o cursor para gerenciar o BD
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS noticias (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        url TEXT NOT NULL,
                        status TEXT NOT NULL   
                            )
                """)

        except sqlite3.IntegrityError as e:  # <- Violação de integridade do BD
            print(f"Erro de integridade: {e}")

        except sqlite3.OperationalError as e:  # <- Problemas de operação
            print(f"Erro operacional: {e}")

        except sqlite3.DatabaseError as e:  # <- Erro interno do BD
            print(f"Erro geral no banco: {e}")
            raise

    def get_news_by_id(self, news_id: int) -> tuple[int, str, str] | None:
        """
        Procura uma notícia pelo ID.

        Args:
            news_id(int): ID da notícia

        Returns:
            result: Tupla com (id, url, status) se for encontrado
            ou None se não existir notícia com o ID informado
        """
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, url, status FROM noticias WHERE id = ?", (news_id,)
            )
            result = cursor.fetchone()

        return result  # <- Retorna None se não existir

    def add_news(self, url: str, status: str) -> bool:
        """
        Adiciona uma nova notícia ao banco de dados.

        Args:
            url(str): Url da notícia
            status(str): Status desejado para a respectiva notícia

        Returns:
            bool: Retorna True se adicionou ou False se não adicionou

        Examples:
            >>> add_news("www.YouTube.com", "Verdadeiro")
            True
            >>> add_news("www.GitHub.com", " ")
            False
        """
        try:
            with self._conectar() as conn:  # <- Abre, insere, faz o commit e fecha o BD
                cursor = conn.cursor()

                cursor.execute(
                    "INSERT INTO noticias (url, status) VALUES (?, ?)", (url, status)
                )
                return True

        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade: {e}")

        except sqlite3.OperationalError as e:
            print(f"Erro operacional: {e}")

        except sqlite3.DatabaseError as e:
            print(f"Erro geral no banco: {e}")

        return False

    def update_news(self, news_id: int, new_status: str) -> bool:
        """
        Atualiza os status de uma notícia existente.

        Args:
            news_id(int): ID da notícia que vai ser atualizada
            new_status(str): Novo status para a notícia

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

        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade: {e}")

        except sqlite3.OperationalError as e:
            print(f"Erro operacional: {e}")

        except sqlite3.DatabaseError as e:
            print(f"Erro geral no banco: {e}")

        return False

    def delete_news(self, news_id: int) -> bool:
        """
        Deleta uma notícia permanentemente caso ela exista.

        Args:
            news_id(int): ID da notícia

        Returns:
            bool: retorna True Caso tenha deletado com sucesso
        """
        try:
            with self._conectar() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM noticias WHERE id = ?", (news_id,))
                return True

        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade: {e}")

        except sqlite3.OperationalError as e:
            print(f"Erro operacional: {e}")

        except sqlite3.DatabaseError as e:
            print(f"Erro geral no banco: {e}")

        return False

    def search_status_news(self, status: str) -> list:
        """
        Busca todas as notícias com um status especifico.

        Args:
            status(str): Status para filtrar (ex: "Verdadeiro", ...)

        Returns:
            list: Lista de tuplas com respectivas informações.

        Examples:
            >>> search_status_news("Verdadeiro")
            [(1, "www.YouTube.com", "Verdadeiro"), (3, ...)]
        """

        try:
            with self._conectar() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM noticias WHERE status = ?", (status,))

                return cursor.fetchall()

        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade: {e}")

        except sqlite3.OperationalError as e:
            print(f"Erro operacional: {e}")

        except sqlite3.DatabaseError as e:
            print(f"Erro geral no banco: {e}")

        return []

    def load_news(self) -> list:
        """
        Obtêm todas as notícias.

        Returns:
            list: Lista de tuplas com todas as notícias.

        Examples:
            >>> load_news()
            [(1, "www.YouTube.com", "Verdadeiro"),
            (2, "www.python.org", "Não Checado"),
            (3, ...)]
        """
        try:
            with self._conectar() as conn:
                cursor = conn.cursor()

                cursor.execute("SELECT * FROM noticias")

                return cursor.fetchall()  # <- Retorna todas as notícias

        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade: {e}")

        except sqlite3.OperationalError as e:
            print(f"Erro operacional: {e}")

        except sqlite3.DatabaseError as e:
            print(f"Erro geral no banco: {e}")

        return []

    def qtd_news_register(self) -> int:
        """
        Obtêm o total de notícias cadastradas.

        Returns:
            int: Total de notícias.
        """
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM noticias")

            return cursor.fetchone()[0]

    def qtd_news_status_each(self, status: str) -> int:
        """
        Obtêm o total de notícias por status.

        Returns:
            int: Total de notícias de acordo com o status.
        """
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM noticias WHERE status = ?", (status,))
            return cursor.fetchone()[0]
        
    def percent_calculation(self) -> float:
        """
        Calcula a porcentagem de cada status em relação ao total.

        Returns:
            float: Porcentagem das notícias com status individualmente.
        """
        total = self.qtd_news_register()
        true_news = self.qtd_news_status_each("Verdadeiro")
        false_news = self.qtd_news_status_each("Falso")
        unverified_news = self.qtd_news_status_each("Não Checado")

        if total > 0:  # <- Evita divisão por 0
            percent_true = (true_news / total) * 100
            percent_false = (false_news / total) * 100
            percent_unverified = (unverified_news / total) * 100

        else:
            return 0.0, 0.0, 0.0

        return percent_true, percent_false, percent_unverified

