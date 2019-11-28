import os
import time
import keyboard
from getpass import getpass
from tqdm import tqdm

from .Cliente import Clientes
from .Empleados import Empleados
from .Compra import Compras
from .Ventas import VentaProductos
from .Factura import factura


def loggin(func):    
    def verificar(self,Obj):
        if Obj.validar(input('Ingrese su Usuario: ').title(),getpass('Ingrese contraseña: ')) or Obj.getcargo is not None:
            print('Welcome at the platform')
            #for i in tqdm(range(10)):
            #   time.sleep(2)
            func(self,Obj)
            return True
        else:
            print('sorry,but cant sing up')
            time.sleep(1)
            os.system('cls')
        return False
    
    return verificar

    
class Empresa():

  def __init__(self, nombreE):
    self.Nombre = nombreE
    self.ObjetoCompra = Compras()
    self.ObjetoVenta = VentaProductos()
    self.objCliente = Clientes()
    self.ojPersonal=Empleados()


    "16DA:BN25_27"

 # ----------------------------Clientes--------------------------
  def Moduloclientes(self):
    opcionesCliente={
        '1':self.objCliente.Agregar_Cliente,
        '2':self.objCliente.Modificar_Cliente,
        '3':self.objCliente.Remover_Cliente,
        '4':self.objCliente.Buscar_Cliente,
        '5':self.objCliente.Ver_Clientes,
        '6':self.ValidarCargoMenu
        }
    while True:
        OptCliente = input(
            'Seleccione una Opcion \n' '1).Crear clientes\n' '2).Modificar clientes\n' '3).Eliminar clientes\n' '4).Buscar cliente\n' '5).Ver Clientes\n' '6) Salir: ')
        if OptCliente.isdigit(): 
            time.sleep(1)
            os.system('cls')
            break
    valor=opcionesCliente.get(OptCliente)
    if OptCliente == '4':
        return valor(input('Ingrese el Codigo/Nombre del Cliente a Buscar: '))
    elif valor is not None:
        valor()
    return self.ValidarCargoMenu()

 # ----------------------------Comprar-----------------------------
  def ModuloCompras(self):
      
      opcionescompra={
        '1':self.ObjetoCompra.AgregarCompra,
        '2':self.ObjetoCompra.VerCompra,
        '3':self.ValidarCargoMenu
    }
      while True: 
        respuesta = input('Seleccione una Opcion\t\n1) Registrar Compra\n2)Visualizar compras\n3)regresar: ')
        if respuesta.isdigit():
            time.sleep(1)
            os.system('cls')             
            break
      re=opcionescompra.get(respuesta)
      if re is not  None:
          re()
      return self.ValidarCargoMenu()       
 # ----------------------------Ventas-------------------------------

  def ModuloVentas(self):
      while True:
          iteraciones=int(input(f'Cuatos productos adquirio en nuestra Tienda estimado {self.objCliente.get_Nombre}: '))
          intentos=0
          while iteraciones >= intentos:
            print('Ingrese el Producto N°',intentos+1)
            respuesta=self.ObjetoVenta.AgregarVenta( input('Producto a Buscar: '), input('ingrese la cantiad: '))    
            if respuesta is True:
               os.system('cls')
               intentos+=1  
          consultar=input('Desea Genara una factura a la compra: ')
          if consultar in ('Si','si','s','S'):
              self.__ModuloFactura()
          break  
      self.menuAdministrador()

 # ----------------------------Factura-------------------------------

  def __ModuloFactura(self):
     ObjFactura = factura(self.objCliente.get_Codigo)
     if self.objCliente.get_Nombre is None:    
         respuesta = input(
             "El cliente no ha sido registrado en el sistema, por tal motivo  el cliente saldra como Generico en la factura desea aceptar (S|N): ")
         if respuesta in ('S', 'Si', 's', 'y', 'Yes'):
            ObjFactura.getCabecera('Generico')
     else:
         ObjFactura.generarFactura(self.Nombre,self.objCliente.get_Nombre,self.objCliente.get_Apellido,self.objCliente.get_Codigo,self.ObjetoVenta._Cesta_Venta)


 # ----------------------------Validacion Reguistro--------------------
  @loggin
  def registro(self, Obj):
      if Obj.getcargo is not None:
          os.system('cls')
          print(f'Atendido por: {Obj.SetUsuario} \t\t\t Cargo: {Obj.SetCargo}')
          self.ValidarCargoMenu()
      return False

  def ValidarCargoMenu(self):
       if self.ojPersonal.getcargo is not  None:
           if self.ojPersonal.getcargo == "ADMINISTRADOR":
            self.MenuOpcionesAdministrador(str(self.menuAdministrador()))
           else:
            self.MenuOpciones(self.menuEmpleado())
       return False


 # -----------------------------Menus de Roles a Desempeñar en el sistema----

 # ----------------------------Empleados------------------------------------.
  def menuEmpleado(self):
        print('''**********> 1)Clientes''')
        print('''**********> 2)Ventas''')
        return input('Dijite una Opcion a realizar: ')

  def MenuOpciones(self, opt):
     if opt == '1':
        self.Moduloclientes()
     elif opt == '2':
         self.ModuloVentas()
 # ----------------------------Administrador-----------------------------------

  def menuAdministrador(self):
    
     while True:
         try:
             print('''Modulo Disponibles.''')
             print('''////////////////////.''')
             print('''**********> 1)Clientes''')
             print('''**********> 2)Compra.''')
             print('''**********> 3)Venta''')
             print('''**********> 4)Almacen''')
             print('''**********> 5)Empleados''')
             print('''**********> 6)Productos.''')
             opt = int(input('Dijite el modulo a usar: '))
             return opt
         except ValueError as e:
             print(
                 f'ADVERTENCIA : Valor ingresado Incorrecto se lanzo la excepcion de tipo: {e}')
             time.sleep(3)
             os.system('cls')

  def MenuOpcionesAdministrador(self,opt):
      opts={
          '1':self.Moduloclientes,
          '2':self.ModuloCompras,
          '3':self.ModuloVentas,
          }
      retornar=opts.get(opt)
      if retornar is not  None:
          return retornar()
#---------------------------------

  def banner(self):
      print('''
      ##     ## ####  #######  ##     ## ####  ######  ##    ##  ######  ######## ######## ##     ## 
      ###   ###  ##  ##     ## ###   ###  ##  ##    ##  ##  ##  ##    ##    ##    ##       ###   ### 
      #### ####  ##  ##     ## #### ####  ##  ##         ####   ##          ##    ##       #### #### 
      ## ### ##  ##  ##     ## ## ### ##  ##   ######     ##     ######     ##    ######   ## ### ## 
      ##     ##  ##  ##     ## ##     ##  ##        ##    ##          ##    ##    ##       ##     ## 
      ##     ##  ##  ##     ## ##     ##  ##  ##    ##    ##    ##    ##    ##    ##       ##     ## 
      ##     ## ####  #######  ##     ## ####  ######     ##     ######     ##    ######## ##     ## 
      ''')  

  def run(self):
      try:
          self.banner()
          listaOpciones=['Si','si','s','S']
          opcion=input('Perteneces o trabajas en nuestra empresa (si/no): ')
          if opcion in listaOpciones:
              self.registro(self.ojPersonal)
          else:        
              consulta=input('Estimado Clientes tienes registro o posees un cuenta en nuestra Empresa (Si/No): ')
              if consulta in listaOpciones:
                   self.objCliente.Buscar_Cliente(input('Ingrese su codigo '))
                   if self.objCliente.validar():
                       os.system('cls')
                       print(f' Bienvenido {self.objCliente.get_Nombre} {self.objCliente.get_Apellido}')
                       self.ModuloVentas()
      except KeyboardInterrupt as e:
         print('\n')
         print('*'*100)
         print('Cerrando Programa'.center(20))
         print('*'*100)
      except ValueError  as e:
          print('Valor ingreado erroneo')
 
