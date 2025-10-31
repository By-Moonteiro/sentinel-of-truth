from src.logic.manager import ManageNews
from src.utils.json_handler import Handler
from src.utils.validation import menu_validation


def main() -> None:
    """Menu Principal"""
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
                ManageNews.register_news()

            case 2:
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
                    noticias = Handler.load_date()

                elif sub_option == 2:
                    ManageNews.search_status_news("Verdadeiro")

                elif sub_option == 3:
                    ManageNews.search_status_news("Falso")

                elif sub_option == 4:
                    ManageNews.search_status_news("Não Checado")

                elif sub_option == 5:
                    continue

            case 3:
                ManageNews.update_news()

            case 4:
                print("...")

            case 5:
                print("Encerrando o sistema..")
                running = False


if __name__ == "__main__":
    main()
