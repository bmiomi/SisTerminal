from abc import abstractproperty,ABCMeta
class Persona (metaclass=ABCMeta):

    @abstractproperty
    def get_Nombre(self):
        pass

    @abstractproperty
    def set_nombre(self):
        pass

    @abstractproperty
    def get_Apellido(self):
        pass

    @abstractproperty
    def set_Apellido(self):
        pass

    @abstractproperty
    def get_ID(self):
        pass

    @abstractproperty
    def set_ID(self):
        pass