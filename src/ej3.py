#!/usr/bin/env python2.7

""" EJercicio 3 del Dia 3: wtpc2016
Linkeo libreria en C con python

"""
__author__      = "Humberto Celleri"


import ctypes as C

def pasajeNumeroAtipoCint(arg = 0):
    ret = C.c_int(arg)
    return ret

def pasajeNumeroAtipoCfloat(arg = 0):
    ret = C.c_float(arg)
    return ret



def main():
    """ We wish to test Python-Compiled examples
    """
    HumsMath = C.CDLL('./HumsMath.so')
    
    
    # Probamos suma integers
    suma_int = HumsMath.add_int(3,4)
    
    print " La suma de integers da ", suma_int
    print " "
    
    # Probamos suma float: debemos definir los tipos.
    HumsMath.add_float.restype = C.c_float
    HumsMath.add_float.argtypes = [C.c_float , C.c_float]
    suma_float = HumsMath.add_float(3.,4.)
    
    print " La suma de floats da ", suma_float
    print " "


    # Probamos suma integers por referencia
    arg1 = pasajeNumeroAtipoCint(3)
    arg2 = pasajeNumeroAtipoCint(4)
    suma_int_ref = pasajeNumeroAtipoCint()
    HumsMath.add_int_ref( C.byref(arg1), C.byref(arg2), C.byref(suma_int_ref))

    print " La suma de integers por referencia da ", suma_int_ref.value
    print " "


    # Probamos suma float por referencia: debemos definir los tipos.
    arg1_float = pasajeNumeroAtipoCfloat(3)
    arg2_float = pasajeNumeroAtipoCfloat(4)
    suma_float_ref = pasajeNumeroAtipoCfloat()
    HumsMath.add_float_ref( C.byref(arg1_float), C.byref(arg2_float), \
    C.byref(suma_float_ref))
    
    print " La suma de floats por referencia da ", suma_float_ref.value
    print " "


    # Probamos arrays.add_int_array
    arg1_array = (C.c_int*3)(3,7,9)
    arg2_array = (C.c_int*3)(1,1,1)
    add_array = (C.c_int*3)(0,0,0)

    HumsMath.add_int_array( C.byref(arg1_array), C.byref(arg2_array),\
    C.byref(add_array),3)

    print " La suma de arrays da ", \
    add_array[0], add_array[1], add_array[2]
    print " "


    # Probamos arrays.dot_product
    arg1_dot = (C.c_float*3)(2,1,2)
    arg2_dot = (C.c_float*3)(1,1,1)
    HumsMath.dot_product.restype = C.c_float
    res_dot = HumsMath.dot_product( C.byref(arg1_dot), C.byref(arg2_dot),3)
    
    print " La multiplicacion punto de arrays da ", \
    res_dot
    print " "
    
if __name__ == "__main__":
    main()

