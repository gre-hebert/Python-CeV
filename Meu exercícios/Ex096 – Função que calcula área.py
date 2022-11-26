def terreno(lar, com):
    print(f'A área de um terreno {lar:.1f} x {com:.1f} é {lar * com:.1f}m²')

print(' Controle de Terrenos')
print('-' * 22)
terreno(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))