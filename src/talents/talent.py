
class Talent:
    
    def __init__(self, name, email, phone, identity, id_city):
        self._name = name
        self._email = email
        self._phone = phone
        self._identity = identity
        self._id_city = id_city

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
    def id_city(self):
        return self._id_city

    @id_city.setter
    def id_city(self, id_city):
        self._id_city = id_city

    @property
    def display(self):
        print(self._name, self._email, self._phone, self._identity, self._id_city)
        return
    
    def set_phone(self, new_phone):
        pass 

    @property
    def get_array(self):
        return ({
            'name': self._name,
            'email': self._email,
            'phone': self._phone,
            'id': self._identity,
            'id_city': self._id_city
        })
    
    def __str__(self):
        return f'Talento [Nombre: {self._name}, ' \
               f'Email: {self._email},' \
               f'Teléfono: {self._phone},' \
               f'Identificación: {self._identity},' \
               f'Ciudad identificación: {self._id_city}]'
    

if __name__ == '__main__':
    talento1 = Talent('Richard Saavedra',
                      'r@r.com',
                      '3506764164',
                      14397755,
                      'Ibagué')
    print(talento1)
