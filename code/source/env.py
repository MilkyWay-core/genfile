import yaml

key_words = ['$main$', '$result_file$', '$range$', ]


class envException(Exception):
    pass


class env:
    '''
    класс получает данных из yaml 
    '''

    def __init__(self, loaded_yaml):
        result = yaml.load(loaded_yaml, Loader=yaml.SafeLoader)
        try:
            self._n_env = []
            ranges = result['$main$']['$range$']
            for range_key, range_value in ranges.items():
                nd = _normalized_data()
                nd.result_file = result['$main$']['$result_file$']
                nd.add_normalize_range(range_key)
                nd.data = range_value
                self._n_env.append(nd)
        except KeyError as err:
            raise envException(
                f'Не указаны обязательные переменные $main$, $result_file$, $range$:  {err}')

    def get_data(self):
        """
        возвращает лист с нормализованными данными для каждого range
        """
        return self._n_env


class _normalized_data():
    """
    нормализованные данные готовые к передаче в genfile
    """

    def __init__(self):
        self.result_file = ''
        #dict in dict
        self.range_list = []
        self.data = {}

    def add_normalize_range(self, range_string: str):
        ranges = str(range_string).split(' ')
        for range_element in ranges:
            between = range_element.split('..')
            if len(between) > 2:
                raise envException(
                    'Диапазон range не должен содержать более двух цифр')
            elif len(between) == 1:
                self.range_list.append([int(between[0]), int(between[0])+1])
            elif len(between) == 2:
                if int(between[0]) > int(between[1]):
                    raise envException(
                        'Начальное значение диапазона range не может превышать конечное')
                self.range_list.append([int(between[0]), int(between[1])+1])
            else:
                raise envException('Допущена ошибка в диапазоне $range$')


'''
пусть лежит, рекурсия ещё пригодится для реализации чтения в других форматах
    def _perefix_recurs(self, source, result):
        if type(source) is str or type(source) is int:
            print(f'{list(result.keys())[-1]}:{source}')
            result[list(result.keys())[-1]] = source
        else:
            # запоминаем имя ключа родителя
            last_key = ''
            if result:
                last_key = list(result.keys())[-1]
            for key, value in source.items():
                # если последний ключ не пустой то модернизируем имя ключа
                if last_key:
                    if result[list(result.keys())[-1]] != '':
                        result[last_key+'.'+key] = ''
                    else:
                        result.pop(last_key)
                        result[last_key+'.'+key] = ''
                else:
                    result[key] = ''
                self._perefix_recurs(value, result)
'''
