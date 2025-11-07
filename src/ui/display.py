from ..utils.config import clear_screen


def display_all_news(manager) -> None:
    """Exibe todas as notícias"""

    clear_screen()
    print("=" * 60)
    print("{:^60}".format("TODAS AS NOTÍCIAS\n"))
    print("=" * 60)
    print("=" * 60)


def display_news_by_status(manager, title: str, status: str) -> None:
    """
    Exibe as notícias filtradas por status
    Função genérica para qualquer status

    Args:
        title(str): Titulo do cabeçalho formatado
        status(str): Status desejado para a exibição
    """
    clear_screen()
    print("=" * 60)
    print("{:^60}".format(f"{title}\n"))  # <- Cabeçalho
    print("=" * 60)
    news = manager.search_status_news(f"{status}")
    manager.display_news(news)  # <- Exibe as notícias por status
    print("=" * 60)



def display_news(self, noticias: dict) -> None:
        """
        Exibe cada notícia formatada.

        Args:
            noticias(dict): Dicionário de notícias para exibir

        Returns:
            None: Função apenas exibe output na tela
        """

        if not noticias:  # <- Caso não tenha notícias
            print("Não tem noticias para ser apresentada")
            return

        for id_news, news in noticias.items():
            print(f"ID: {id_news} | URL: {news[0]} | Status: {news[1]}\n")


def wait_for_enter() -> None:
    """Aguarda o usuário pressionar Enter para continuar"""
    input("\nPronto para voltar? (Enter)")
