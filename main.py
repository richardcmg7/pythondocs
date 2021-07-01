#/usr/bin/python3

from docxtpl import DocxTemplate
import datetime
from src.projects.projects_admin import ProjectsAdmin
from main_menu import MainMenu
# from talent_book import TalentBook
from src.talents.talents_admin import TalentsSelected
from src.experts.experts_admin import ExpertsSelected


def infraestructura(name, talents):
    # Import template document
    template = DocxTemplate('templates/infraestructura.docx')
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
    template.save('./generated/infraestructura_document.docx')


def confidencialidad(project, talents, experts):
    # Import template document
    print(project)
    template = DocxTemplate('templates/confidencialidad.docx')
    context = {
        'city': 'Neiva',
        'project_name': project[0].name,
        'project_id': project[0].id,
        'project_manager': "Richard Camilo Saavedra",
        'line': "Tecnologías virtuales",
        'day': day,
        'month': month,
        'year': year,
        'titular_name': talents[0]['name'],
        'titular_id': talents[0]['id'],
        'titular_id_city': talents[0]['id_city'],
        'inter_name': talents[1]['name'],
        'inter_id': talents[1]['id'],
        'inter_id_city': talents[1]['id_city'],
        'ejecutor_name': talents[2]['name'],
        'ejecutor_id': talents[2]['id'],
        'ejecutor_id_city': talents[2]['id_city'],
        'table_experts': experts
    }
    # Render automated report
    template.render(context)
    template.save('./generated/confidencialidad_document.docx')


def date_select():
    data = input('Deseas usar la fecha actual? [S] o [N]: ')
    if data == "S" or data == "s":
        months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        day = datetime.datetime.now().strftime('%d')
        month = months[int(datetime.datetime.now().month)-1]
        year = datetime.datetime.now().strftime('%Y')
    else:
        date_entry = input('Ingresa fecha  con formato YYYY-MM-DD: ')
        year, month, day = map(int, date_entry.split('-'))
    return day, month, year


## Start program
if __name__ == "__main__":
    print('*********************************************')
    print('*********************************************')
    print('Listo vamos a generar los documentos de fase de inicio')
    print('Selecciona los documentos que se quieren generar')
    while True:
        main = MainMenu()
        print(main.list_options)
        command = str(input(''))

        if command == 's':
            break

        if command == 'a':
            print('\nEsta bien... Ahora generemos un proyecto...\n')
            project = ProjectsAdmin()
            project_selected = project.select_project()

            # Admin date
            day, month, year = date_select()

            # Admin Talents
            print("Ahora vamos a gestionar los talentos que estarán en el documento")
            talentos = TalentsSelected()
            selected_talents = talentos.get_talents_selected()

            # Admin Experts
            experts = ExpertsSelected()
            selected_experts = experts.get_experts_selected()

            # To document generate function
            confidencialidad(project_selected, selected_talents, selected_experts)
            print('Documento generado')

        if command == 'm':
            # Project Admin - Create Project instance
            # Admin Project

            print('\nEsta bien... Ahora generemos un proyecto...\n')
            project = ProjectsAdmin()
            project_selected = project.select_project()

            # Admin date
            day, month, year = date_select()
            # Admin Talents
            print("Ahora vamos a gestionar los talentos que estarán en el documento")
            talentos = TalentsSelected()
            selected = talentos.get_talents_selected()

            # To document generate function
            infraestructura(project_selected[0].name, selected)
            print('Documento generado')

        if command == 'am':
            pass
        


