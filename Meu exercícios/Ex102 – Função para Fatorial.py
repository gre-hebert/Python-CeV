def fatorial(valor, show=False):
    """
    CALCULADORA DE FATORIAL:
    valor = O valor que será calculado
    show = Se for "True" mostrará a resolução
    return = O resultado
    """
    if show == True:
        print(f'{valor}! = {valor}', end=" x ")
    for rep in range (valor - 1, 0, -1):
        if show == True and rep > 1:
            print(rep, end=' x ')
        elif show == True:
            print(rep, end=' = ')
        valor *= rep
    return valor



print(fatorial(5, True))
