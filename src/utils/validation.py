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
    try:
        option = int(opc)  # <- Converte a opção para int para verificar

        # Verifica no range se é uma opção válida
        if start <= option <= end:
            return option  # <- Retorna a opção válida

    except ValueError:
        return None  # <- Não é um número


def valid_status(status: int) -> str:
    """
    Solicita e valida o status do usuário

    Returns:
        status(str): status válido

    Examples:
        >>> status(1)
        Status: Verdadeiro
        >>> status(2)
        Status: Falso
        >>> status(4)
        Opção invalida
    """
    try:
        status = int(status)
        return STATUS.get(status)  # <- Retorna None se nao for válido

    except ValueError:
        return None
