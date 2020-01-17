import logging
import os
import platform

if platform.platform().startswith('Windows'):
    fichero_log = os.path.join( os.getcwd()+'\log','Clientes.log')
else:
    fichero_log = os.path.join(os.getenv('HOME'), 'test.log')
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    filename = fichero_log,
                    filemode = 'a')