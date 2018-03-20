"""This module reads from csv file data, process it and writes into plain txt file"""
from datetime import datetime


DATA = []
RESULTS = []
HEADER = []
DATA_FILE = "input01.csv"
RESULTS_FILE = "output01_[1612801].txt"


def read_header(data_file):
    """
    reads first line of the file and stores into header's list
    :return:
    """
    datafile = open(data_file, "r")
    header_string = next(datafile)
    header = header_string.strip().split(',')
    return header


def read_file(data, data_file):
    """
    reads csv file and stores all the data in to two dimensional list
    :param data:
    :param data_file
    """
    datafile = open(data_file, "r")
    next(datafile)
    file_data = datafile.readlines()
    for line in file_data:
        array = line.strip().split(',')
        data.append(array)
    datafile.close()


def task_a(header):
    """
    Changes headers first letter to upper
    :param header:
    :return:
    """
    temp = []
    for element in header:
        element = element[:1].upper() + element[1:]
        temp.append(element)
    return temp


def task_b(data, results, column=2, sort_type="ends", string_part="INC"):
    """
    goes through the date and stores lines which satisfies conditions provided by parameters
    :param data:
    :param results:
    :param column:
    :param sort_type:
    :param string_part:
    """
    for line in data:
        element = line[column - 1]
        if sort_type is "ends":
            if element[len(element)-3:] == string_part:
                results.append(line)
        else:
            if element[0:3] == string_part:
                results.append(line)


def task_c(results, column=7, element_type="date", sort_type="ASC"):
    """
    sorts the data using the parameters provided
    :param results:
    :param column:
    :param element_type:
    :param sort_type:
    :return:
    """
    reversal = True
    if sort_type == "ASC":
        reversal = False
    if element_type is "date":
        results = sorted(results, key=lambda x: datetime.strptime(x[column-1], '%Y-%m-%d'),
                         reverse=reversal)
    elif element_type is "float":
        results = sorted(results, key=lambda x: float('-inf') if x[column-1] == ""
                         else float(x[column-1]), reverse=reversal)
    elif element_type is "int":
        results = sorted(results, key=lambda x: int('-inf') if x[column - 1] == ""
                         else int(x[column - 1]), reverse=reversal)
    else:
        results = sorted(results, key=lambda x: x[column-1], reverse=reversal)

    return results


def task_d(results, header, column1=8, column2=22):
    """
    changes two columns positions
    :param results:
    :param header:
    :param column1:
    :param column2:
    """
    header[column1 - 1], header[column2 -1] = header[column2 - 1], header[column1 -1]
    for lines in results:
        lines[column1 - 1], lines[column2 - 1] = lines[column2 - 1], lines[column1 - 1]


def write_file(results, header, results_file, symbol="tab"):
    """
    writes results into file
    :param symbol:
    :param results_file:
    :param results:
    :param header:
    """
    if symbol == "tab":
        rez_file = open(results_file, "w")
        rez_file.write('\t'.join(header))
        rez_file.write('\n')
        for line in results:
            rez_file.write('\t'.join(line))
            rez_file.write('\n')
    else:
        rez_file = open(results_file, "w")
        rez_file.write(symbol.join(header))
        rez_file.write('\n')
        for line in results:
            rez_file.write(symbol.join(line))
            rez_file.write('\n')
    rez_file.close()


HEADER = read_header(DATA_FILE)
read_file(DATA, DATA_FILE)
HEADER = task_a(HEADER)
task_b(DATA, RESULTS)
RESULTS = task_c(RESULTS)
task_d(RESULTS, HEADER)
write_file(RESULTS, HEADER, RESULTS_FILE)
