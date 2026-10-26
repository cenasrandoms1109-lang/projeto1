def m_para_km(x):
    return x / 1000

def km_para_m(x):
    return x * 1000

def m_para_mm(x):
    return x * 1000

def mm_para_m(x):
    return x / 1000

def menu():
    print("(1) m -> km")
    print("(2) km -> m")
    print("(3) m -> mm")
    print("(4) mm -> m")
    op = int(input("> "))

    if op == 1:
        print(f"km = {m_para_km(float(input('m = ')))}")
    elif op == 2:
        print(f"m = {km_para_m(float(input('km = ')))}")
    elif op == 3:
        print(f"mm = {m_para_mm(float(input('m = ')))}")
    elif op == 4:
        print(f"m = {mm_para_m(float(input('mm = ')))}")
    else:
        print("Opção incorreta")