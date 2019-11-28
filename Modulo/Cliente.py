import random
from .config import config
from .config.archivos import Directorio

# from Modulo.Persona import Persona

class Clientes:

	# variable de classe de ambito privado.
	__clientes = []

	def __init__(self):
		# Persona.__init__(self)
		self.__nombre = None
		self.__apellido = None
		self.set_Codigo = None

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
			archivo.write(f'Nombre:{cliente} Apellido: Codigo:{str(codigo)}\n')

	@staticmethod
	def __CargarClientes():
		'''Se crea una lista con diccionarios del archivo txt en el directorio \\base .'''
		lista1 = []
		with open(Directorio()+'Clientes', 'r') as listadeclientes:
			contenedor = listadeclientes.read().split()
			while len (contenedor)> 3:
				tem=contenedor[:3]
				lista1.append(tem)
				contenedor=contenedor[3:]
			lista1.append(contenedor)
			contenedor=[]
			for i in lista1:
				for x in range(len(i)):
					Clientes.__clientes.append(i[x].split(':'))
					if len(Clientes.__clientes) == 3:
						contenedor.append(Clientes.__clientes)  # N° Elementos
						Clientes.__clientes = []  # 0
			for i in contenedor:
				Clientes.__clientes.append(dict(i))
			return Clientes.__clientes

	# Metodos de Instancia
	def Agregar_Cliente(self):
		try:
			cliente=input('ingrese el cliente ')
			config.logging.debug('Proceso Agregar Cliente')
			if self.Buscar_Cliente(cliente) == False:
				codigo = random.randint(0, 99999)
				self.__guargar_txt(cliente, codigo)
				print("Cliente: {0} creado con exito su codigo es {1} ".format(
					cliente, codigo))
				config.logging.debug(
					"Cliente: {0} creado con exito".format(cliente))
			else:
				print("Cliente: {0} no creado por que ya existe.".format(
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
			if len(cliente)>3 and cliente in i:
				resp = input(f'Seguro desea Eliminar el cliente {cliente}:')
				if resp in ('si', 'S', 'SI', 's'):
					archivoreadlines.remove(i)
					lista = [i.split() for i in archivoreadlines]
					with open(Directorio()+'Clientes', 'w') as archivo:
						for i in range(len(lista)):
							archivo.write(lista[i][0]+' '+lista[i][1]+' '+lista[i][2]+'\n')
					print(f"Cliente: {cliente} Eliminado con exito ")
				else:
					print(f"Los cambios para el cliente {cliente} fueron cancelados.")

	def Buscar_Cliente(self, Buscar):
		for i in self.getLista_clientes:
			if Buscar in i['Codigo'] or Buscar in i['Nombre']:
				self.set_Nombre = i['Nombre']
				self.set_Apellido = i['Apellido']
				self.set_Codigo = i['Codigo']
				print(f'Codigo: {self.get_Codigo} Cliente: {self.get_Nombre} {self.get_Apellido}')
				return True
		return False

	def Ver_Clientes(self):
		print('N° Clientes: ', len(self.getLista_clientes))
		if len(self.getLista_clientes) >= 1:
			for i in self.getLista_clientes:
				print(f"Cliente:{i['Nombre']} Apellido:{i['Apellido']} Codigo:{i['Codigo']}")

	def validar(self):
		if self.get_Codigo is not None and self.get_Nombre is not None:
			return True
		return False
