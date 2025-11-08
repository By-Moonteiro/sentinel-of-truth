from .manager import ManageNews
from src.utils import menu_validation, valid_status


class InputService:
    """
    Obtêm os dados de input do usuário.
    """
    def input_option(self, start: int, end: int) -> int:
        """
        Obtêm o input do usuário e verifica se está no range válido.

        Returns:
            int: Opção válida
        """
        while True:
            opc = input("➤ Escolha uma opção: ").strip()
            valid_opc = menu_validation(opc, start, end)

            if valid_opc:
                return valid_opc

            print("\n╔══════════════════════════════════════════════════╗")
            print(f"➤ Opção inválida! Escolha uma opção entre {start} e {end}.")
            print("╚══════════════════════════════════════════════════╝")

    def input_status(self) -> bool:
        """
        Obtêm o input do usuário e verifica o status válido correspondente.

        Returns:
            bool: True se atualizou
        """
        valid = False
        while not valid:
            print("Status: [ 1 ]: Verdadeiro | [ 2 ]: Falso | [ 3 ]: Não Checado")
            status = input("➤Digite o Status desejado: ").strip()
            valid_stats = valid_status(status)

            if valid_stats:
                valid = True
                return valid_stats

            print("\n╔════════════════════════════════════════════════╗")
            print("➤ Opção inválida! Escolha uma opção Válida.      ")
            print("╚════════════════════════════════════════════════╝")

    def input_url(self):
        close = False
        while not close:
            url = input("➤Digite a Url desejada: ").strip()
            if url:
                close = True
                return url

            print("\n╔════════════════════════════════════════════════╗")
            print("➤ Esse campo não pode estar vazia..              ")
            print("╚════════════════════════════════════════════════╝")


class NewsService(InputService):
    def __init__(self, manager: ManageNews):
        self.manager = manager

    def register_news(self) -> None:
        """
        Obtêm os dados da notícia do usuário e adiciona ela ao BD.

        Returns:
            None: Adiciona a notícia
        """

        url = self.input_url()
        status = self.input_status()

        self.manager.add_news(url, status)
        return True

    def edit_news(self) -> bool:
        """
        Atualiza os status de uma notícia caso ela exista.

        Returns:
            bool: True se atualizou, False se não atualizou
        """

        try:
            news_id = int(input("➤Digite o ID desejado: ").strip())

        except ValueError:
            print("ID Inválido")
            return

        news = self.manager.get_news_by_id(news_id)

        if news:
            new_status = self.input_status()
            self.manager.update_news(news_id, new_status)
            print(f"Status da notícia: {news[1]} atualizado")
            return True

        else:
            print("Nenhuma notícia encontrada com esse ID")
            return False

    def remove_news(self) -> None:
        """
        Obtêm o ID da notícia pelo usuário e apaga ela do BD.

        Returns:
            None: Deleta a notícia do Banco de Dados
        """
        try:
            news_id = int(input("➤Digite o ID desejado: ").strip())

        except ValueError:
            print("ID Inválido")
            return

        news = self.manager.get_news_by_id(news_id)
        if not news:
            print("Nenhuma notícia encontrada com esse ID")
            return

        print(f"Id: {news[0]} | Url: {news[1]} | Status: {news[2]}")
        confirm = (
            input("Tem certeza que deseja deletar a notícia? (s/n): ").strip().lower()
        )

        if confirm == "s":
            self.manager.delete_news(news_id)
            print("Noticia deletada com sucesso")
        else:
            print("Ação cancelada")
