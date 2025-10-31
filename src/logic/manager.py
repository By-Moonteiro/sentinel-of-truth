from .news import News
from src.utils.json_handler import Handler
from src.utils.validation import valid_status


def id_generation(news: dict) -> int:
    """
    Gera um ID novo para a notícia.

    Args:
        news(dict): Dicionario de notícias

    Returns:
        int: ID + 1
    """
    if not news:  # Se o dicionário estiver vazio
        return 1

    max_id = 0
    for key in news.keys():
        int_key = int(key)
        if int_key > max_id:
            max_id = int_key
            
    return max_id + 1 # Retorna o maior id + 1


class ManageNews:
    """
    Gerencia as notícias.

    Attributes:
        noticia (dict): Dicionário no formato {id: Notícia}
    """

    def __init__(self) -> dict:
        """
        Inicializa um gerenciador de notícias vazio.
        """
        self.news = {}

    def add_news(self, noticia: News) -> dict:
        """
        Adiciona uma nova notícia ao gerenciador.

        Args:
            noticia: Objeto News contendo a url e status

        Returns:
            int: ID atribuído á notícia
        """

        next_id = id_generation(self.news)
        self.news[next_id] = noticia


    def register_news() -> None:
        """
        Gerencia todo o registro.
        """

        manager = ManageNews()
        loaded_news = Handler.load_date() # Carrega os arquivos

        if loaded_news: # Coloca as existentes no gerenciador
            manager.news = loaded_news


        url = input("URL: ")
        print("Status: [ 1 ] Verdadeiro | [ 2 ] Falso | [ 3 ] Não Checado")
        status = valid_status()


        news = News(url, status)
        news_to_list = news.to_list() # Converte para lista
        manager.add_news(news_to_list)
       
        Handler.save_date(manager.news)

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
