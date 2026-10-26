def Volumetricas():
    print("Conversor de Unidades Volumétricas")
    print("(1) Litros -> Mililitros")
    print("(2) Mililitros -> Litros")
    print("(3) Metros cúbicos -> Litros")
    print("(4) Litros -> Metros cúbicos")
    
    op = int(input("> "))
    
    if op == 1:
        x = float(input("Litros = "))
        print(f"Mililitros = {x * 1000}")
        
    elif op == 2:
        x = float(input("Mililitros = "))
        print(f"Litros = {x / 1000}")
        
    elif op == 3:
        x = float(input("Metros cúbicos = "))
        print(f"Litros = {x * 1000}")
        
    elif op == 4:
        x = float(input("Litros = "))
        print(f"Metros cúbicos = {x / 1000}")