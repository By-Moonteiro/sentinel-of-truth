# --- Lógica principal ---
from src.logic.manager import ManageNews
from src.logic.report import ReportNews

# --- Utilitários gerais ---
from src.utils.helpers import clear_screen

# --- Interface e exibição ---
from src.logic.services import InputService, NewsService
from src.ui.display import Display
from src.ui.menu import display_main_menu, display_sub_menu


def main() -> None:
    """Coordena todo o programa"""

    # <- instâncias
    manager = ManageNews()
    in_service = InputService()
    service = NewsService(manager)
    display = Display()


    running = True
    while running:
        display_main_menu()  # <- Exibe o Menu principal
        option = in_service.input_option(1, 6)

        match option:
            case 1:
                service.register_news()  # <- Gerencia todo o registro das notícias

            case 2:
                clear_screen()
                display_sub_menu()  # <- Exibe o Sub-menu
                sub_option = in_service.input_option(1, 5)

                if sub_option == 1:  # <- Exibe todas as notícias
                    display.display_all_news()
                    display.wait_for_enter()  # <- Aguarda o usuário pressionar Enter p/ continuar
                    clear_screen()

                elif sub_option == 2:
                    display.display_news_by_status(
                        "NOTÍCIAS VERDADEIRAS", "Verdadeiro"
                    )
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
                    continue

            case 3:
                service.edit_news()  # <- Atualiza o status da notícia

            case 4:
                service.remove_news() # <- Deleta uma notícia

            case 5:
                report = ReportNews(manager)  # <- Instância
                report.report_generation()  # Gera o relatório

            case 6:
                print("Encerrando o sistema..")
                running = False


if __name__ == "__main__":
    main()
