
class Talent:
    
    def __init__(self, name, email, phone, identity, id_city):
        self.name = name
        self.email = email
        self.phone = phone
        self.identity = identity
        self.id_city = id_city
        
    @property
    def display(self):
        print(self.name, self.email, self.phone, self.identity, self.id_city)
        return
    
    def set_phone(self, new_phone):
        pass 

    @property
    def get_array(self):
        return ({
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'id': self.identity,
            'id_city': self.id_city
        })
