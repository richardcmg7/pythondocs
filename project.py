class Project:
    def __init__(self, id, name, date):
        self._id = id
        self._name = name
        self._date = date
    
    @property
    def display(self):
        print(f'Nombre del proyecto { self.name }, código del proyecto { self.id }')
    
    # getter function
    @property
    def id(self):
        return self._id
    
    # setter function
    @id.setter
    def id(self, i):
        self._id = i
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, n):
        self._name = n

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, d):
        self._date = d

    @property
    def get_project(self, id):
        pass