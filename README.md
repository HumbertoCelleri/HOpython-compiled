# Compiled languages into Python

En este hands-on vamos a practicar cómo llamar a una librería
nuestra desde python. En la carpeta `src/` tienen dos archivos de C.
Para completar este ejercicio tienen que hacer los siguientes pasos:

1. Compilar ambos archivos como objetos separados
  Compilamos los objetos de manera " Position independet Code": 
  ```gcc -fPIC -c *.c
  ```
2. Construir una librería dinámica que tenga ambos objetos

  La llamamos Biblioteca de matematica de Humberto (HumsMath).

  ```gcc -shared *.o -o .so
  ```
  La libreria dinamica, en tiempo de ejecución, va donde esta linkeada y la ejecuta y vuelve. En las estaticas ya copiaste el código.
  
3. Escribir un script en python que pruebe **todas** las funciones
de la librería

  Vamos a usar Ctypes, que permite llamar funciones en C defiendo los tipos en Python

#!/usr/bin/env python2.7
