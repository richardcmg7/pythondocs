class Expert:

    def __init__(self, name, email, phone, id):
        self.name = name
        self.email = email
        self.phone = phone
        self.id = id

    @property
    def display(self):
        print(self.name, self.email, self.phone, self.id)

    def set_phone(self, new_phone):
        pass

    @property
    def get_array(self):
        return ({
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'id': self.id
        })