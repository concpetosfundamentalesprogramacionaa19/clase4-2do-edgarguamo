"""
    @reroes
    Ejemplo de manejo de paquetes
"""
# valor2 elevado a la potencia 2 es igual a 4

from paquete1.informacion import valores
from paquete1.informacion2 import hacer_potencia


for l in valores:
    r = hacer_potencia(l, 2)
    print("Valor %d elevado a la potencia %d"\
        "es igual a %.2f" % (l, 2, r))
