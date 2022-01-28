# **FILE GENERATOR**

**Генератор файлов из шаблона**

Исполняемый файл **genfile**

```
genfile.py [-h] [-r [result]] [-e [env]] template
```

## КЛЮЧИ:

**-h**  справка

**-r**  директория для сохранения сгенерированных файлов. Если не указывать сохранит в директорию artifacts

**-e**  переменные для шаблона. Можно передавать файл в формате YAML или в командной строке. Если аргумент не указан, тогда программа будет искать в директории templates/ файл формата name_template.env. Если файл не будет найден тогда файл будет создан из шаблона без переменных 
Формат для передачи через cli описан ниже.

**template**  путь до файла шаблона, либо имя шаблона расположенного в папке templates.

## ПРИМЕРЫ:

Пусть файл шаблона расположен в директории source/template/example_1.template, переменные для шаблона source/template/example_1.template.env, относительно genfile.py

```
python genfile.py example_2.txt
```
Найдёт example_2.txt в директории source/template/, найдёт файл с переменными example_1.template.env в той же директории и сгенерирует файлы в директорию по умолчанию artifacts

```
python genfile.py -esource/template/universal_env example_2.txt
```

Найдёт example_2.txt в директории source/template/, найдёт файл с переменными source/template/universal_env и сгенерирует файлы в директорию по умолчанию artifacts

```
python genfile.py "-e{\$main\$:{\$result_file\$: example_2.txt, \$range\$: {1: {site: www.example, admin_panel: admin.example}}}}" -r/home/milkyway/tmp /home/milkyway/Templates/example_2.txt
```

Найдёт example_2.txt в директории /home/milkyway/Templates/, переменные получит из аргумента -e и сгенерирует файлы в директорию /home/milkyway/tmp.

## ПРИМЕР ФАЙЛА С ПЕРЕМЕННЫМИ В ФОРМАТЕ YAML:
```
$main$:
    $default$:
        $result_file$: example_default_$i$.txt
        site: www.example_default.com
        admin_panel: admin.example_default.com
    $range$: 
        1..5 10:
            $result_file$: example_from_admin_config_$i$.txt
            site: www.example_$i$
            admin_panel: admin.example
        20..30:
            $result_file$: example_config_$i$.txt
            site: www.example_$i$
            admin_panel: admin.example
            shop: shop.example
        31:
            shop: shop.example
            admin_panel: admin.example_shop.com  
```
**$main$** - точка входа, программа читает только то что внутри, весь остальной документ игнорируется

**$default$** - секуция default добавляет параметры ко всем **$range$**. Эти параметры можно переопределить внутри **$range$**

**$result_file$** - содержит имя файла который будет сгенерирован

**$range$** - указывает количество создаваемых файлов. В примере будет создано 16 файлов с разным содержимым для диапазонов '1..5 10' и '20..30'. Если нужно создать один файл, нужно просто указать одну цифру.

**$i$** - итерация по range. В примере $i$ будет принимать значение 1, 2, 3, 4, 5, 10, 20, 21, 22, 23, 24, 25

всё что внутри диапазонов ('1..5 10' и '20..30') является переменными которые используются в шаблоне

```
name_variable: value
name_variable_1:
    name_variable_2: value
```

В шаблоне переменная будет обозначаться как **{{name_variable}}**

Также поддерживается вложенность которая обозначается как **{{name_variable_1.name_variable_2}}**

$i$ в шаблоне обозначатся как **{{i}}**

## ПРИМЕР ПЕРЕДАЧИ ПЕРЕМЕННЫХ ЧЕРЕЗ CLI:
```
"-e{\$main\$:{\$result_file\$: example_2.txt, \$range\$: {1: {site: www.example, admin_panel: admin.example}}}}"
```

**-e** - аргумент

**$** - необходимо экранировать символом  \

**{}** - начало и конец любого блока


```
{
    \$main\$:
    {
        \$result_file\$: example_2.txt, 
        \$range\$: 
        {
            1: 
                {
                    site: www.example, admin_panel: admin.example}
                }
        }
}

#аналогичный пример в формате YAML

$main$:
    $result_file$: example_2.txt 
    $range$: 
        1: 
            site: www.example
            admin_panel: admin.example
```

## ПРИМЕР ШАБЛОНА jinja2:
```
      # example{{i}}
      - {{site}}.ru                CNAME   188.188.188.188
      - {{admin_panel}}{{i}}.ru         CNAME   {{site}}.ru.
      {% if shop %}
       - {{shop}}_{{i}}.ru                CNAME   {{site}}.ru
      {% endif %}
```


___________________________________________________________________________

! ! ! РАБОТАЕТ ТОЛЬКО НА PYTHON 3.Х ! ! !

___________________________________________________________________________








