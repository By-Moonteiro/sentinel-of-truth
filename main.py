# --- Biblioteca interna do python ---
import os

# --- Caminho do arquivo principal ---
from src.utils import DATA

# --- Lógica principal ---
from src.repository.news_repository import NewsRepository

# --- Interface e exibição ---
from src.controllers import NewsController
from src.ui import MenuController, InputService


def main() -> None:
    """Coordena todo o programa"""

    # Garante que a pasta 'data' exista
    data_direct = os.path.dirname(DATA)
    if not os.path.exists(data_direct):
        os.makedirs(data_direct) # <- Cria a pasta se ela não existir

    # instâncias
    manager = NewsRepository()
    in_service = InputService()
    controller = NewsController(manager, in_service)

    # Exibição do programa
    menu = MenuController(controller, in_service, manager)
    menu.run()


if __name__ == "__main__":
    main()
