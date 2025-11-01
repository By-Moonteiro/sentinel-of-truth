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

    return max_id + 1  # Retorna o maior id + 1


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
        self.news = {}

    def add_news(self, noticia: News) -> None:
        """
        Adiciona uma nova notícia ao gerenciador.

        Args:
            noticia: Objeto News contendo a url e status

        Returns:
            int: ID atribuído á notícia
        """
        next_id = id_generation(self.news)

        if not noticia:
            print("Você não adicionou uma notícia.")
            return

        self.news[next_id] = noticia
        print(f"Notícia gerada com o ID: {next_id}")

    def register_news(self) -> None:
        """
        Gerencia todo o registro.
        """

        loaded_news = Handler.load_date()  # Carrega os arquivos

        if loaded_news:  # Coloca as existentes no gerenciador
            self.news = loaded_news

        while True:
            url = input("URL: ").strip()
            if url:
                break
            print("A URL não pode estar vazia..")

        print("Status: [ 1 ] Verdadeiro | [ 2 ] Falso | [ 3 ] Não Checado")
        status = valid_status()

        news = News(url, status)
        news_to_list = news.to_list()  # Converte os atributos para lista
        self.add_news(news_to_list)  # Adiciona a lista à um dicionario

        Handler.save_date(self.news)

    def update_news(self) -> bool:
        """
        Atualiza os status de uma notícia existente.

        Returns:
            bool: True se atualizou, False se não atualizou
        """
        loaded_news = Handler.load_date()

        if not loaded_news:
            print("Não há notícia para ser alterada")
            return False

        while True:
            id_news = input("Digite o ID da notícia (ou '0' para cancelar): ").strip()

            if id_news == "0":
                return False

            elif id_news in loaded_news:
                news = loaded_news[id_news]

                print(f"O Status atual é: {news[1]}")
                new_status = valid_status()  # <- Pega o novo status
                news[1] = new_status
                print("Status Atualizado Com Sucesso!")

                Handler.save_date(loaded_news)

                return True

            else:
                print("ID não encontrado. Tente outro ID")

    def search_status_news(self, status: str) -> dict:
        """
        Busca todas as notícias com um status especifico.

        Args:
            status: Status para filtrar (ex: "Verdadeiro", ... , "Não Checado".)

        Returns:
            dict: Dicionário de Noticias com o status especifico
        """
        try:
            loaded_news = Handler.load_date()
            if not loaded_news:
                return {}

            filter_status = {}

            for id_news, news in loaded_news.items():
                if news[1] == status:
                    filter_status[id_news] = news

            return filter_status

        except Exception as e:
            print(f"Erro ao tentar buscar: {e}")
            return {}

    def display_news(self, noticias: dict) -> None:
        """
        Exibe cada notícia formatada.

        Args:
            noticias(dict): Dicionário de notícias para exibir

        Returns:
            None: Função apenas exibe output na tela
        """
        if not noticias:
            print("Não tem noticias para ser apresentada")
            return

        for id_news, news in noticias.items():
            print(f"ID: {id_news} | URL: {news[0]} | Status: {news[1]}\n")
