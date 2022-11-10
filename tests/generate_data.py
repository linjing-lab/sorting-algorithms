# load import dependencies
import codecs
import random
import csv

# generate data
data = [[random.randint(0, 10) for _ in range(1000)] for _ in range(10000)]

def data_write_csv(file_name: str, datas: list):
    file_csv = codecs.open(file_name, 'w+', 'utf-8') # append
    writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for data in datas:
        writer.writerow(data)
    print("Success!")

data_write_csv('tests/data.csv', data)