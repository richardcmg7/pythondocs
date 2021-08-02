from src.persons.Person import Person


class Talent(Person):
    count = 0

    def __init__(self, name, email, phone, identity, id_city):
        Person.__init__(self, name, email, phone, identity, id_city)
        Talent.count += 1

    @classmethod
    def show_count(cls):
        print(f'Hay {cls.count}')


if __name__ == '__main__':
    talento1 = Talent('Richard Saavedra',
                      'r@r.com',
                      '3506764164',
                      14397755,
                      'Ibagué')
    print(talento1)

    # Using class methods to define several way to receive the data
    # Dictionary
    data_talent = {'name': 'Saavedra',
                   'email': 'r@r.com',
                   'phone': '3506764164',
                   'identity': 14397755,
                   'id_city': 'Ibagué'}
    talent_2 = Talent.from_dict(data_talent)
    print(talent_2)
    print(Talent.show_count())

    # String
    data_talent = 'Richard, r@r.com, 3506764164, 14397755,Ibagué'
    talent_3 = Talent.from_str(data_talent)
    print(talent_3)
    print(Talent.show_count())
