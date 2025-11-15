# --- Lógica principal ---
from src.repository.news_repository import NewsRepository
from src.services.report_generator import ReportService

# --- Utilitários gerais ---
from src.utils import clear_screen

# --- Interface e exibição ---
from src.controllers import NewsController
from src.ui import main_menu, sub_menu, sub_menu_options, InputService


def main() -> None:
    """Coordena todo o programa"""

    # <- instâncias
    manager = NewsRepository()
    in_service = InputService()
    service = NewsController(manager, in_service)

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
                report = ReportService(manager)  # <- Instância
                report.report_generation()  # Gera o relatório

            case 6:
                print("Encerrando o sistema..")
                running = False


if __name__ == "__main__":
    main()
