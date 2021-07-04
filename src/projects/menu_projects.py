#!/usr/bin/python3

class MenuProjects:
    
    def __init__(self):
        pass
    @property
    def list_options(self):
        command = '''
        Que deseas hacer?
        
        [a]gregar proyecto
        [ac]tualizar proyecto
        [se]eleccionar proyecto
        [l]istar proyectos 
        [e]liminar proyecto
        [s]alir con el proyecto seleccionado    
        '''
        return command