
from os import system
from source.rnd import rnd



#exampl 1
#Генерируем множество файлов на основе одного шаблона (можно использовать и несколько шаблонов одновременно)

for num in range(101, 105):
    #Заполняем справочник с переменными из шаблона
    if num == 101 or num == 103:
        dict_variable_template = {
            'db_port': '3306',
            'db_hostname': '192.168.0.2',
            'db_user': 'barabashka',
            'db_pass': 'chikibriki'
        }
    else:
        dict_variable_template = {
            'db_port': '3306',
            'db_hostname': '192.168.0.2',
            'db_user': 'barabashka-admin',
            'db_pass': 'chikibrikiblayt'
        }
    s_num = str(num)
    #1. Создаём экзепляр класс rnd, с указанием имени шаблона
    caster = rnd('exampl_1.yaml')
    #2.Заполняем справочник с переменными из шаблона
    dict_variable_template['node_num'] = s_num
    #3.Передаём справочник экзепляру
    caster.set_variable(dict_variable_template)
    #4.Генерируем файл
    caster.cast_file(f'exampl_{s_num}.yaml')
    


#exampl 2
#Заполняем один файл множеством строк 

#1. Создаём экзепляр класс rnd, с указанием имени шаблона
caster = rnd('exampl_2.txt')
#2.Заполняем справочник с переменными из шаблона
dict_variable_template = {'site': 'site', 'admin_panel': 'admin.site'}
#3.Передаём справочник экзепляру
caster.set_variable(dict_variable_template)
#4.Генерируем файл
caster.cast_file('dns_config.txt')

