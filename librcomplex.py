import math

def sumaComplejos (z1, z2):
    parte_real = z1[0] + z2[0]
    parte_imag = z1[1] + z2[1]
    return (parte_real, parte_imag)

def restaComplejos (z1, z2):
    parte_real = z1[0] - z2[0]
    parte_imag = z1[1] - z2[1]
    return (parte_real, parte_imag)

def multiplicaComplejos (z1, z2):
    parte_real = (z1[0] * z2[0]) - (z1[1] * z2[1])
    parte_imag = (z1[0] * z2[1]) + (z1[1] * z2[0])
    return (parte_real, parte_imag)

def moduloComplejo (z):
    return math.sqrt((z[0]**2) + (z[1]**2))

def fase (z):
    angulo = math.atan2(z[1], z[0])
    return angulo if angulo >= 0 else (2 * math.pi + angulo)

def aPolar (z):
    magnitud = moduloComplejo(z)
    angulo = fase(z)
    return (magnitud, angulo)

def aCartesiano (z):
    r = z[0]
    theta = z[1]
    parte_real = r * math.cos(theta)
    parte_imag = r * math.sin(theta)
    return (parte_real, parte_imag)

def conjugadoComplejo(z):
    parte_real = z[0]
    parte_imag = -z[1]
    return (parte_real, parte_imag)

def divisionComplejos (z1, z2):
    numerador = multiplicaComplejos(z1, conjugadoComplejo(z2))
    denominador = z2[0]**2 + z2[1]**2
    parte_real = numerador[0] / denominador
    parte_imag = numerador[1] / denominador
    return (parte_real, parte_imag)
