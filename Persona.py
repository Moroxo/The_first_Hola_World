

class Persona:
	# en py hay solo un "constructor" que se llama __init__ (doble underscore) intit (doble underscore)
	# deben recibir un parametro self!!
	# si una variable parte con un guion bajo se dene tratar como si fuera privada
	def __init__( self, nombre, rut):
		self.nombre = nombre
		self.rut = rut

	def imprimir(self):
		texto = " ".join(("soy", self.nombre, "mi rut es ", self.rut))
		print(texto)
