import keyboard


def menu ():
  respuesta = int(input('Seleccione una Opcion\t\n1) Crear producto\n2)Modificar Producto\n3)Eliminar Producto\n4)VerProductos\n5)regresar: '))
  return respuesta

while True:
    menu()
    keyboard._listener
    if keyboard.is_pressed('ctrl+a'):
        print('se precionono ctrl+a')
        break