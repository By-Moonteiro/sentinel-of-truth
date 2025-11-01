from src.logic.manager import ManageNews
from src.utils.json_handler import Handler
from src.utils.validation import menu_validation
from src.logic.report import ReportNews
from src.utils.config import clear_screen


def main() -> None:
    """Menu Principal"""

    manager = ManageNews()  # <- instância

    running = True
    while running:
        print("\n╔══════════════════════════════╗")
        print("║      SENTINEL OF TRUTH       ║")
        print("╠══════════════════════════════╣")
        print("║ 1 - Cadastrar uma notícia    ║")
        print("║ 2 - Consultar notícias       ║")
        print("║ 3 - Atualizar uma notícia    ║")
        print("║ 4 - Gerar um relatório       ║")
        print("║ 5 - Encerar o programa       ║")
        print("╚══════════════════════════════╝")
        option = input("➤ Escolha uma opção: ")

        option = menu_validation(option, 1, 5)

        match option:
            case 1:
                manager.register_news()

            case 2:
                clear_screen()

                print("\n╔═════════════════════════════════╗")
                print("║            CHECK NEWS           ║")
                print("╠═════════════════════════════════╣")
                print("║ 1 - Ver todas as notícias       ║")
                print("║ 2 - Ver notícias VERDADEIRAS    ║")
                print("║ 3 - Ver notícias FALSAS         ║")
                print("║ 4 - Ver notícias NÃO CHECADAS   ║")
                print("║ 5 - Retornar                    ║")
                print("╚═════════════════════════════════╝")

                sub_option = input("➤ Escolha uma opção: ")
                sub_option = menu_validation(sub_option, 1, 5)

                if sub_option == 1:
                    clear_screen()
                    print("=" * 60)
                    print("{:^60}".format("TODAS AS NOTÍCIAS\n"))
                    print("=" * 60)
                    noticias = Handler.load_date()
                    manager.display_news(noticias)
                    print("=" * 60)
                    input("\nPronto para voltar? (Enter)")

                elif sub_option == 2:
                    clear_screen()
                    print("=" * 60)
                    print("{:^60}".format("NOTÍCIAS_VERDADEIRAS\n"))
                    print("=" * 60)
                    verdadeiras = manager.search_status_news("Verdadeiro")
                    manager.display_news(verdadeiras)
                    print("=" * 60)
                    input("\nPronto para voltar? (Enter)")

                elif sub_option == 3:
                    clear_screen()
                    print("=" * 60)
                    print("{:^60}".format("NOTÍCIAS_FALSAS\n"))
                    print("=" * 60)
                    falsas = manager.search_status_news("Falso")
                    manager.display_news(falsas)
                    print("=" * 60)
                    input("\nPronto para voltar? (Enter)")

                elif sub_option == 4:
                    clear_screen()
                    print("=" * 60)
                    print("{:^60}".format("NOTÍCIAS NÃO CHECADAS\n"))
                    print("=" * 60)
                    nao_checadas = manager.search_status_news("Não Checado")
                    manager.display_news(nao_checadas)
                    print("=" * 60)
                    input("\nPronto para voltar? (Enter)")

                elif sub_option == 5:
                    clear_screen()
                    continue

            case 3:
                manager.update_news()

            case 4:
                report = ReportNews()
                report.report_generation()

            case 5:
                print("Encerrando o sistema..")
                running = False


if __name__ == "__main__":
    main()
