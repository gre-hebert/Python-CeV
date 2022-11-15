pasta = 0 #Se o pasta ficar dentro de if vai zera toda hora.
for n in range(1, 501):
    if n % 2 == 1 and n % 3 == 0:
               pasta += n
print(pasta)    