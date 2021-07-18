from src.talents.menu_talents import Menu
from src.talents.talent_book import TalentBook
import re


class TalentsSelected:
    def __init__(self):
        self.talents = []
        self.talent_phone = ""
        self.talent_id = ""
        self.talent_email = ""

    def get_talents_selected(self):
        selected = []
        talents = self.select_talent()
        for idx, t in enumerate(talents):
            data = t.get_array
            data['index'] = idx + 1
            selected.append(data)
        return selected

    def select_talent(self):
        talent_book = TalentBook()
        talent_book.get_csv
        menu = Menu()
        while True:
            print('*------*------*------*------*')
            print("Talentos seleccionados: \n")
            for t in self.talents:
                t.display

            print(menu.list_options)
            command = str(input(''))
            if command == 'a':
                # Name input
                talent_name = input(f'Ingresa el nombre del talento: ')
                # Phone input with validation
                talent_phone = self.phone_input()

                # Email input with validation
                talent_email = self.email_input()

                # Id Input with validation
                talent_id = self.id_input()

                # Identification city
                talent_id_city = input("Ingresa la ciudad de expedición de la identificación: ")

                talent_book.add(talent_name, talent_email, talent_phone, talent_id, talent_id_city)

            if command == 'ac':
                talent_name = input(f'Ingresa el nombre: ')
                try:
                    idx, talent = talent_book.search(talent_name)
                    talent_book.update(idx, talent)
                except ValueError:
                    print(f'\nEl talento {talent_name} no fue encontrado\n')

            if command == 'b':
                talent_name = input(f'Ingresa el nombre: ')
                talent_book.search(talent_name)

            if command == 'se':
                self.talents = []
                is_valid_talents = False
                talent_book.show_list()
                while not is_valid_talents:
                    talent_selected = input("Seleccione los talentos por ID ej.[ 1,4 ]: ")
                    talent_selected = talent_selected.split(',')
                    # Validate if talent is ok
                    for t in talent_selected:
                        try:
                            talent = talent_book.select(int(t))
                            talent.display
                            self.talents.append(talent)
                            is_valid_talents = True
                        except ValueError:
                            print("No es valida la seleccion")
                            # is_valid_talents = False
                    print(f'\n {self.talents}')

            if command == 'l':
                talent_book.show_all()

            if command == 'e':
                talent_email = input(f'Ingresa el correo electrónico: ')
                talent_book.delete(talent_email)

            if command == 's':
                for t in self.talents:
                    t.display
                break
        return self.talents

    def phone_input(self):
        is_seven_to_ten_number = False
        while not is_seven_to_ten_number:
            self.talent_phone = input(f'ingresa el número de teléfono: ')
            if 7 <= len(self.talent_phone) <= 10:
                is_seven_to_ten_number = True
            else:
                print('El teléfono debe ser de 7 o 10 numeros')
            print('El telefono ingresado es: ' + self.talent_phone)
        return self.talent_phone

    def email_input(self):
        is_valid_input_email = False
        # for validating an Email
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

        while not is_valid_input_email:
            self.talent_email = input(f'Ingresa el correo electrónico: ')
            # pass the regular expression
            # and the string in search() method
            if re.search(regex, self.talent_email):
                is_valid_input_email = True
            else:
                print("El formato de correo electrónico es invalido")
        return self.talent_email

    def id_input(self):
        is_valid_id = False
    
        while not is_valid_id:
            self.talent_id = input('Ingresa el número de identificación del'
                              ' talento: ')
            talent_split = self.talent_id.split(".")
            if self.talent_id.isdigit() and 5 <= len(self.talent_id) <= 12:
                is_valid_id = True
            else:
                print('La identificación debe ser un numero entre 5'
                      ' y 11 caracteres. ')
        return self.talent_id


# For testing purpose
if __name__ == '__main__':
    selected = TalentsSelected()
    selected.select_talent()
