from src.talents.talent import Talent
import csv
import os


class TalentBook:
    
    def __init__(self):
        self._talents = []

    def add(self, name, email, phone, identity, id_city):
        talent = Talent(name, email, phone, identity, id_city)
        self._talents.append(talent)
        self._save()
    
    def select(self, identity):
        for idx, talent in enumerate(self._talents):
            if idx == identity:
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
        with open('./src/talents/talents.csv', 'r') as f:
            reader = csv.reader(f)
            for idx, row in enumerate(reader):
                if idx == 0:
                    continue
                self.add(row[0], row[1], row[2], row[3], row[4])
        return

    def search(self, name):
        find = 0
        temp = []
        for idx, expert in enumerate(self._talents):
            talent_str = expert.__str__()
            if name in talent_str:
                print(talent_str)
                temp.append(name)
                find += 1
        print(find)
        if find == 0:
            self._not_found()
            return
        else:
            return temp

    def update(self, idx, talent):
        already_updated = False
        while not already_updated:
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
                os.system('cls')
                print(f'\n\tLa acción {item} no existe')
            self._talents[idx] = talent
            print('\nContacto actualizado con exito.')
            self._save()

    def _save(self):
        with open('./src/talents/talents.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'email', 'phone', 'id', 'id_city'))

            for talent in self._talents:
                writer.writerow((talent.name, talent.email, talent.phone, talent.identity, talent.id_city))
            
    def __print_talent(self, talent):
        print('--- * --- * --- * --- * --- * --- *')
        print('Nombre: {}'.format(talent.name))
        print('Correo electrónico: {}'.format(talent.email))
        print('Teléfono: {}'.format(talent.phone))
        print('Identificación: {}'.format(talent.identity))
        print('--- * --- * --- * --- * --- * --- *')
    
    def __print_list_talent(self, idx, talent):
        print(f'|  {idx}  | {talent.name}  |  {talent.email} | ')

    def _not_found(self):
        print('*******')
        print('! No encontrado')
        print('*******')
        return


if __name__ == '__main__':
    talents = TalentBook()
    talents.add("Richard", "rcsaavedra@sena.edu.co", "3506764164", "14397755", 'Ibague')
    talents.add("Camilo", "rcsaavedra@sena.edu.co", "3506764164", "14397755", 'Neiva')
    talents.add("Saavedra", "rcsaavedra@sena.edu.co", "3506764164", "14397755", 'pereira')
    talents.show_list()
    print(talents.search('3506764164'))
# talentos = TalentBook()
# selected_talents = talentos.show_list()