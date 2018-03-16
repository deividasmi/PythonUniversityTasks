from datetime import datetime
import sys


data = []
results = []
header = []



def read_header():
    file = open("input01.csv", "r")
    header_string = next(file)
    header = header_string.strip().split(',')
    return header


def read_file(data):
    file = open("input01.csv", "r")
    header_string = next(file)
    file_data = file.readlines()
    #print(file_data[0])
    for line in file_data:

        array = line.strip().split(',')
        data.append(array)
    file.close()


def task_a(header):
    temp = []
    for element in header:
        element = element[:1].upper() + element[1:]
        #print(element)
        temp.append(element)
    #print(temp)
    return temp


def task_b(data, results, column=2, sort_type="ends", string_part="INC"):
    results.append(data[0])
    for line in data:
        element = line[column - 1]
        if sort_type is "ends":
            if element[len(element)-3:] == string_part:
                results.append(line)


def task_c(results, column=7, element_type="date", sort_type="ASC"):
    #print(len(results))
    #print(results[1][column-1])
    if element_type is "date":
        sorted(results, key=lambda x: datetime.strptime(x[column-1], "%Y-%m-%d"))


def task_d(results, header, column1=8, column2=22):
    header[column1 - 1], header[column2 -1] = header[column2 - 1], header[column1 -1]
    for lines in results:
        lines[column1 - 1], lines[column2 - 1] = lines[column2 - 1], lines[column1 - 1]
        #print(lines)


def write_file(results, header):
    file = open("output01_[1612801].txt", "w")
    file.write('\t'.join(header))
    file.write('\n')
    for line in results:
        file.write('\t'.join(line))
        file.write('\n')
    #print(newline)
    file.close()


header = read_header()
read_file(data)
header = task_a(header)
#print(header)
task_b(data, results)
task_c(results)
#task_d(results, header, 8, 22)
write_file(results, header)
for rez_line in data:
    print(rez_line)


