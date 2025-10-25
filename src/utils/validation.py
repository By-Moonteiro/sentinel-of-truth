def menu_validation(op: int):
    """
    Verifica:  
    - Se é inteiro  
    - Se não é um caractere  
    - Se esta entre 1 e 5  

    Retorna:
    - Opção Válida
    
    """
    valid = False
    while not valid:
        try:
            opc = int(op)
            
            if 1 <= opc <= 5:
                print("deu certo")
                valid = True
                return opc
                
            else:
                print("╔════════════════════════════════════════════════╗")
                print("➤ Opção inválida! Escolha uma opção entre 1 e 5.");
                print("╚════════════════════════════════════════════════╝")

        except ValueError:
            print("╔════════════════════════════════════════════════╗")
            print("➤ Opção inválida! Escolha uma opção entre 1 e 5.");
            print("╚════════════════════════════════════════════════╝")
        op = input("➤ Escolha uma opção: ")

