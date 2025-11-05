# --- Lógica principal ---
from src.logic.manager import ManageNews
from src.logic.report import ReportNews

# --- Utilitários gerais ---
from src.utils.json_handler import Handler
from src.utils.validation import menu_validation
from src.utils.config import clear_screen

# --- Interface e exibição ---
from src.utils.display import (
    display_all_news, 
    display_news_by_status, 
    wait_for_enter
)
from src.utils.menu import (
    display_main_menu, 
    display_sub_menu
)


def main() -> None:
    """Coordena todo o programa"""

    manager = ManageNews()  # <- instância
    running = True

    while running:
        display_main_menu() # <- Exibe o Menu principal

        option = input("➤ Escolha uma opção: ")
        option = menu_validation(option, 1, 5) # <- Valida somente as opções entre 1 e 5
        match option:
            case 1:
                manager.register_news() # <- Gerencia todo o registro das notícias

            case 2:
                clear_screen()
                display_sub_menu() # <- Exibe o Sub-menu

                sub_option = input("➤ Escolha uma opção: ")
                sub_option = menu_validation(sub_option, 1, 5)

                if sub_option == 1: # <- Exibe todas as notícias 
                    display_all_news(manager)
                    wait_for_enter() # <- Aguarda o usuário pressionar Enter p/ continuar

                elif sub_option == 2:                  
                    display_news_by_status(
                        manager, "NOTÍCIAS VERDADEIRAS", "Verdadeiro"
                        )
                    wait_for_enter()

                elif sub_option == 3: # <- Exibe somente as notícias Falsas
                    display_news_by_status(
                        manager, "NOTÍCIAS FALSAS", "Falso"
                        )
                    wait_for_enter()

                elif sub_option == 4:
                    display_news_by_status(
                        manager, "NOTÍCIAS NÃO CHECADAS", "não_checado"
                        )
                    wait_for_enter()

                elif sub_option == 5:  # <- Retorna pro Menu Principal  
                    clear_screen()
                    continue

            case 3:
                manager.update_news()  # <- Atualiza o status da notícia

            case 4:
                report = ReportNews()  # <- Instância
                report.report_generation() # Gera o relatório

            case 5:
                print("Encerrando o sistema..")
                running = False


if __name__ == "__main__":
    main()
