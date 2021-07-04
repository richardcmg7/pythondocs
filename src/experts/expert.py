class Expert:
    count = 0

    def __init__(self, name, email, phone, identity):
        self._name = name
        self._email = email
        self._phone = phone
        self._identity = identity
        self.count += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, identity):
        self._identity = identity

    @property
    def display(self):
        print(self._name, self._email, self._phone, self._identity)

    @property
    def get_array(self):
        return ({
            'name': self._name,
            'email': self._email,
            'phone': self._phone,
            'id': self._identity
        })

    @classmethod
    def from_str(cls, string):
        name, email, phone, identity = string.split(',')
        return cls(name=name, email=email, phone=phone, identity=identity)

    @classmethod
    def from_dict(cls, dictionary):
        return cls(name=dictionary['name'],
                   email=dictionary['email'],
                   phone=dictionary['phone'],
                   identity=dictionary['identity'])

    def __str__(self):
        return f'Experto [Nombre: {self._name}, ' \
               f'Email: {self._email},' \
               f'Teléfono: {self._phone},' \
               f'Identificación: {self._identity}]'


if __name__ == '__main__':
    experto1 = Expert('Richard Saavedra',
                      'r@r.com',
                      '3506764164',
                      14397755)
    print(experto1)

    # Using class methods to define several way to receive the data
    # Diccionario
    data_expert = {'name': 'Saavedra',
                   'email': 'r@r.com',
                   'phone': '3506764164',
                   'identity': 14397755}
    experto2 = Expert.from_dict(data_expert)
    print(experto2)

    # String
    data_expert = 'Richard, r@r.com, 3506764164, 14397755'
    experto3 = Expert.from_str(data_expert)
    print(experto3)