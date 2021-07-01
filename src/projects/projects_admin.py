from src.projects.menu_projects import MenuProjects
from src.projects.project_book import ProjectBook


class ProjectsAdmin:
    def __init__(self):
        self.project = []

    def select_project(self):
        project_book = ProjectBook()
        project_book.get_csv
        menu = MenuProjects()
        while True:
            print('*------*------*------*------*')
            print("Proyecto seleccionado: \n")
            for p in self.project:
                p.display

            print(menu.list_options)
            command = str(input(''))
            if command == 'a':
                # Name input
                project_name = input(f'Ingresa el nombre del proyecto: ')

                project_id = input(f'Ingresa el identificador del proyecto: ')

                project_date = input(f'Ingresa la fecha de inicio del proyecto YYYY-MM-dd: ')

                project_book.add(project_id, project_name, project_date)

            if command == 'ac':
                pass
                # talent_name = input(f'Ingresa el nombre: ')
                # try:
                #     idx, talent = project_book.search(talent_name)
                #     project_book.update(idx, talent)
                # except:
                #     print(f'\nEl talento {talent_name} no fue encontrado\n')

            if command == 'se': 
                self.project = []
                isValidProject = False
                project_book.show_list()
                while not isValidProject:
                    project_selected = input("Seleccionar el identificador del proyecto ej.[1]: ")
                    project_selected = project_selected.split(',')
                    # Validate if talent is ok
                    for p in project_selected:
                        try: 
                            project = project_book.select(int(p))
                            project.display
                            self.project.append(project)
                            isValidProject=True
                        except:
                            print("No es valida la seleccion")

                    print(f'\n {self.project}')

            if command == 'l':
                project_book.show_list()
                input("\nContinuar al menú...")

            if command == 'e':
                project_to_delete = input("Seleccionar el identificador del proyecto a eliminar: ")
                project_book.delete(project_to_delete)
                
            if command == 's':
                break
        return self.project


## Main to test program
if __name__ == '__main__':
    project = ProjectsAdmin()
    selected = project.select_project()
    print(selected)