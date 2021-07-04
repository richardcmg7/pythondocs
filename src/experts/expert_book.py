from src.experts.expert import Expert
import csv


class ExpertBook:
    
    def __init__(self):
        self._experts = []

    def add(self, name, email, phone, identity):
        expert = Expert(name, email, phone, identity)
        self._experts.append(expert)
        self._save()
    
    def select(self, ident):
        for idx, expert in enumerate(self._experts):
            if idx == ident:
                return expert
            else: 
                print('El "ID" ingresado no esta en la lista')

    def show_all(self):
        for expert in self._experts:
            # print(expert)
            self.__print_expert(expert)
        print("Se han mostrado todos los expertos")
        print("Puedes utilizar 'show_list()' para mostrarlo mas compacto")
        input("Presiona una tecla para continuar")

    def show_list(self):
        print('|  Id |   Nombre  | Correo electrónico')
        for idx, expert in enumerate(self._experts):
            self.__print_list_expert(idx, expert)
        print("Se han mostrado todos los expertos".center(50, '-'))
        input("Presiona una tecla para continuar")

    def delete(self, email):
        for idx, expert in enumerate(self._experts):
            if expert.email.lower() == email.lower():
                del self._experts[idx]
                self._save()
                break

    @property
    def get_csv(self):
        with open('src/experts/experts.csv', 'r') as f:
            reader = csv.reader(f)
            for idx, row in enumerate(reader):
                if idx == 0:
                    continue
                self.add(row[0], row[1], row[2], row[3])
        
    def search(self, name):
        find = 0
        temp = []
        for idx, expert in enumerate(self._experts):
            print()
            if expert.name.lower() == name.lower() or expert.email.lower() == name.lower():
                print('Experto que coincide con la busqueda')
                print(expert)
                temp.append(expert)
                # self.__print_expert(expert)
                # return idx, expert
                find += 1
        
        if find == 0:
            self._not_found()
        
        else:
            return temp

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
        with open('src/experts/experts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'email', 'phone', 'id'))

            for expert in self._experts:
                writer.writerow((expert.name, expert.email, expert.phone, expert.identity))

    def __print_expert(self, expert):
        print('Experto'.center(50, "*"))
        print('Nombre: {}'.format(expert.name))
        print('Correo electrónico: {}'.format(expert.email))
        print('Teléfono: {}'.format(expert.phone))
        print('Identificación: {}'.format(expert.identity))
        print('*'.center(50, "*"))

    def __print_list_expert(self, idx, expert):
        print(f'|  {idx}  | {expert.name}  |  {expert.email} | ')

    def _not_found(self):
        print('*'.center(50, "*"))
        print(' No encontrado '.center(50, "-"))
        print('*'.center(50, "*"))


if __name__ == '__main__':
    experts = ExpertBook()
    experts.add("Richard", "rcsaavedra@sena.edu.co", "3506764164", "14397755")
    experts.add("camilo", "rcsaavedra@sena.edu.co", "3506764164", "14397755")
    experts.add("Saavedra", "richardc7@misena.edu.co", "3506764164", "14397755")
    # experts.show_list()
    # experts.show_all()
    experts_finded = experts.search('rcsaavedra@sena.edu.co')
    print(experts_finded)