from .config import STATUS


def menu_validation(opc: str, start: int, end: int) -> int:
    """
    Função genérica para validar a opção escolhida em menus interativos.

    Args:
       opc(str): Entrada do usuário.
       start(int): Começo do range desejado
       end(int): Fim do range desejado

    Returns:
        option(int): Opção válida convertida para inteiro.

    Examples:
        >>> menu_validation("1", 1, 5) 
        True  
        >>> menu_validation("6", 1, 5)
        False


    """
    valid = False
    while not valid:
        try:
            option = int(opc)

            if start <= option <= end:
                valid = True
                return option

            else:
                print("╔════════════════════════════════════════════════╗")
                print(f"➤ Opção inválida! Escolha uma opção entre {start} e {end}.")
                print("╚════════════════════════════════════════════════╝")

        except ValueError:
            print("╔════════════════════════════════════════════════╗")
            print(f"➤ Opção inválida! Escolha uma opção entre {start} e {end}.")
            print("╚════════════════════════════════════════════════╝")
        opc = input("➤ Escolha uma opção: ").strip()


def valid_status() -> str:
    """
    Solicita e valida o status do usuário

    Returns:
        status(str): status válido

    Examples:
        >>> status("1")
        Verdadeiro
        >>> status("2")
        Falso
    """
    while True:
        status = input("STATUS: ").strip()

        if status in ["1", "2", "3"]:
            return STATUS.get(status)

        print("Opção invalida! Digite 1, 2 ou 3\n")
