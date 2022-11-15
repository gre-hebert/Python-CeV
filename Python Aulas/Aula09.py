frase = ' Curso em Vídeo Python   '
print(frase) #r
print(frase[3]) #rdo em Víd
print(frase[3:13]) # Curso em Vid
print(frase[:13]) #eo Python
print(frase[13:]) #Croe íe
print(frase[1:15:2]) #Croe íe yhn
print(frase[1::2]) #us mVdoPto
print(frase[::2]) # us mVdoPto
print(frase.count('o')) #3
print(frase.count('O')) #0
print(frase.upper().count('O')) #3
print(len(frase)) #25
print(len(frase.strip())) #21
print(frase.replace('Python', 'Android')) # Cueso em Vídeo Android
print('Curso' in frase) #true
print(frase.find('Curso')) #1
print(frase.find('Vídeo')) #10
print(frase.find('video')) #-1
print(frase.lower().find('vídeo')) #10
print(frase.split()) #['Curso', 'em', 'Vídeo', 'Python']
dividido = frase.split()
print(dividido) #['Curso', 'em', 'Vídeo', 'Python']
print(dividido[2]) #Vídeo
print(dividido[2][3]) #Vídeo