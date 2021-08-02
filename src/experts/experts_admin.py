from src.experts.menu_experts import MenuExperts
from src.experts.expert_book import ExpertBook
import re


class ExpertsSelected:
    def __init__(self):
        self.experts = []
        self.talent_phone = ""
        self.talent_email = ""
        self.talent_id = ""

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
                try:
                    t.display
                except AttributeError:
                    self.experts = []
                    print("Se ha seleccionado un Id que no esta en lista")

            print(menu.list_options)
            command = str(input(''))
            if command == 'a':
                # Name input
                expert_name = input(f'Ingresa el nombre del experto: ')
                # Phone input with validation
                expert_phone = self.phone_input()

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
                except ValueError:
                    print(f'\nEl experto {expert_name} no fue encontrado\n')

            if command == 'b':
                expert_name = input(f'Ingresa el nombre: ')
                expert_book.search(expert_name)

            if command == 'se':
                self.experts = []
                is_valid_experts = False
                expert_book.show_list()
                while not is_valid_experts:
                    expert_selected = input("Seleccione los expertos por ID ej.[ 1,4 ]: ")
                    expert_selected = expert_selected.split(',')
                    # Validate if expert is ok
                    for t in expert_selected:
                        try:
                            expert = expert_book.select(int(t))
                            try:
                                expert.display
                            except AttributeError:
                                self.experts = []
                                print("El ID seleccionado 'NO' corresponde a un experto")
                            self.experts.append(expert)
                            is_valid_experts = True
                        finally:
                            print("No es valida la seleccion")
                            # is_valid_experts = False
                    print(f'\n {self.experts}')

            if command == 'l':
                expert_book.show_all()

            if command == 'e':
                expert_email = input(f'Ingresa el correo electrónico: ')
                expert_book.delete(expert_email)

            if command == 's':
                print("Has salido sin experto seleccionado") if len(self.experts) == 0 else ""
                for e in self.experts:
                    e.display
                break

        return self.experts

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
            self.talent_id = input('Ingresa el número de identificación del talento: ')
            self.talent_id = self.talent_id.replace(".", "")
            if self.talent_id.isdigit() and 5 <= len(self.talent_id) <= 12:
                is_valid_id = True
            else:
                print('La identificación debe ser un numero entre 5 y 11 caracteres. ')
        return self.talent_id


# For testing purpose
if __name__ == '__main__':
    selected = ExpertsSelected()
    selected.select_expert()
