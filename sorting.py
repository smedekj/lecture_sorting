import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data


def selection_sort(number_array, direction='ascending'):
    l = len(number_array)
    for i in range(l):
        min_max_idx = i
        for num_idx in range(i+1, l):
            if direction == 'ascending':
                if number_array[num_idx] < number_array[min_max_idx]:
                    min_max_idx = num_idx
            elif direction == 'descending':
                if number_array[num_idx] > number_array[min_max_idx]:
                    min_max_idx = num_idx

        number_array[i], number_array[min_max_idx] = number_array[min_max_idx], number_array[i]

    return number_array


def bubble_sort(number_array):
    l = len(number_array)
    for i in range(l-1):
        for x in range(l-i-1):
            if number_array[x] < number_array[x+1]:
                continue
            elif number_array[x] > number_array[x+1]:
                number_array[x], number_array[x+1] = number_array[x+1], number_array[x]

    return number_array


def insertion_sort(number_array):



def main():
    data = read_data('numbers.csv')
    print(data)
    sorted_nums = selection_sort(data['series_1'])
    print(sorted_nums)
    sorted_bubble_nums = bubble_sort(data['series_2'])
    print(sorted_bubble_nums)
    pass


if __name__ == '__main__':
    main()
