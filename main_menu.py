# /usr/bin/python3

class MainMenu:

    def __init__(self):
        pass

    @property
    def list_options(self):
        command = '''
        Selecciona el acta que se va a generar?

        [a]cta de confidencialidad y compromiso
        [m]anual de uso de infraestructura
        [am]acta de confidencialidad y manual de infraestructura
        [s]alir
        '''
        return command
