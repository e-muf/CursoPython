#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys 

if len(sys.argv) == 2:
    numero = sys.argv[1][::-1]
    longitud = len(numero)
    
    for i in range(longitud):
        print('{:0{}d}'.format(int(numero[i]) * 10 ** i, longitud))

else:
    print('Error, número de argumentos no válido')
    print('Ejemplo: python descomposicion.py [numero]')