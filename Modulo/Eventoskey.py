import sys

if sys.platform == 'win32':

    import msvcrt

    def keypressed():
        key = msvcrt.getch()
        if key == b"\x1b": #ESC
            return "Escape"
        else:
            return key.decode("ANSI")


elif sys.platform == 'linux':

    import os
    import termios
    TERMIOS = termios

    def keypressed():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
        new[6][TERMIOS.VMIN] = 1
        new[6][TERMIOS.VTIME] = 0
        termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
        key = None
        try:
            key = os.read(fd, 4)
            if key == b'\x1b':
                key = "Escape"
            else:
                key = key.decode()

        finally:
            termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
        return key

pt=keypressed()
print(pt)