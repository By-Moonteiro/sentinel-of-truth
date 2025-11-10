from .display import Display
from src.utils.helpers import clear_screen

def main_menu() -> None:
    """Exibe o menu principal"""
    print("\n╔══════════════════════════════╗")
    print("║      SENTINEL OF TRUTH       ║")
    print("╠══════════════════════════════╣")
    print("║ 1 - Cadastrar uma notícia    ║")
    print("║ 2 - Consultar notícias       ║")
    print("║ 3 - Atualizar uma notícia    ║")
    print("║ 4 - Deletar uma notícia      ║")
    print("║ 5 - Gerar um relatório       ║")
    print("║ 6 - Encerar o programa       ║")
    print("╚══════════════════════════════╝")


def sub_menu() -> None:
    """Exibe o sub-menu"""
    print("\n╔═════════════════════════════════╗")
    print("║            CHECK NEWS           ║")
    print("╠═════════════════════════════════╣")
    print("║ 1 - Ver todas as notícias       ║")
    print("║ 2 - Ver notícias VERDADEIRAS    ║")
    print("║ 3 - Ver notícias FALSAS         ║")
    print("║ 4 - Ver notícias NÃO CHECADAS   ║")
    print("║ 5 - Retornar                    ║")
    print("╚═════════════════════════════════╝")

def sub_menu_options(sub_option: int) -> None:
    """
    Exibe opções do sub-menu

    Args:
        sub_option(int): Opção inserida pelo usuário

    Returns:
        None: Executa a opção desejada
    """
    # Instância
    display = Display()


    if sub_option == 1:  # <- Exibe todas as notícias
        display.display_all_news()
        display.wait_for_enter()  # <- Aguarda o usuário pressionar Enter p/ continuar
        clear_screen()

    elif sub_option == 2:
        display.display_news_by_status("NOTÍCIAS VERDADEIRAS", "Verdadeiro")
        display.wait_for_enter()
        clear_screen()

    elif sub_option == 3:  # <- Exibe somente as notícias Falsas
        display.display_news_by_status("NOTÍCIAS FALSAS", "Falso")
        display.wait_for_enter()
        clear_screen()

    elif sub_option == 4:
        display.display_news_by_status(
                "NOTÍCIAS NÃO CHECADAS", "não_checado"
                )
        display.wait_for_enter()
        clear_screen()

    elif sub_option == 5:  # <- Retorna pro Menu Principal
        clear_screen()    
