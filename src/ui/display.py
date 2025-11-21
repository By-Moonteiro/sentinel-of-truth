from ..utils.helpers import clear_screen


class Display:
    """
    Responsável por exibir as notícias de forma organizada para o usuário.

    Attributes:
        repository: Classe que gerencia o BD
    """
    def __init__(self, repository):
        self.repository = repository

    def display_all_news(self) -> None:
        """Exibe todas as notícias gerais"""

        clear_screen()
        print("=" * 90)
        print("{:^90}".format("TODAS AS NOTÍCIAS\n"))

        all_news = self.repository.load_news()  # <- Carrega todas as notícias

        if not all_news:
            print("Nenhuma notícia cadastrada")
        else:
            for news_id, url, status in all_news:
                print(f"Id: {news_id} | Url: {url} | Status: {status}")

        print("=" * 90)

    def display_news_by_status(self, title: str, status: str) -> None:
        """
        Exibe as notícias filtradas por status
        Função genérica para qualquer status

        Args:
            title(str): Titulo do cabeçalho formatado
            status(str): Status desejado para a exibição
        """
        clear_screen()
        print("=" * 90)
        print("{:^90}".format(f"{title}\n"))  # <- Cabeçalho
        print("=" * 90)
        status_news = self.repository.search_status_news(status)

        if not status_news:
            print("Nenhuma notícia cadastrada")
        else:
            for news_id, url, status_value in status_news:
                print(f"Id: {news_id} | Url: {url} | Status: {status_value}")

        print("=" * 90)

    def wait_for_enter(self) -> None:
        """Aguarda o usuário pressionar Enter para continuar"""
        input("\nPronto para voltar? (Enter)")
