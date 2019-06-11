from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
import PRUEVA

def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText(str(PRUEVA.nombre), font='big'),
            screen.height // 2 - 8),

           Cycle(
            screen,
            FigletText(('Buen Dia '), font='big'),
            screen.height // 2 + 3),
        Stars(screen, (screen.width + screen.height) // 2)
    ]
    screen.play([Scene(effects, 500)])

import random
import time
intentos=5
while intentos >=0:
    dato=input('Dijita un numero: ')
    print('Intentos N°',intentos)
    numero=random.randint(0,3)
    if numero == int(dato):
        print('Genial, Ganaste tu premio. '+':(')
        print('en breve te direcciono a tu primera sorpresa.')
        time.sleep(20)
        Screen.wrapper(demo)
    else:
        print('Genial te gane!!')
        intentos-=1