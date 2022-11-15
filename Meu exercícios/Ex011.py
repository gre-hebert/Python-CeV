lar = float(input('Qual a largura da parede: '))
alt = float(input('Qual a altura da parede: '))
area = lar * alt
print('A area de sua parede é de {}m²\nE será necessário {} litros de tinta para pintá-la.'.format(area, (area/2)))
