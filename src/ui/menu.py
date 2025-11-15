from .display import Display
from src.utils.helpers import clear_screen
from src.services import ReportService

class MenuController:
    """
    Controla o fluxo dos menus
    
    Attributes:
        controller: Classe que liga o UI com o BD
        input_service: Classe que lida com a interação com o usuário (UI)
        repository: Classe que gerencia o BD
    """
    def __init__(self, controller, input_service, repository):
        self.controller = controller
        self.in_service = input_service
        self.display = Display()
        self.report = ReportService(repository)

    def main_menu(self) -> None:
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


    def sub_menu(self) -> None:
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

        

    def sub_menu_options(self, sub_option: int) -> None:
        """
        Exibe opções do sub-menu

        Args:
            sub_option(int): Opção inserida pelo usuário

        Returns:
            None: Executa a opção desejada
        """
        # Instância


        if sub_option == 1:  # <- Exibe todas as notícias
            self.display.display_all_news()
            self.display.wait_for_enter()  # <- Aguarda o usuário pressionar Enter p/ continuar
            clear_screen()

        elif sub_option == 2:
            self.display.display_news_by_status("NOTÍCIAS VERDADEIRAS", "Verdadeiro")
            self.display.wait_for_enter()
            clear_screen()

        elif sub_option == 3:  # <- Exibe somente as notícias Falsas
            self.display.display_news_by_status("NOTÍCIAS FALSAS", "Falso")
            self.display.wait_for_enter()
            clear_screen()

        elif sub_option == 4:
            self.display.display_news_by_status(
                    "NOTÍCIAS NÃO CHECADAS", "não_checado"
                    )
            self.display.wait_for_enter()
            clear_screen()


    def run(self) -> None:
        """Roda todo o fluxo principal"""
        running = True

        while running:
            self.main_menu()
            option = self.in_service.input_option(1, 6)

            match option:
                case 1:
                    self.controller.register_news()

                case 2:
                    clear_screen()
                    sub_running = True
                    while sub_running:
                        self.sub_menu()
                        sub_option = self.in_service.input_option(1, 5)

                        if sub_option == 5:
                            clear_screen()
                            sub_running = False

                        else:
                            self.sub_menu_options(sub_option)

                case 3:
                    self.controller.edit_news()

                case 4:
                    self.controller.remove_news()

                case 5:
                    self.report.report_generation()

                case 6:
                    print("Encerrando o Sistema..")
                    running = False
