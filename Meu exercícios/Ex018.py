print('Calculadora de SENO, COSSENO e a TANGENTE! ')
an = float(input('Qual o angulo? '))
from cmath import sin
import math
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('Ângulo: {}°\nSeno: {:.2f}\nCosseno: {:.2f}\nTagente: {:.2f}'.format(an, seno, cos, tan))