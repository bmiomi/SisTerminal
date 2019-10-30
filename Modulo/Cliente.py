import random

from .config import config
from .config.archivos import Directorio

# from Modulo.Persona import Persona


class Clientes:

	# variable de clase de ambito privado.
	__clientes = []

	def __init__(self, codigo=None):
		# Persona.__init__(self)
		self.__nombre = None
		self.__apellido = None
		self.set_Codigo = None
		self.Buscar_Cliente(codigo)

	def __repr__(self):
		return f" Cliente {self.get_Nombre} con Codigo:{self.get_Codigo}"

	# retorna  una lista diccionaro de Clientes.
	@property
	def getLista_clientes(self):
		if len(self.__clientes) == 0:
			return self.__CargarClientes()
		return self.__clientes

	# nombre del Cliente
	@property
	def get_Nombre(self):
		return self.__nombre

	@get_Nombre.setter
	def set_Nombre(self, nombre):
		self.__nombre = nombre

	@property
	def get_Apellido(self):
		return self.__apellido

	@get_Apellido.setter
	def set_Apellido(self, apellido):
		self.__apellido = apellido

	@property
	def get_Codigo(self):
		return self.__codigo

	@get_Codigo.setter
	def set_Codigo(self, codigo):
		self.__codigo = codigo

 # metodos Staticos Privados
	@staticmethod
	def __guargar_txt(cliente, codigo):
		with open(str(Directorio())+'Clientes', 'a') as archivo:
			archivo.write(
				f'Nombre:{cliente} Apellido: Codigo:{str(codigo)}\n')

	@staticmethod
	def __CargarClientes():
		'''
		  se cargan los productos que se encuentran en archivo txt
		  a la lista diccionario.
		'''

		with open(Directorio()+'Clientes', 'r') as listadeclientes:
			contenedor = listadeclientes.read().split()
			lista1 = []
			lista2 = []
			for i in range(len(contenedor)):
				lista1.append(contenedor[i])
				if len(lista1) == 3:
					lista2.append(lista1)  # N°Elementos
					lista1 = []  # 0
			for i in lista2:
				for x in range(len(i)):
					Clientes.__clientes.append(i[x].split(':'))
					if len(Clientes.__clientes) == 3:
						lista1.append(Clientes.__clientes)  # N° Elementos
						Clientes.__clientes = []  # 0
			for i in lista1:
				Clientes.__clientes.append(dict(i))
			return Clientes.__clientes

	@classmethod
	def VerficarClienteArchivo(cls, nombre):
		'''Se verifica que el cliente exista en el archivo creado en caso de existir retornara un True'''
		with open(Directorio()+'Clientes', 'r') as archivo:
			if nombre in archivo.read():
				return True
			return False

	# Metodos de Instancia
	def Agregar_Cliente(self):
		try:
			cliente=input('ingrese el cliente ')
			config.logging.debug('Proceso Agregar Cliente')
			if Clientes.VerficarClienteArchivo(cliente) == False:
				codigo = random.randint(0, 99999)
				self.__guargar_txt(cliente, codigo)
				print("Cliente: {0} creado con exito su codigo es {1} ".format(
					cliente, codigo))
				config.logging.debug(
					"Cliente: {0} creado con exito".format(cliente))
			else:
				print("Cliente: {0} no creado por que ya existe o su registro no fue el correcto.".format(
					cliente))
				config.logging.critical(
					'Proceso no realizado,Cliente existente')
		finally:
			config.logging.info('Proceso  finalizado.')

	def Modificar_Cliente(self):
		consulta = input(
			'Escriba si o no en caso que desee modificar su Usuario :\n' '1)Si\n' '2)No ')
		if consulta in ('Si', 'si', 's', 'S'):
			antiguo = input(' Dijite el nombre antiguo: ')
			if Clientes.VerficarClienteArchivo(antiguo):
				with open(Directorio()+'Clientes', 'r') as Antiguo_archivocliente:
					archivoclienteread = Antiguo_archivocliente.read()
					if antiguo in archivoclienteread:
						with open(Directorio()+'Clientes', 'w') as archivocliente1:
							Nuevo = input(' Dijite el Nuevo Nombre: ')
							archivocliente1.write(
								archivoclienteread.replace(antiguo, Nuevo))
						print('El cambio de Usuario fue exitoso')
		else:
			print('Entiendo,su modificasíon a sido cancelada')

	def Remover_Cliente(self):
		cliente = input('Ingrese el Nombre del cliente a eliminar: ')
		with open(Directorio()+'Clientes', 'r') as archivo:
			archivoreadlines = archivo.readlines()
		for i in archivoreadlines:
			if cliente in i:
				resp = input(
					'Seguro desea Eliminar el cliente {0}: '.format(cliente))
				if resp in ('si', 'S', 'SI', 's'):
					archivoreadlines.remove(i)
					lista = [i.split() for i in archivoreadlines]
					with open(Directorio()+'Clientes', 'w') as archivo:
						for i in range(len(lista)):
							archivo.write(lista[i][0]+' '+lista[i][1]+' '+lista[i][2]+'\n')
					print("Cliente: {0} Eliminado con exito ".format(cliente))
				else:
					print(
						'El cliente {0} no se encuentra en este equipo'.format(cliente))

	def Buscar_Cliente(self, codigo):
		for i in self.getLista_clientes:
			if type(i) is dict:
				if codigo is not None and codigo in i['Codigo']:
					self.set_Nombre = i['Nombre']
					self.set_Apellido = i['Apellido']
					self.set_Codigo = i['Codigo']
					return True,i
		return False, "Cliente No Encontrado."

	def Ver_Clientes(self):
		print('N° Clientes: ', len(self.getLista_clientes))
		if len(self.getLista_clientes) >= 1:
			for i in self.getLista_clientes:
				print(
					f"Cliente:{i['Nombre']} Apellido:{i['Apellido']} Codigo:{i['Codigo']}")

	def validar(self):
		if self.get_Codigo is not None and self.get_Nombre is not None:
			return True
		else:
			return False
