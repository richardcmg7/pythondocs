#/usr/bin/python3
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm, Inches, Mm, Emu
import random
import csv
import re
import datetime
import matplotlib.pyplot as plt
# from talent_book import TalentBook
from talents_admin import TalentsSelected

def main():
        
    #Import template document
    template = DocxTemplate('infraestructura.docx')
    context = {
        'city': 'Neiva',
        'project_name': project_name,
        'project_manager': "Richard Camilo Saavedra",
        'line': "Tecnologías virtuales",
        'day': day,
        'month': month,
        'year': year,
        'table_talents': talents,
        }
    #Render automated report
    template.render(context)
    template.save('infraestructura_report.docx')

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

def request_talents():
    talent_quantity = int(input('Cuantos talentos se registrarán en la idea: '))
    table_talents = []
    for i in range (talent_quantity):
        talent_name = input(f'Ingresa el nombre del talento {i+1}: ')
        talent_phone = input(f'ingresa el número de teléfono: ')
        talent_id = input(f'Ingresa la Identificacion del talento {i+1}: ')
        table_talents.append({
            'index': i+1,
            'talent': talent_name,
            'phone': talent_phone,
            'id': talent_id
        })
        print(table_talents)

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
    return table_talents

## Start program
if __name__ == "__main__":
    # print('*********************')
    # project_name = input('Ingresa el nombre del proyecto: ')
    # print('*********************')
    # project_code = input('Ingresa el código del proyecto: ')
    # print('*********************')
    # day, month, year = date_select()
    # Request Talents talents
    talentos = TalentsSelected()
    talentos.select_talent()
    print(talentos)

    #talents  = request_talents()
    #main()
    #print('Documento generado')