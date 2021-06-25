from src.talents.menu_talents import Menu
from talent_book import TalentBook
import re


def phone_input():
    is_seven_to_ten_number = False
    while not is_seven_to_ten_number:
        talent_phone = input(f'ingresa el número de teléfono: ')
        if (len(talent_phone) >= 7 and len(talent_phone) <= 10):
            is_seven_to_ten_number = True
        else:
            print('El teléfono debe ser de 7 o 10 numeros')
        print('El telefono ingresado es: ' + talent_phone)
    return talent_phone


def email_input():
    isValidInputEmail = False
    # for validating an Email
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    while not isValidInputEmail:
        talent_email = input(f'Ingresa el correo electrónico: ')
        # pass the regular expression
        # and the string in search() method
        if (re.search(regex, talent_email)):
            isValidInputEmail = True
        else:
            print("El formato de correo electrónico es invalido")
    return talent_email


def id_input():
    is_valid_id = False

    while not is_valid_id:
        talent_id = input('Ingresa el número de identificación del' \
                          ' talento: ')
        talent_split = talent_id.split(".")
        if (talent_id.isdigit() and 5 <= len(talent_id) <= 12):
            is_valid_id = True
        else:
            print('La identificación debe ser un numero entre 5' \
                  ' y 11 caracteres. ')
    return talent_id


class TalentsSelected:
    def __init__(self):
        self.talents = []

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
                talent_phone = phone_input()

                # Email input with validation
                talent_email = email_input()

                # Id Input with validation
                talent_id = id_input()

                # Identification city
                talent_id_city = input("Ingresa la ciudad de expedición de la identificación: ")

                talent_book.add(talent_name, talent_email, talent_phone, talent_id, talent_id_city)

            if command == 'ac':
                talent_name = input(f'Ingresa el nombre: ')
                try:
                    idx, talent = talent_book.search(talent_name)
                    talent_book.update(idx, talent)
                except:
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
                        except:
                            print("No es valida la seleccion")
                            # is_valid_talents = False
                    print(f'\n {self.talents}')

            if command == 'l':
                talent_book.show_all()

            if command == 'e':
                talent_email = input(f'Ingresa el correo electrónico: ')
                talent_book.delete(talent_email)

            if command == 's':
                break
        return self.talents

# talentos = TalentsSelected()
# selected_talents = talentos.get_talents_selected()