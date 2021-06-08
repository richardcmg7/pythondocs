from talent import Talent
import csv
import re

class TalentBook:
    
    def __init__(self):
        self._talents = []

    def add(self, name, email, phone, id):
        talent = Talent(name, email, phone, id)
        self._talents.append(talent)
        self._save()
    
    def select(self, id):
        for idx, talent in enumerate(self._talents):
            if idx == id:
                return talent
            else: 
                print('El "ID" ingresado no esta en la lista')
                

    def show_all(self):
        for talent in self._talents:
            # print(talent)
            self.__print_talent(talent)

    def show_list(self):
        print('|  Id |   Nombre  | Correo electrónico')
        for idx, talent in enumerate(self._talents):
            self.__print_list_talent(idx, talent)

    def delete(self, email):
        for idx, talent in enumerate(self._talents):
            if talent.email.lower() == email.lower():
                del self._talents[idx]
                self._save()
                break
    @property
    def get_csv(self):
        with open('talents.csv', 'r') as f:
            reader = csv.reader(f)
            for idx, row in enumerate(reader):
                if idx == 0:
                    continue
                self.add(row[0],row[1],row[2], row[3])
        
    def search(self, name):
        for idx, talent in enumerate(self._talents):
            if talent.name.lower() == name.lower():
                print('Se ha encontrado el(los) talento(s)')
                self.__print_talent(talent)
                return idx, talent
        else: 
            self._not_found()

    def update(self, idx, talent):
        alreadyUpdated = False
        while not alreadyUpdated :
            item = str(input('''
            Qué deseas actualizar? presione [6] para actualizar:
            [1] Nombre
            [2] Correo electrónico
            [3] Teléfono
            [4] Identificación
            [5] Todo
            --->'''))
            if item == "1":
                talent.name = str(input("Escribe el nuevo nombre: "))
            if item == "2":
                talent.email = str(input("Escribe el nuevo correo electrónico: "))
            if item == "3":
                talent.phone = str(input("Escribe el nuevo teléfono: "))
            if item == "4":
                talent.id = str(input("Escribe la nueva identificación: "))
            if item == "5":
                talent.name = str(input("Escribe el nuevo nombre: "))
                talent.email = str(input("Escribe el nuevo correo electrónico: "))
                talent.phone = str(input("Escribe el nuevo teléfono: "))
                talent.id = str(input("Escribe la nueva identificación: "))
            elif item == "6":
                break
            else:
                os.system ('cls')
                print(f'\n\tLa acción {item} no existe')
            self._talents[idx] = talent
            print('\nContacto actualizado con exito.')
            self._save()

    def _save(self):
        with open('talents.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'email', 'phone', 'id'))

            for talent in self._talents:
                writer.writerow((talent.name, talent.email, talent.phone, talent.id))
            
    def __print_talent(self, talent):
        print('--- * --- * --- * --- * --- * --- *')
        print('Nombre: {}'.format(talent.name))
        print('Correo electrónico: {}'.format(talent.email))
        print('Teléfono: {}'.format(talent.phone))
        print('Identificación: {}'.format(talent.id))
        print('--- * --- * --- * --- * --- * --- *')
    
    def __print_list_talent(self, idx, talent):
        print(f'|  {idx}  | {talent.name}  |  {talent.email} | ')

    def _not_found(self):
        print('*******')
        print('! No encontrado')
        print('*******')
        