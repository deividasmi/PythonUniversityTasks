"""Duomenu manipulation module
Deividas Miliauskas IT 3gr. s1612801
Pylint - 9.88/10
"""
from collections import namedtuple
from datetime import datetime


class DataManipulation:
    """Data manipulation class"""
    data_types = dict()
    data = []

    def __init__(self, csv_file):
        """Recognizes column types"""
        header = next(csv_file)
        my_tuple = namedtuple('DataManipulation', header)
        temp_data = []
        for line in csv_file:
            temp_data.append(my_tuple(*line))
            self.data.append(my_tuple(*line))
        for element in header:
            column_type = 'str'
            for line in temp_data:
                try:
                    if datetime.strptime(getattr(line, element), '%Y-%m-%d'):
                        column_type = 'date'
                        break
                except ValueError:
                    column_type = 'str'
                if check_int(getattr(line, element)):
                    column_type = 'int'
                elif getattr(line, element) == '0':
                    column_type = 'int'
                elif check_float(getattr(line, element)):
                    column_type = 'float'
                    break
            self.data_types[element] = column_type

        #print(*header)
        #print(temp_data[5]._fields)
        #print(self.data_types)

    def select(self, *column_names):
        """Select columns by their names"""
        my_data = self.get()
        new_data = []
        #print(self.data[5]._fields)
        header = my_data[5]._fields

        column_names_copy = column_names
        for names_copy in column_names_copy:
            count = 0
            for name in column_names:
                if name == names_copy:
                    count += 1
            if count > 1:
                raise KeyError("Column names repeat")
        new_tuple = namedtuple('DataManipulation', column_names)
        for line in my_data:
            for name in column_names:
                if name in header:
                    new_tuple.name = getattr(line, name)
                else:
                    raise KeyError("No such column")
                new_data.append(new_tuple)
        self.data = new_data

    def get(self, types=False):
        """Returns data or data types saved in dict"""
        if types:
            return self.data_types
        return self.data

    def save(self, csv_file):
        """Saves data"""
        my_data = self.data
        header = my_data[5]._fields
        csv_file.writerow(header)
        for line in my_data:
            csv_file.writerow(line)

    def filter(self, column, operators, attr):
        """Filters by the given operator"""
        my_data = self.get()
        new_data = []
        header = my_data[4]._fields
        if column not in header:
            raise KeyError("No such column")
        for line in my_data:
            if operators(getattr(line, column), attr):
                new_data.append(line)
        self.data = new_data


def check_int(value):
    """Checks if type is int"""
    try:
        if int(value):
            return True
    except ValueError:
        return False


def check_float(value):
    """Checks if type is float"""
    try:
        if float(value):
            return True
    except ValueError:
        return False
