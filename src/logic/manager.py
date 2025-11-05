from src.utils.json_handler import Handler
from src.utils.validation import valid_status
from .news import News


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


handler = Handler()  # <- Instância


class ManageNews:
    """
    Gerencia o ciclo completo das notícias.

    Responsável por cadastrar, buscar, atualizar e exibir noticias

    Attributes:
        news (dict): Dicionário no formato {id: [url, status]}
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
            None: Cria o dicionário com o ID atribuído á notícia
        """
        next_id = id_generation(self.news)  # <- Gera um ID

        if not noticia:
            print("Você não adicionou uma notícia.")
            return

        self.news[next_id] = noticia  # <- Adiciona a notícia ao dicionário geral

        print(f"Notícia gerada com o ID: {next_id}")

    def register_news(self) -> None:
        """
        Gerencia todo o processo de registro e salva as notícias no Json.:
        """
        loaded_news = handler.load_date() # <- Carrega os arquivos

        if loaded_news: # <- Coloca as existentes no gerenciador
            self.news = loaded_news

        while True:
            url = input("URL: ").strip()

            # Se o usuário digitou algo, sai do loop
            if url:
                break

            print("A URL não pode estar vazia..")

        print("Status: [ 1 ] Verdadeiro | [ 2 ] Falso | [ 3 ] Não Checado")
        status = valid_status()

        news = News(url, status)
        news_to_list = news.to_list()  # Converte os atributos para lista
        self.add_news(news_to_list)  # Adiciona a lista à um dicionario

        handler.save_date(self.news)

    def update_news(self) -> bool:
        """
        Atualiza os status de uma notícia existente.

        Returns:
            bool: True se atualizou, False se não atualizou
        """
        loaded_news = handler.load_date()

        if not loaded_news:
            print("Não há notícia para ser alterada")
            return False

        while True:
            id_news = input("Digite o ID da notícia (ou '0' para cancelar): ").strip()

            if id_news == "0": # <- Cancela o looping
                return False

            if id_news in loaded_news: # <- Verifica o id é de uma notícia
                news = loaded_news[id_news]

                print(f"O Status atual é: {news[1]}")
                print("Status: [ 1 ] Verdadeiro | [ 2 ] Falso | [ 3 ] Não Checado")
                new_status = valid_status()  # <- Pega o novo status
                news[1] = new_status
                print("Status Atualizado Com Sucesso!")

                handler.save_date(loaded_news) # <- salva no JSON

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
            loaded_news = handler.load_date()

            if not loaded_news: # <- Caso não tenha notícias
                return {} # <- Retorna um dicionário vazio

            filter_status = {}

            for id_news, news in loaded_news.items():
                if news[1] == status:# <- filtra por status (news[1] = atributo: status)
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

        if not noticias: # <- Caso não tenha notícias
            print("Não tem noticias para ser apresentada")
            return

        for id_news, news in noticias.items():
            print(f"ID: {id_news} | URL: {news[0]} | Status: {news[1]}\n")
