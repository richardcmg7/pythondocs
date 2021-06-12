#/usr/bin/python3

class Menu:
    
    def __init__(self):
        pass
    @property
    def list_options(self):
        command = '''
        Que deseas hacer?
        
        [a]ñadir talento
        [ac]tualizar talento
        [b]uscar talento
        [se]eleccionar talentos
        [l]istar talentos
        [e]liminar talento
        [s]alir con los talentos seleccionados     
        '''
        return command