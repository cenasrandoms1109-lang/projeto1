def l_para_ml(x):
    return x * 1000

def ml_para_l(x):
    return x / 1000

def l_para_hl(x):
    return x / 100

def hl_para_l(x):
    return x * 100

def menu():
    print("(1) l -> ml")
    print("(2) ml -> l")
    print("(3) l -> hl")
    print("(4) hl -> l")
    op = int(input("> "))

    if op == 1:
        print(f"ml = {l_para_ml(float(input('l = ')))}")
    elif op == 2:
        print(f"l = {ml_para_l(float(input('ml = ')))}")
    elif op == 3:
        print(f"hl = {l_para_hl(float(input('l = ')))}")
    elif op == 4:
        print(f"l = {hl_para_l(float(input('hl = ')))}")
    else:
        print("Opção incorreta")