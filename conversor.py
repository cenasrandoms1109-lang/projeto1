#!/usr/bin/env python3



#Para fins de teste
if __name__ == "__main__":

    print("Converter\n")
    print("(1) Unidades metricas")
    print("(2) Unidades volumetricas")
    op1 = int(input("> "))

    if op1 == 1:
        print("(1) m -> km")
        print("(2) km -> m")
        print("(3) m -> mm")
        print("(4) mm -> m")
        op2 = int(input("> "))

        if op2 == 1:
            x = float(input("m = "))
            print(f"km = {x/1000}")

        elif op2 == 2:
            x = float(input("km = "))
            print(f"m = {x*1000}")

        elif op2 == 3:
            x = float(input("m = "))
            print(f"mm = {x*1000}")

        elif op2 == 4:
            x = float(input("mm = "))
            print(f"m = {x/1000}")

        else:
            print("Opção incorreta")

    elif op1 == 2:
        print("(1) l -> ml")
        print("(2) ml -> l")
        print("(3) l -> hl")
        print("(4) hl -> l")
        op2 = int(input("> "))

        if op2 == 1:
            x = float(input("l = "))
            print(f"ml = {x*1000}")

        elif op2 == 2:
            x = float(input("ml = "))
            print(f"l = {x/1000}")

        elif op2 == 3:
            x = float(input("l = "))
            print(f"hl = {x/100}")

        elif op2 == 4:
            x = float(input("hl = "))
            print(f"l = {x*100}")

        else:
            print("Opção incorreta")

    else:
        print("Opção incorreta")


    #Area para utilizar funcoes