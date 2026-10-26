#!/usr/bin/env python3

import metricas
import volumetricas

if __name__ == "__main__":
    print("Converter\n")
    print("(1) Unidades metricas")
    print("(2) Unidades volumetricas")
    op = int(input("> "))

    if op == 1:
        metricas.menu()
    elif op == 2:
        volumetricas.menu()
    else:
        print("Opção incorreta")