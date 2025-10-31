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
        news_to_list = news.to_list() # Converte os atributos para lista
        manager.add_news(news_to_list) # Adiciona a lista à um dicionario
       
        Handler.save_date(manager.news)

    def update_news(self) -> bool:
        """
        Atualiza os status de uma notícia existente.

        Returns:
            bool: True se atualizou, False se não atualizou
        """
        loaded_news = Handler.load_date()

        while True:
            id_news = input("Digite o ID da notícia (ou '0' para cancelar): ")

            if id_news == "0":
                return False

            elif id_news in loaded_news:
                news = loaded_news[id]

                print(f"O Status atual é: {news[1]}")
                new_status = valid_status() # <- Pega o novo status
                news[1] = new_status
                print("Status Atualizado Com Sucesso!")

                Handler.save_date(loaded_news)

                return True
           
            else:
                print("ID não encontrado. Tente outro ID")
                    
                        

    def search_status_news(self, status: str) -> list:
        """
        Busca todas as notícias com um status especifico.

        Args:
            status: Status para filtrar (ex: "Verdadeiro", ... , "Não Checado".)

        Returns:
            list: Lista de Noticias com o status especifico
        """
        loaded_news = Handler.load_date()
        filter_status = []

        for id_news, news in loaded_news.items():
            if news[1] == status:
                filter_status.append({
                        "id": id_news,
                        "url": news[0],
                        "status": news[1]
                    })
        
        return filter_status
