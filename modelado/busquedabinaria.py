
class busquedabinaria(object):
	def __init__(self,datos):
		self.datos = datos

	def optener_datos(self):
		return self.datos
	def agregar_datos(self,datos):
		self.datos = datos

	def BusquedaBinaria(self,busqueda):
		elementobusqueda = busqueda
		inferior = 0 
		superior = len (self.datos)-1
		medio = int((inferior + superior + 1) / 2)
		ubicacion = -1
		# condicion para encontar el elemento a buscar 
		while ((inferior <= superior) and (ubicacion == -1)):
			if (elementobusqueda == self.datos[medio]):
				ubicacion = medio
			elif (elementobusqueda < self.datos[medio]):
				superior = medio -1
			else :
		  		inferior = medio +1 
		  	# convertimos a entermos los valores de las cadenas
			medio = int((inferior + superior +1)/2)
		return ubicacion