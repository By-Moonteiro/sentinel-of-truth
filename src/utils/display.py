from .config import clear_screen


def display_all_news(manager) -> None:
    """Exibe todas as notícias"""
    from .json_handler import Handler

    clear_screen()
    print("=" * 60)
    print("{:^60}".format("TODAS AS NOTÍCIAS\n"))
    print("=" * 60)
    handler = Handler()  # <- Instância
    noticias = handler.load_date()  # <- Carrega todas as notícias
    manager.display_news(noticias)  # <- Exibe as notícias organizadas
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


def wait_for_enter() -> None:
    """Aguarda o usuário pressionar Enter para continuar"""
    input("\nPronto para voltar? (Enter)")
