from src.utils import STATUS, MAX_URL_LENGTH


class InputService:
    """
    Obtêm os dados de input do usuário.
    """

    def analyze_int(self, value: str) -> int | None:
        """
        Verifica se o valor passado é inteiro e retorna ele convertido

        Args:
            value(str): Valor desejado para a verificação

        Returns:
            valor_inteiro(int): Valor inteiro | None: caso não seja número
        """
        try:
            int_value = int(value)
            return int_value

        except ValueError:
            return None

    def input_option(self, start: int, end: int) -> int:
        """
        Obtêm o input do usuário e verifica se está no range válido.

        Returns:
            int: Opção válida
        """

        while True:
            opc = input("➤ Escolha uma opção: ").strip()
            valid_opc = self.analyze_int(opc)

            if valid_opc is not None and start <= valid_opc <= end:
                return valid_opc

            print("╔══════════════════════════════════════════════════╗")
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
            status = input("➤ Digite o Status desejado: ").strip()
            valid_stats = self.analyze_int(status)

            if valid_stats in STATUS:
                valid = True
                return STATUS.get(valid_stats)

            print("╔════════════════════════════════════════════════╗")
            print("➤ Opção inválida! Escolha uma opção Válida.      ")
            print("╚════════════════════════════════════════════════╝")

    def input_url(self):
        
        close = False
        while not close:
            url = input("➤ Digite a Url desejada: ").strip()

            if  not url: # Caso o usuário não digite nada
                print("╔════════════════════════════════════════════════╗")
                print("➤ Esse campo não pode estar vazia..              ")
                print("╚════════════════════════════════════════════════╝")
                continue # Volta ao topo do loop
            
            if len(url) > MAX_URL_LENGTH: # Caso o usuário digite uma URL com + de 500 caracteres
                print("╔═════════════════════════════════════════════════════════════════════════════════╗")
                print(f"➤ URL muito longa! O limite máximo é de {MAX_URL_LENGTH} caracteres. Tente novamente.")
                print("╚═════════════════════════════════════════════════════════════════════════════════╝")
                continue 

            # Retorna a URL após passar pelas 2 verificações
            close = True
            return url

    def input_news_id(self) -> int:
        """Pede e valida um ID de notícia"""
        while True:
            news_id = input("➤ Digite o ID da notícia: ").strip()

            valid_id = self.analyze_int(news_id)

            if valid_id is not None and valid_id > 0:
                return int(news_id)

            print("ID Inválido.. Digite um numero inteiro positivo.")
