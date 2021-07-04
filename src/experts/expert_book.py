from src.experts.expert import Expert
import csv


class ExpertBook:
    
    def __init__(self):
        self._experts = []

    def add(self, name, email, phone, id):
        expert = Expert(name, email, phone, id)
        self._experts.append(expert)
        self._save()
    
    def select(self, id):
        for idx, expert in enumerate(self._experts):
            if idx == id:
                return expert
            else: 
                print('El "ID" ingresado no esta en la lista')
                

    def show_all(self):
        for expert in self._experts:
            # print(expert)
            self.__print_expert(expert)

    def show_list(self):
        print('|  Id |   Nombre  | Correo electrónico')
        for idx, expert in enumerate(self._experts):
            self.__print_list_expert(idx, expert)

    def delete(self, email):
        for idx, expert in enumerate(self._experts):
            if expert.email.lower() == email.lower():
                del self._experts[idx]
                self._save()
                break
    @property
    def get_csv(self):
        with open('./src/experts/experts.csv', 'r') as f:
            reader = csv.reader(f)
            for idx, row in enumerate(reader):
                if idx == 0:
                    continue
                self.add(row[0],row[1],row[2], row[3])
        
    def search(self, name):
        for idx, expert in enumerate(self._experts):
            if expert.name.lower() == name.lower():
                print('Se ha encontrado el(los) experto(s)')
                self.__print_expert(expert)
                return idx, expert
        else: 
            self._not_found()

    def update(self, idx, expert):
        already_updated = False
        while not already_updated:
            item = str(input('''
            Qué deseas actualizar? presione [6] para actualizar:
            [1] Nombre
            [2] Correo electrónico
            [3] Teléfono
            [4] Identificación
            [5] Todo
            ---> '''))
            if item == "1":
                expert.name = str(input("Escribe el nuevo nombre: "))
            if item == "2":
                expert.email = str(input("Escribe el nuevo correo electrónico: "))
            if item == "3":
                expert.phone = str(input("Escribe el nuevo teléfono: "))
            if item == "4":
                expert.id = str(input("Escribe la nueva identificación: "))
            if item == "5":
                expert.name = str(input("Escribe el nuevo nombre: "))
                expert.email = str(input("Escribe el nuevo correo electrónico: "))
                expert.phone = str(input("Escribe el nuevo teléfono: "))
                expert.id = str(input("Escribe la nueva identificación: "))
            elif item == "6":
                break
            else:
                print(f'\n\tLa acción {item} no existe')
            self._experts[idx] = expert
            print('\nContacto actualizado con exito.')
            self._save()

    def _save(self):
        with open('./src/experts/experts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'email', 'phone', 'id'))

            for expert in self._experts:
                writer.writerow((expert.name, expert.email, expert.phone, expert.id))

    def __print_expert(self, expert):
        print('--- * --- * --- * --- * --- * --- *')
        print('Nombre: {}'.format(expert.name))
        print('Correo electrónico: {}'.format(expert.email))
        print('Teléfono: {}'.format(expert.phone))
        print('Identificación: {}'.format(expert.id))
        print('--- * --- * --- * --- * --- * --- *')

    def __print_list_expert(self, idx, expert):
        print(f'|  {idx}  | {expert.name}  |  {expert.email} | ')

    def _not_found(self):
        print('*******')
        print('! No encontrado')
        print('*******')

# experts = ExpertBook()
# experts.add("Richard", "rcsaavedra@sena.edu.co", "3506764164", "14397755")
# experts.add("Camilo", "rcsaavedra@sena.edu.co", "3506764164", "14397755")
# experts.add("Saavedra", "rcsaavedra@sena.edu.co", "3506764164", "14397755")
# experts.show_list()