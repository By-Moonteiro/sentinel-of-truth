from .config import STATUS


def menu_validation(opc: str, start: int, end: int) -> int:
    """
    Verifica se é uma opção válida e retorna como inteiro

    Args:
       op(str): Entrada do usuário.
       start

    Returns:
        int: Opção válida convertida para inteiro.

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
    """
    while True:
        status = input("STATUS: ").strip()

        if status in ["1", "2", "3"]:
            return STATUS.get(status)

        print("Opção invalida! Digite 1, 2 ou 3\n")
