import os
import sys
import time
import keyboard
from getpass import getpass
from tqdm import tqdm

from .Cliente import Clientes
from .Personal import Personal
from .Compra import Compras
from .Ventas import VentaProductos
from .Factura import factura


def loggin(func):
    def verificar(self, Objpersonal):
        if Objpersonal.validar(input('Ingresa tu Usuario:'), getpass('Ingresa tus credenciales:')):
          print('Welcome at the platform')
          #for i in tqdm(range(10)):
          #   time.sleep(2)
          print(f'Atendido por: {Objpersonal.SetUsuario} \t\t\t Cargo: {Objpersonal.Cargo}')
          return True,Objpersonal 
        else:
          print('sorry,but cant sing up')
          time.sleep(1)
          return False
          os.system('cls')
    return verificar
    
class Empresa():

  def __init__(self, nombreE):
    self.Nombre = nombreE
    self.ObjetoCompra = Compras()
    self.ObjetoVenta = VentaProductos()
    self.objCliente = Clientes()

    "16DA:BN25_27"

 # ----------------------------Clientes--------------------------
  def Moduloclientes(self):
     try:
         while True:
             try:
                 OptCliente = input(
                     'Seleccione una Opcion \n' '1).Crear clientes\n' '2).Modificar clientes\n' '3).Eliminar clientes\n' '4).Buscar cliente\n' '5).Ver Clientes\n' '6) Salir: ')
                 break
             except ValueError as e:
                 print(
                     f'ADVERTENCIA : Valor ingresado Incorrecto se lanzo la excepcion de tipo: {e}')
                 time.sleep(1)
                 os.system('cls')
         opcionesCliente={
             '1':self.objCliente.Agregar_Cliente,
             '2':self.objCliente.Modificar_Cliente,
             '3':self.objCliente.Remover_Cliente,
             '4':self.objCliente.Buscar_Cliente,
             '5':self.objCliente.Ver_Clientes,
             '6':self.ValidarCargoMenu
         }
         
         valor=opcionesCliente.get(OptCliente)
         if valor:
             return valor()
         else:
            print('Opcion Incorrecta')         
            time.sleep(3)
            os.system('cls')
         self.Moduloclientes()
     except KeyboardInterrupt:
         print('\n')
         print('*'*100)
         print('Cerrando programa'.center(20))
         print('*'*100)
 
 # ----------------------------Prductos-----------------------------
  def ModuloProdutos(self):
     try:
         while True:
                try:
                    respuesta = int(input(
                        'Seleccione una Opcion\t\n1) Crear producto\n2)Modificar Producto\n3)Eliminar Producto\n4)VerProductos\n5)regresar: '))
                    break
                except ValueError as e:
                    print(
                        f'ADVERTENCIA : Valor ingresado Incorrecto se lanzo la excepcion de tipo: {e}')
                    time.sleep(3)
                    os.system('cls')

         if respuesta == 1:
             prodc = int(input('Cuantos Productos Deseas Agregar: '))
             for i in range(prodc):
                 nombre = input('Dijiste el nombre del producto: ')
                 cantidad = input('Dijiste la Categoria del producto: ')
                 producto = Productos(nombre, cantidad)
                 producto.agre_productos()
                 time.sleep(3)
         elif respuesta == 2:
             NombreViejo = input('Nombre del Producto que Deseas Modificar: ')
             nombreNuevo = input('Ingrese el Nuevo nombre: ')
             producto = Productos()
             producto.actu_productos(NombreViejo, nombreNuevo)
         elif respuesta == 3:
             pass
         elif respuesta == 4:
             producto = Productos()
             producto.ver_todosproductos()
             time.sleep(5)
         elif respuesta == 5:
             os.system('cls')
         self.ValidarCargoMenu(i[1])  # ojo revisar
     except KeyboardInterrupt:
         print('\n')
         print('*'*100)
         print('Cerrando programa'.center(20))
         print('*'*100)

 # ----------------------------Comprar-----------------------------
  def ModuloCompras(self):
     try:
         while True:
                try:
                    respuesta = int(input(
                        'Seleccione una Opcion\t\n1) Registrar Compra\n2)Visualizar compras\n3)regresar: '))
                    break
                except ValueError as e:
                    print(
                        f'ADVERTENCIA : Valor ingresado Incorrecto se lanzo la excepcion de tipo: {e}')
                    time.sleep(3)
                    os.system('cls')
         opcionescompra={
             '1':self.ObjetoCompra.AgregarCompra,
             '2':self.ObjetoCompra.VerCompra,
         }
         
         re=opcionescompra.get(respuesta)
         if re:
             return re()           
         time.sleep(3)
         os.system('cls')
         self.ValidarCargoMenu(i[1])
     except KeyboardInterrupt:
         print('\n')
         print('*'*100)
         print('Cerrando programa'.center(20))
         print('*'*100)

 # ----------------------------Ventas-------------------------------
  def ModuloVentas(self):
     try:
             try:
                 while True:
                    if keyboard.is_pressed('ctrl+g'):
                        print('entre')
                        self.ModuloFactura()
                        break
                    else:
                         self.ObjetoVenta.AgregarVenta(
                             input('Producto a Buscar: '), 
                             input('ingrese la cantiad: ')
                             )
                         #self.ObjetoVenta.verCesta()
                 # time.sleep(30)
                 # os.system('cls')
             except ValueError as e:
                 print(
                     f'ADVERTENCIA : Valor ingresado Incorrecto se lanzo la excepcion de tipo: {e}')
                 # time.sleep(3)
                 # os.system('cls')
     except KeyboardInterrupt:
         print('\n')
         print('*'*100)
         print('Cerrando programa'.center(20))
         print('*'*100)
    # self.menuAdministrador()

 # ----------------------------Factura-------------------------------
  def ModuloFactura(self):
     ObjFactura = factura(self.objCliente.get_Codigo)
     p = self.objCliente.Buscar_Cliente(self.objCliente.get_Codigo)
     if p[0] is False:
         respuesta = input(
             "El cliente no ha sido registrado en el sistema, por tal motivo  el cliente saldra como Generico en la factura desea aceptar (S|N): ")
         if respuesta in ('S', 'Si', 's', 'y', 'Yes'):
            ObjFactura.getCabecera('Generico')
     else:
         ObjFactura.getCabecera(p[1]['Nombre'])
     ObjFactura.getdetalle()

 # ----------------------------Usuario----------------
  def ModuloUsuario(self):
     pass
 # ----------------------------Validacion del Rol---------------------
  @loggin
  def registro(self, Obj):
      return Obj

  def ValidarCargoMenu(self,o):
     os.system('cls')
     print(f'Atendido por: {o.SetUsuario} \t\t\t Cargo: {o.Cargo}')
     if o.getcargo() in ('ADMINISTRADOR', 'ANALISTA'):
         self.MenuOpcionesAdministrador(str(self.menuAdministrador()))
     else:
         self.MenuOpciones(self.menuEmpleado())
 # -----------------------------Menus de Roles a Desempeñar en el sistema----
 # ----------------------------Empleados------------------------------------.

  def menuEmpleado(self):
     print('''**********> 1)Clientes''')
     print('''**********> 2)Ventas''')
     opt = int(input('Dijite una Opcion a realizar: '))
     return opt

  def MenuOpciones(self, opt):
     if opt == 1:
        self.Moduloclientes()
     elif opt == 2:
         self.ModuloCompras()
  # ----------------------------Administrador-----------------------------------

  def menuAdministrador(self):
     try:
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
     except KeyboardInterrupt:
         print('\n')
         print('*'*100)
         print('Cerrando programa'.center(20))
         print('*'*100)

  
  def MenuOpcionesAdministrador(self,opt):
      opts={
          '1':self.Moduloclientes,
          '2':self.ModuloCompras,
          '3':self.ModuloVentas,
          '5':self.ModuloProdutos
          }
      retornar=opts.get(opt)
      if retornar is not  None:
          return retornar()

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
       self.banner()
       listaOpciones=['Si','si','s','S']
       opcion=input('Perteneces o trabajas en nuestra empresa (si/no): ')
       if opcion in listaOpciones:
            #global i
            i=self.registro(Personal())
#            i.Cargo() in ()
            if i[1].getcargo in ('ADMINISTRADOR', 'ANALISTA'):
                self.MenuOpcionesAdministrador(str(self.menuAdministrador()))
            else:
                self.MenuOpciones(self.menuEmpleado())   
            if i !=False:
                self.ValidarCargoMenu(i[1])

       else:
           consulta=input('Estimado Clientes tienes registro o posees un cuenta en nuestra Empresa (Si/No): ')
           if consulta not in listaOpciones:
               self.objCliente.Agregar_Cliente(input('Ingrese su Nombre: '))
           else:
                f=self.objCliente.Buscar_Cliente(input('Ingrese su codigo '))
                if self.objCliente.validar():
                    print(f' Bienvenido {self.objCliente.get_Nombre} {self.objCliente.get_Apellido}')
                    self.ModuloVentas()
                


       time.sleep(4)       

