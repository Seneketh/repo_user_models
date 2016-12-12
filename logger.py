import numpy as np
import csv

dictionary_list = []


dictionary_list.append( {'data': 10,'label': 20} )
dictionary_list.append( {'data': 33,'label': 44} )

for n in range(len(dictionary_list)):

    print(dictionary_list[n]['data'])

# as per http://stackoverflow.com/questions/13660240/write-python-dictionary-to-csv-where-where-keys-columns-values-rows


fieldnames = sorted(list(set(k for d in dictionary_list for k in d)))

with open("data.csv", 'w') as out_file:
    writer = csv.DictWriter(out_file, fieldnames=fieldnames, dialect='excel')
    writer.writeheader()
    writer.writerows(dictionary_list)
    
