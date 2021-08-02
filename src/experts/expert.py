from src.persons.Person import Person


class Expert(Person):
    count = 0

    def __init__(self, name, email, phone, identity, id_city=""):
        Person.__init__(self, name, email, phone, identity, id_city)

    @classmethod
    def show_count(cls):
        print(f'Hay {cls.count}')


if __name__ == '__main__':
    experto1 = Expert('Richard Saavedra',
                      'r@r.com',
                      '3506764164',
                      14397755,
                      "Ibagué - Tolima")
    print(experto1)

    # Using class methods to define several way to receive the data
    # Diccionario
    data_expert = {'name': 'Saavedra',
                   'email': 'r@r.com',
                   'phone': '3506764164',
                   'identity': 14397755,
                   'id_city': "Ibagué - Tolima"}
    experto2 = Expert.from_dict(data_expert)
    print(experto2)

    # String
    data_expert = 'Richard, r@r.com, 3506764164, 14397755, Santa rosa de cabal'
    experto3 = Expert.from_str(data_expert)
    print(experto3)
