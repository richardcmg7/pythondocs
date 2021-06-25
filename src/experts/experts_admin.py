from src.experts.menu_experts import MenuExperts
from expert_book import ExpertBook
import re


def phone_input():
    is_seven_to_ten_number = False
    while not is_seven_to_ten_number:
        talent_phone = input(f'ingresa el número de teléfono: ')
        if 7 <= len(talent_phone) <= 10:
            is_seven_to_ten_number = True
        else:
            print('El teléfono debe ser de 7 o 10 numeros')
        print('El telefono ingresado es: ' + talent_phone)
    return talent_phone


class ExpertsSelected:
    def __init__(self):
        self.experts = []

    def email_input(self):
        is_valid_input_email = False
        # for validating an Email
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

        while not is_valid_input_email:
            talent_email = input(f'Ingresa el correo electrónico: ')
            # pass the regular expression
            # and the string in search() method
            if re.search(regex, talent_email):
                is_valid_input_email = True
            else:
                print("El formato de correo electrónico es invalido")
        return talent_email

    def id_input(self):
        is_valid_id = False

        while not is_valid_id:
            talent_id = input('Ingresa el número de identificación del talento: ')
            talent_id = talent_id.replace(".", "")
            if talent_id.isdigit() and 5 <= len(talent_id) <= 12:
                is_valid_id = True
            else:
                print('La identificación debe ser un numero entre 5 y 11 caracteres. ')
        return talent_id

    def get_experts_selected(self):
        select = []
        experts = self.select_expert()
        for idx, t in enumerate(experts):
            data = t.get_array
            data['index'] = idx + 1
            select.append(data)
        return select

    def select_expert(self):
        expert_book = ExpertBook()
        expert_book.get_csv
        menu = MenuExperts()
        while True:
            print('*------*------*------*------*')
            print("Expertos seleccionados: \n")
            for t in self.experts:
                t.display

            print(menu.list_options)
            command = str(input(''))
            if command == 'a':
                # Name input
                expert_name = input(f'Ingresa el nombre del experto: ')
                # Phone input with validation
                expert_phone = phone_input()

                # Email input with validation
                expert_email = self.email_input()

                # Id Input with validation
                expert_id = self.id_input()

                expert_book.add(expert_name, expert_email, expert_phone, expert_id)

            if command == 'ac':
                expert_book.show_list()
                expert_name = input(f'Ingresa el nombre: ')
                try:
                    idx, expert = expert_book.search(expert_name)
                    expert_book.update(idx, expert)
                except:
                    print(f'\nEl experto {expert_name} no fue encontrado\n')

            if command == 'b':
                expert_name = input(f'Ingresa el nombre: ')
                expert_book.search(expert_name)

            if command == 'se':
                self.experts = []
                isValidexperts = False
                expert_book.show_list()
                while not isValidexperts:
                    expert_selected = input("Seleccione los expertos por ID ej.[ 1,4 ]: ")
                    expert_selected = expert_selected.split(',')
                    # Validate if expert is ok
                    for t in expert_selected:
                        try:
                            expert = expert_book.select(int(t))
                            expert.display
                            self.experts.append(expert)
                            isValidexperts = True
                        finally:
                            print("No es valida la seleccion")
                            # isValidexperts = False
                    print(f'\n {self.experts}')

            if command == 'l':
                expert_book.show_all()

            if command == 'e':
                expert_email = input(f'Ingresa el correo electrónico: ')
                expert_book.delete(expert_email)

            if command == 's':
                break
        return self.experts

# For testing purpose
selected = ExpertsSelected()
selected.select_expert()
