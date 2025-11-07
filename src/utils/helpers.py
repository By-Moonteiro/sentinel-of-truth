import os

def clear_screen() -> None:
    """
    Limpa o terminal

    Returns:
        None: Caso seja windows usa o comando: "cls", caso seja outro: "clear"
    """
    os.system("cls" if os.name == "nt" else "clear")