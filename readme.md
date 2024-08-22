# Librcomplex

Librcomplex es una librería en Python para realizar operaciones básicas con números complejos. Incluye funciones para sumar, restar, multiplicar, dividir y realizar otras operaciones con números complejos.

## Funciones

### sumaComplejos(z1, z2)

Suma dos números complejos.

*Parámetros:*
- z1 (tuple): Primer número complejo como una tupla (parte_real, parte_imag).
- z2 (tuple): Segundo número complejo como una tupla (parte_real, parte_imag).

*Retorna:*
- Tuple: Resultado de la suma como (parte_real, parte_imag).

### restaComplejos(z1, z2)

Resta dos números complejos.

*Parámetros:*
- z1 (tuple): Primer número complejo como una tupla (parte_real, parte_imag).
- z2 (tuple): Segundo número complejo como una tupla (parte_real, parte_imag).

*Retorna:*
- Tuple: Resultado de la resta como (parte_real, parte_imag).

### multiplicaComplejos(z1, z2)

Multiplica dos números complejos.

*Parámetros:*
- z1 (tuple): Primer número complejo como una tupla (parte_real, parte_imag).
- z2 (tuple): Segundo número complejo como una tupla (parte_real, parte_imag).

*Retorna:*
- Tuple: Resultado de la multiplicación como (parte_real, parte_imag).

### moduloComplejo(z)

Calcula el módulo (magnitud) de un número complejo.

*Parámetro:*
- z (tuple): Número complejo como una tupla (parte_real, parte_imag).

*Retorna:*
- Float: Magnitud del número complejo.

### fase(z)

Calcula la fase (ángulo) de un número complejo.

*Parámetro:*
- z (tuple): Número complejo como una tupla (parte_real, parte_imag).

*Retorna:*
- Float: Ángulo en radianes del número complejo.

### aPolar(z)

Convierte un número complejo de forma cartesiana a polar.

*Parámetro:*
- z (tuple): Número complejo como una tupla (parte_real, parte_imag).

*Retorna:*
- Tuple: Representación polar del número complejo como (magnitud, ángulo).

### aCartesiano(z)

Convierte un número complejo de forma polar a cartesiana.

*Parámetro:*
- z (tuple): Número complejo en forma polar como una tupla (magnitud, ángulo).

*Retorna:*
- Tuple: Representación cartesiana del número complejo como (parte_real, parte_imag).

### conjugadoComplejo(z)

Calcula el conjugado de un número complejo.

*Parámetro:*
- z (tuple): Número complejo como una tupla (parte_real, parte_imag).

*Retorna:*
- Tuple: Conjugado del número complejo como (parte_real, -parte_imag).

### divisionComplejos(z1, z2)

Divide dos números complejos.

*Parámetros:*
- z1 (tuple): Numerador como una tupla (parte_real, parte_imag).
- z2 (tuple): Denominador como una tupla (parte_real, parte_imag).

*Retorna:*
- Tuple: Resultado de la división como (parte_real, parte_imag).

