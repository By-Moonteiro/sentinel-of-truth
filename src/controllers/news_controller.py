from ..repository.abstract_repository import AbstractNewsRepository
from ..models.news import News
from src.ui.input_service import InputService


class NewsController:
    """
    Faz a interação do usuário (UI) com o repository (BD)

    Attributes:
        manager: Classe que interage com o BD
        in_service: Classe UI que pega e valida a entrada do usuário
    """
    def __init__(self, manager: AbstractNewsRepository, in_service: InputService):
        self.manager = manager
        self.input = in_service

    def register_news(self) -> bool:
        """
        Obtêm os dados da notícia do usuário e adiciona ela ao BD.

        Returns:
            bool: True se adicionou a notícia
        """

        url = self.input.input_url()
        status = self.input.input_status()

        news = News(url, status)

        success = self.manager.add_news(news)

        if success:
            print("Notícia salva com sucesso!")
            return True
        else:
            print("Erro! Não foi possível salvar a notícia.")
            return False

    def edit_news(self) -> bool:
        """
        Atualiza os status de uma notícia caso ela exista.

        Returns:
            bool: True se atualizou, False se não atualizou
        """
        news_id = self.input.input_news_id()

        news = self.manager.get_news_by_id(news_id)

        if not news:
            print("Nenhuma notícia encontrada com esse ID")
            return False

        new_status = self.input.input_status()
        self.manager.update_news(news_id, new_status)

        print(f"Status da notícia: {news[1]} atualizado")
        return True

    def remove_news(self) -> bool:
        """
        Obtêm o ID da notícia pelo usuário e apaga ela do BD.

        Returns:
            bool: True se removeu, False se não removeu a notícia do Banco de Dados
        """
        news_id = self.input.input_news_id()

        news = self.manager.get_news_by_id(news_id)

        if not news:
            print("Nenhuma notícia encontrada com esse ID")
            return False

        print(f"Id: {news[0]} | Url: {news[1]} | Status: {news[2]}")
        confirm = (
            input("Tem certeza que deseja deletar a notícia? (s/n): ").strip().lower()
        )

        if confirm == "s":
            self.manager.delete_news(news_id)
            print("Noticia deletada com sucesso")
            return True

        elif confirm == "n":
            print("Ação cancelada")
            return False

        else:
            print("Ação cancelada! Opção não encontrada, Tente refazer a operação.")
            return False
