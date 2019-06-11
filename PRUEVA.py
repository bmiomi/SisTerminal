


from asciimatics.screen import Screen
from time import sleep

def demo ( screen ):
    screen.print_at ( 'Bryano' , 0 , 0,Screen.COLOUR_GREEN,Screen.COLOUR_RED)
    screen . refresh ()
    sleep ( 10 )
    
Screen . wrapper ( demo )