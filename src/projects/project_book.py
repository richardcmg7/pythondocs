from src.projects.project import Project
import csv
import os

class ProjectBook:

    def __init__(self):
        self._projects = []

    def add(self, idx, name, date):
        project = Project(idx, name, date)
        self._projects.append(project)
        self._save()
    
    def select(self, id):
        # [ project if id==idx else self._not_found for idx, project in enumerate(self._projects) ]
        for idx, project in enumerate(self._projects):
            if id == idx + 1:
                return project
        else:
            self._not_found()

    def show_all(self):
        for project in self._projects:
            # print(project)
            self.__print_project(project)

    def show_list(self):
        print('|  Id |   Nombre  del proyecto | Fecha')
        for idx, project in enumerate(self._projects):
            self.__print_list_project(idx+1, project)

    def delete(self, id):
        for idx, project in enumerate(self._projects):
            if project.id == id:
                del self._projects[idx]
                self._save()
                break
        else:
            self._not_found()
    
    @property
    def get_csv(self):
        with open('./src/projects/projects.csv', 'r') as f:
            reader = csv.reader(f)
            for idx, row in enumerate(reader):
                if idx == 0:
                    continue
                self.add(row[0],row[1],row[2])
        
    def search(self, name):
        for idx, project in enumerate(self._projects):
            if project.name.lower() == name.lower():
                print('Se ha encontrado el(los) projecto(s)')
                self.__print_project(project)
                return idx, project
        else: 
            self._not_found()

    def update(self, idx, project):
        alreadyUpdated = False
        while not alreadyUpdated :
            item = str(input('''
            Qué deseas actualizar? presione [6] para actualizar:
            [1] Nombre
            [2] Código del proyecto
            [3] fecha
            [4] Todo
            [5] Salir
            --->'''))
            if item == "1":
                project.name = str(input("Escribe el nuevo nombre: "))
            if item == "2":
                project.id = str(input("Escribe el nuevo código del proyecto: "))
            if item == "3":
                project.date = str(input("Escribe la nueva fecha: "))
            if item == "4":
                project.name = str(input("Escribe el nuevo nombre: "))
                project.id = str(input("Escribe el nuevo código del proyecto: "))
                project.date = str(input("Escribe la nueva fecha: "))
                
            elif item == "5":
                break
            else:
                os.system ('cls')
                print(f'\n\tLa acción {item} no existe')
            self._projects[idx] = project
            print('\nContacto actualizado con exito.')
            self._save()

    def _save(self):
        with open('./src/projects/projects.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('ID proyecto', 'Nombre del proyecto', 'fecha de registro'))

            for project in self._projects:
                writer.writerow((project.id, project.name, project.date))
            
    def __print_project(self, project):
        print('--- * --- * --- * --- * --- * --- *')
        print('Id del proyecto: {}'.format(project.id))
        print('Nombre del proyecto: {}'.format(project.name))
        print('Fecha: {}'.format(project.date))
        print('--- * --- * --- * --- * --- * --- *')
    
    def __print_list_project(self, idx, project):
        print(f'| {idx} | {project.id}  | {project.name}  |  {project.date} | ')

    def _not_found(self):
        print('*******')
        print('! No encontrado')
        print('*******')


if __name__ == '__main__':
    project_book = ProjectBook()
    project_book.add('P-043','Este es el proyecto 1','2021-05-12')
    project_book.add('P-044','Este es el proyecto 1','2021-05-13')
    project_book.add('P-045','Este es el proyecto 1','2021-05-21')
    # # project_book.get_csv
    project_book.show_list()
    # data = input('Write Id del proyecto to delete: ')
    # project_book.delete(data)
    # project_book.show_list()
    select = project_book.select(1)
    print(select.display)