#/usr/bin/python3

from docxtpl import DocxTemplate, InlineImage
import datetime
from projects_admin import ProjectsAdmin
from main_menu import MainMenu
# from talent_book import TalentBook
from talents_admin import TalentsSelected

def infraestructura(name, talents):
    #Import template document
    template = DocxTemplate('infraestructura.docx')
    context = {
        'city': 'Neiva',
        'project_name': name,
        'project_manager': "Richard Camilo Saavedra",
        'line': "Tecnologías virtuales",
        'day': day,
        'month': month,
        'year': year,
        'table_talents': talents,
        }
    #Render automated report
    template.render(context)
    template.save('infraestructura_document.docx')

def date_select():
    date_select = input('Deseas usar la fecha actual? [S] o [N]: ')
    if date_select == "S" or date_select == "s":
        months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        day = datetime.datetime.now().strftime('%d')
        month = months[int(datetime.datetime.now().month)-1]
        year = datetime.datetime.now().strftime('%Y')
    else:
        date_entry = input('Ingresa fecha  con formato YYYY-MM-DD: ')
        year, month, day = map(int, date_entry.split('-'))
    return day, month, year

    # table_talents = [
    #     { 
    #         'index': 1,
    #         'talent': 'Daniel Martinez',
    #         'phone': '3506764164'
    #     },
    #     {
    #         'index': 2,
    #         'talent': 'Mario Santos',
    #         'phone': '350435543'
    #     }
    # ]

## Start program
if __name__ == "__main__":
    print('*********************************************')
    print('*********************************************')
    print('Listo vamos a generar los documentos de fase de inicio')
    print('Selecciona los documentos que se quieren generar')
    while True:
        main = MainMenu()
        command = main.list_options

        if command == 'a':
            pass    

        if command == 'm':
            # Project Admin - Create Project instance
            print('\nEsta bien... Ahora generemos un proyecto...\n')
            # project_name = input('Ingresa el nombre del proyecto: ')
            # print('*********************')
            # project_code = input('Ingresa el código del proyecto: ')
            # print('*********************')
            # project = Project(project_code,project_name)
            project = ProjectsAdmin()
            project_selected = project.select_project()
            print(project_selected[0].display)
            # day, month, year = date_select()
            # print("Ahora vamos a gestionar los talentos que estarán en el documento")
            # talentos = TalentsSelected()
            # selected = talentos.get_talents_selected()
            # print(selected)
            # infraestructura(project_name, selected)

        if command == 'am':
            pass
        
        if command == 's':
            break

    #print('Documento generado')