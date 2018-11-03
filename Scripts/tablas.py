#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
    for fila in range(filas):
        for columna in range(columnas):
            print('*', end='')
        print()
else:
    print('Error, no se han mandado los argumentos correctos')
    print('Ejemplo: python tablas.py 5 6')