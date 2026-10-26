# !/ usr / bin / env python3
from Volumetricas import Volumetricas
from Metricas import Metricas
if __name__ == " __main__ " :
 #menu
    print ( " Converter \ n " )
    print ( " (1) Unidades metricas " )
    print ( " (2) Unidades volumetricas " )
    op1 = int ( input ( "> " ) )
 
    if op1 == 1:
        Metricas()
    elif op1 == 2:
        Volumetricas()
    else:
        print("Opção incorreta")
 
