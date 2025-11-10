# --- Lógica principal ---
from src.logic.manager import ManageNews
from src.logic.report import ReportNews

# --- Utilitários gerais ---
from src.utils.helpers import clear_screen

# --- Interface e exibição ---
from src.logic.services import InputService, NewsService
from src.ui.menu import main_menu, sub_menu, sub_menu_options


def main() -> None:
    """Coordena todo o programa"""

    # <- instâncias
    manager = ManageNews()
    in_service = InputService()
    service = NewsService(manager)

    running = True
    while running:
        main_menu()  # <- Exibe o Menu principal
        option = in_service.input_option(1, 6)

        match option:
            case 1:
                service.register_news()  # <- Gerencia todo o registro das notícias

            case 2:
                clear_screen()

                sub_menu()  # <- Exibe o Sub-menu
                sub_option = in_service.input_option(1, 5) # <- Obtêm a opção

                sub_menu_options(sub_option) # <- Exibe as opções do Sub-menu
                
            case 3:
                service.edit_news()  # <- Atualiza o status da notícia

            case 4:
                service.remove_news()  # <- Deleta uma notícia

            case 5:
                report = ReportNews(manager)  # <- Instância
                report.report_generation()  # Gera o relatório

            case 6:
                print("Encerrando o sistema..")
                running = False


if __name__ == "__main__":
    main()
