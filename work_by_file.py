from typing import Optional, Iterable

from functions import filter_query, map_query, unique_query, sort_query, limit_query

#словарик с фильтрами
CMD_TO_FUNCTION = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query,
}


class WorkByFile:
    def read_file(self, file_name: str):
        """Читаем файл с помощью гернератора"""
        with open(file_name) as file:
            for row in file:
                yield row

    def query(self, cmd, value, data: Optional[Iterable[str]]):
        """применяем заданные фильты к файлу"""
        if data is None:
            prepared_data = self.read_file('./data/apache_logs.txt')
        else:
            prepared_data = data
        result = CMD_TO_FUNCTION[cmd](param=value, data=prepared_data)
        return list(result)
