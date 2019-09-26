#!/usr/bin/python3

# guardar en la carpeta del proyecto
# X:\laragon\www\
# con el nombre ejemplo_funcion

# las funciones en python se definen con def :

def funcion_tonta(nombre) :
	separador = " "
	mensaje = separador.join(("Oh", "El Uwu del" , nombre))
	print(mensaje)



# una funcion un poco mas compleja: calculo del digito verificador
# de un rut chileno.
def  digito_verificador(rut):
	digito = ""
	contador = 2
	suma = 0 
	multiplo = 0
	while rut > 0:
		multiplo = ( rut % 10 ) * contador
		suma = suma + multiplo
		rut = rut // 10 # division entera!
		contador = contador + 1
		if contador == 8 :
			contador = 2
	digito = 11 - (suma % 11)
	if digito == 11:
	   	digito = 0
	if digito == 10 :
		digito = 'K'
	return str(digito)



mi_rut = 20382907
print("-".join((str(mi_rut), digito_verificador(mi_rut))))



# y llamamos al funcion...
funcion_tonta("owo")
funcion_tonta("anibal")
