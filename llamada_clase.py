
from Persona import Persona
		
#ahora "el main" que esta fuera de la clase

perrin = Persona("juan elaca riciador", "12234234-3")
perrin.imprimir()

# en py los atributos son publicos y por tanto se pueden modificar directamente
perrin.rut = "12234234-3"
perrin.imprimir()

# Las clases parten con Mayusculas y usan camel!
# mientras las funciones usan minusculas y se conectan con guin bajo
# ejem: clase (mal) alumno_duoc -> (bien) AlumnoDuoc
# ejem: funcion (mal) imprimirDetalles -> (bien) imprimir_detalle

# Ej: crear una persona leyendo desde la consola:
nombre = input ("Ingrese un nombre")
rut = input ("Ingrese el rut")
personaIngresada = Persona(nombre, rut)
personaIngresada.imprimir()