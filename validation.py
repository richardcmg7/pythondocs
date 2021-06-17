import re
def phone_input(self):
    is_seven_to_ten_number = False
    while not is_seven_to_ten_number:
        expert_phone = input(f'ingresa el número de teléfono: ')
        if (len(expert_phone) >= 7 and len(expert_phone) <= 10):
            is_seven_to_ten_number = True
        else:
            print('El teléfono debe ser de 7 o 10 numeros')
        print('El telefono ingresado es: ' + expert_phone)
    return expert_phone


def email_input(self):
    isValidInputEmail = False
    # for validating an Email
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    while not isValidInputEmail:
        expert_email = input(f'Ingresa el correo electrónico: ')
        # pass the regular expression
        # and the string in search() method
        if (re.search(regex, expert_email)):
            isValidInputEmail = True
        else:
            print("El formato de correo electrónico es invalido")
    return expert_email


def id_input(self):
    isValidId = False

    while not isValidId:
        expert_id = input('Ingresa el número de identificación del' \
                          ' experto: ')

        if (expert_id.isdigit() and 5 <= len(expert_id) <= 12):
            isValidId = True
        else:
            print('La identificación debe ser un numero entre 5' \
                  ' y 11 caracteres. ')
    return expert_id