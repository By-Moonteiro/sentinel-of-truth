from .news import News


def id_generation(noticias: dict) -> int:
    """
    Gera um ID novo para a notícia.

    Args:
        noticias(dict): Dicionario de notícias

    Returns:
        int: ID + 1
    """
    if not noticias:  # Se o dicionário estiver vazio
        return 1

    return max(noticias.keys()) + 1  # Retorna o maior id + 1


class ManageNews:
    """
    Gerencia as notícias.

    Attributes:
        noticia (dict): Dicionário no formato {id: Notícia}
    """

    def __init__(self) -> None:
        """
        Inicializa um gerenciador de notícias vazio.
        """
        self.noticias = {}

    def add_news(self, noticia: News) -> int:
        """
        Adiciona uma nova notícia ao gerenciador.

        Args:
            noticia: Objeto News contendo a url e status

        Returns:
            int: ID atribuído á notícia
        """
        next_id = self.id_generation()
        self.noticias[next_id] = noticia

    def update_news(self, id_news: int, news_status: str) -> bool:
        """
        Atualiza os status de uma notícia existente.

        Args:
            id_news: ID da noticia que vai ser atualizada
            news_status: Novo status para a notícia

        Returns:
            bool: True se atualizou, False se a noticia nao existe
        """
        pass

    def search_status_news(self, status: str) -> list:
        """
        Busca todas as notícias com um status especifico.

        Args:
            status: Status para filtrar (ex: "Verdadeiro", "Falso")

        Returns:
            list: Lista de Noticias com o status especifico
        """
        pass
