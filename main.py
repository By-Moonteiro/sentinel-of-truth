from src.core import Noticia
from src.utils import save_date, load_date, menu_validation

def main():
    running = True
    """Menu Principal"""
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
        menu_validation(option)



        match option:
            case 1:
                print("...")
        
            case 2:
                print("...")

            case 3:
                print("...")

            case 4:
                print("...")
        
            case 5:
                print("Encerrando o sistema..")
                running = False
