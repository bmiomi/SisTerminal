from Cliente import Cliente
from Usuario import Usuarios
from Compra import Compras
from Ventas import VentaProductos 
from Factura import factura
from Productos import Productos

#modulos externos.
import os
import time
from tqdm import tqdm
from getpass import getpass


nombre=input('Tu Nombre: ')
codigo=int(getpass('Tu Codigo: '))

#Intancias
emp=Usuarios(nombre,codigo)
clien=Cliente()
compra=Compras()

def loggin(func):
    def verificar(Nombre,passw):
        if emp.SetPassword== passw and emp.SetUsuario == Nombre:
            print('Welcome at the platform')
            for i in tqdm(range(10)):
                time.sleep(2)
            return True
        else:
            print('sorry,but cant sing up')
            time.sleep(1)
            return False
        os.system('cls')             
    return verificar

@loggin
def registro(Usu,passw):
    return Usu,passw

##----------------------Clientes------------------
# Ingresa datos del cliente, crea cliente, visualizar cliene creado,elimina contenido,menu cliente
#  Ingresa datos a modificar,Modificar datos cliente, visualizar cliente Modificado,elimina contenido,menu cliente
#  Ingresa datos Eliminar,Eliminar datos cliente, visualizar cliente Eliminado,elimina contenido,menu cliente
def Moduloclientes():

    try:
        while True:
            try:
                OptCliente=int(input('Seleccione una Opcion \n' '1).Crear clientes\n' '2).Modificar clientes\n' '3).Eliminar clientes\n' '4).Buscar cliente\n' '5).Ver Clientes\n' '6) Salir: ' ))
                break
            except ValueError as e:
                print(f'ADVERTENCIA : Valor ingresado Incorrecto se lanzo la excepcion de tipo: {e}')
                time.sleep(3)
                os.system('cls')
        if OptCliente == 1:
            nombre=input('Ingresa el nombre: ')
            clien.agregarcliente(nombre)
        elif OptCliente == 2:
            clien.modificarCliente()
        elif OptCliente == 3:
            cliente=input('Ingrese el Nombre del cliente a eliminar: ')
            clien.removercliente(cliente)
        elif OptCliente == 4:
            cliente=input('Ingrese el Nombre del Cliente a buscar: ')
            print(clien.buscarCliente(cliente))
        elif OptCliente ==5:
            clien.verclientes()   
        elif OptCliente==6:
            os.system('cls')
            ValicarCargoMenu()
        else:
            print('No es la Opcion Correcta.')
        time.sleep(3)
        os.system('cls') 
        Moduloclientes()

    except KeyboardInterrupt:
        print('\n')
        print('*'*100)    
        print('Cerrando programa'.center(20))
        print('*'*100)
##----------------------------Comprar-----------------------------
def ModuloCompras():
    try:
        while True:
               try:
                   respuesta=int(input('Seleccione una Opcion\t\n1) Registrar Compra\n2)Visualizar compras\n3)regresar: '))
                   break
               except ValueError as e:
                   print(f'ADVERTENCIA : Valor ingresado Incorrecto se lanzo la excepcion de tipo: {e}')
                   time.sleep(3)
                   os.system('cls')
        if respuesta==1:
            compra.AgregaCompra()
        elif respuesta==2:
            compra.VerCompra()
        elif respuesta ==3:
            pass
        
        time.sleep(3)
        os.system('cls')
        ValicarCargoMenu()

    except KeyboardInterrupt:
        print('\n')
        print('*'*100)    
        print('Cerrando programa'.center(20))
        print('*'*100)

##----------------------------Prductos-----------------------------
def ModuloProdutos():
    try:
        while True:
               try:
                   respuesta=int(input('Seleccione una Opcion\t\n1) Crear producto\n2)Modificar Producto\n3)Eliminar Producto\n4)VerProductos\n5)regresar: '))
                   break
               except ValueError as e:
                   print(f'ADVERTENCIA : Valor ingresado Incorrecto se lanzo la excepcion de tipo: {e}')
                   time.sleep(3)
                   os.system('cls')        
        
        if respuesta == 1:
            prodc=int(input('Cuantos Productos Deseas Agregar: '))
            for i in range(prodc):
                nombre=input('Dijiste el nombre del producto: ')
                cantidad=input('Dijiste la Categoria del producto: ')
                producto=Productos(nombre,cantidad)
                producto.agre_productos()
            producto.agregartxt()
        elif respuesta == 2:
            NombreViejo=input('Nombre del Producto que Deseas Modificar: ')
            nombreNuevo=input('Ingrese el Nuevo nombre: ')
            producto=Productos()
            producto.actu_productos(NombreViejo,nombreNuevo)
        elif respuesta ==3:
            pass
        elif respuesta ==4:
            producto=Productos()
            producto.ver_todosproductos()
        elif respuesta ==5:
            os.system('cls')
        ValicarCargoMenu() # ojo revisar
    except KeyboardInterrupt:
        print('\n')
        print('*'*100)    
        print('Cerrando programa'.center(20))
        print('*'*100)

##----------------------------Ventas-------------------------------
def ModuloVentas():
    ventas=VentaProductos()
    try:
        while True:
            try:
                valor=str
                while valor not in ('S','s'):
                    valor=input('Producto a Buscar: ')
                    ventas.agre_productos(valor)
                os.system('cls')
                ventas.verCesta()
                time.sleep(3)
                break
            except ValueError as e:
                print(f'ADVERTENCIA : Valor ingresado Incorrecto se lanzo la excepcion de tipo: {e}')
                time.sleep(3)
                os.system('cls')
    except KeyboardInterrupt:
        print('\n')
        print('*'*100)    
        print('Cerrando programa'.center(20))
        print('*'*100)

    menuAdministrador()

    ##----------------------------Empleado------------------------------
def ModuloUsuario():
    pass

#------------------------------------------------Menus de Roles a Desempeñar en el sistema----------------------------------.
##-----------------------------------------------Empleados------------------------------------------------------------------.
# Ingresa datos del Empleados, crea Empleados, visualizar cliene creado,elimina contenido,menu Empleados
#  Ingresa datos a modificar,Modificar datos Empleados, visualizar Empleados Modificado,elimina contenido,menu Empleados
#  Ingresa datos Eliminar,Eliminar datos Empleados, visualizar Empleados Eliminado,elimina contenido,menu Empleados
def menuEmpleado():
    print('''**********> 1)Clientes''')
    print('''**********> 3)Ventas''')
    opt=int(input('Dijite una Opcion a realizar: '))
    return opt
##-----------------------------------------------Administrador-----------------------------------------------------------------
# Ingresa datos del Empleados, crea Empleados, visualizar cliene creado,elimina contenido,menu Empleados
#  Ingresa datos a modificar,Modificar datos Empleados, visualizar Empleados Modificado,elimina contenido,menu Empleados
#  Ingresa datos Eliminar,Eliminar datos Empleados, visualizar Empleados Eliminado,elimina contenido,menu Empleados
def menuAdministrador():
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
                opt=int(input('Dijite el modulo a usar: '))
                return opt
            except ValueError as e:
                print(f'ADVERTENCIA : Valor ingresado Incorrecto se lanzo la excepcion de tipo: {e}')
                time.sleep(3)
                os.system('cls')
    except KeyboardInterrupt:
        print('\n')
        print('*'*100)    
        print('Cerrando programa'.center(20))
        print('*'*100)
##------------------------------------------------Validacion del Rol---------------------------------------------------------------------
def ValicarCargoMenu():
    os.system('cls')
    print(f'Atendido por: {emp.SetUsuario} \t\t\t Cargo: {emp.Cargo}')
    if emp.Cargo in ('ADMINISTRADOR','ANALISTA'):
        MenuOpciones(menuAdministrador())
    else:
        MenuOpciones(menuEmpleado())

def MenuOpciones(opt):
    if opt == 1:
        Moduloclientes()
    elif opt==2:
        ModuloCompras()
    elif opt==3:
        ModuloVentas()
    elif opt==4:
        pass
    elif opt==5:
        ModuloEmpleado()
    elif opt==6:
        ModuloProdutos()

if registro(nombre,codigo):
    ValicarCargoMenu()