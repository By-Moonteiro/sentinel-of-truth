# --- Lógica principal ---
from src.repository.news_repository import NewsRepository

# --- Interface e exibição ---
from src.controllers import NewsController
from src.ui import MenuController, InputService


def main() -> None:
    """Coordena todo o programa"""

    # <- instâncias
    manager = NewsRepository()
    in_service = InputService()
    controller = NewsController(manager, in_service)

    # Exibição do programa
    menu = MenuController(controller, in_service, manager)
    menu.run()


if __name__ == "__main__":
    main()
