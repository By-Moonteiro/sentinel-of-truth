from .manager import ManageNews
from src.utils import menu_validation, valid_status

class InputService:

    def input_option(self, start: int, end: int) -> int:
        while True:
            opc = input("➤ Escolha uma opção: ").strip()
            valid_opc = menu_validation(opc, start, end)

            if valid_opc:
                return valid_opc
            
            print("\n╔══════════════════════════════════════════════════╗")
            print(f"➤ Opção inválida! Escolha uma opção entre {start} e {end}.")
            print("╚══════════════════════════════════════════════════╝")
            

    def input_status(self):
        
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



class NewsService:
    pass