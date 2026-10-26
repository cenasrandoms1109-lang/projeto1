
def Metricas():
    print(" (1) m -> km , (2) km -> m, (3) cm -> m, (4) m -> cm ")
    op2 = int(input("> "))
    
    if op2 == 1:
        x = float(input(" m = "))
        print(f"km = {x / 1000} ")
  
    elif op2 == 2:
        x = float(input(" km = "))
        print(f" m = {x * 1000} ")
  
    elif op2 == 3:
        x = float(input(" cm = "))
        print(f" m = {x / 100} ")
 
    elif op2 == 4:
        x = float(input(" m = "))
        print(f" cm = {x * 100} ")