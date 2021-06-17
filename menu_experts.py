# /usr/bin/python3

class MenuExperts:

    def __init__(self):
        pass

    @property
    def list_options(self):
        command = '''
        Que deseas hacer?
        
        [a]ñadir experto
        [ac]tualizar experto
        [b]uscar experto
        [se]eleccionar expertos
        [l]istar expertos
        [e]liminar experto
        [s]alir con los expertos seleccionados     
        '''
        return command
