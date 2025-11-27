from abc import ABC, abstractmethod

from src.models import News


class AbstractNewsRepository(ABC):

    @abstractmethod
    def add_news(self, news: News) -> None:
        """
        Adiciona uma notícia ao repositório.

        Args:
            news: Objeto contendo os dados da notícia
        """
        pass


    @abstractmethod
    def get_news_by_id(self, news_id: int) -> tuple[int, str, str] | None:
        """
        Procura uma notícia pelo ID.

        Args:
            news_id(int): ID da notícia
        """
        pass


    @abstractmethod
    def update_news(self, news_id: int, new_status: str) -> bool:
        """
        Atualiza os status de uma notícia existente.

        Args:
            news_id(int): ID da notícia que vai ser atualizada
            new_status(str): Novo status para a notícia  
        """
        pass


    @abstractmethod
    def delete_news(self, news_id: int) -> bool:
        """
        Deleta uma notícia permanentemente caso ela exista.

        Args:
            news_id(int): ID da notícia
        """
        pass


    @abstractmethod
    def search_status_news(self, status: str) -> list:
        """
        Busca todas as notícias com um status especifico.

        Args:
            status(str): Status para filtrar (ex: "Verdadeiro", ...)
        """
        pass


    @abstractmethod
    def load_news(self) -> list:
        """
        Obtêm todas as notícias.
        """
        pass


    @abstractmethod
    def qtd_news_register(self) -> int:
        """
        Obtêm o total de notícias cadastradas.
        """
        pass


    @abstractmethod
    def qtd_news_status_each(self, status: str) -> int:
        """
        Obtêm o total de notícias por status.
        """
        pass
