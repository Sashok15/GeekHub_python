import os
import re
import csv

path_reports = "C:/Users/sashok/GeekHub/GeekHub_python/HT_4/reports"

if not os.path.exists(path_reports):
    os.makedirs(path_reports)

with open("openerp-server.log", "r") as f:
    all_log = f.read()
    pattern = re.compile('(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),(\d{,3} \d{,5}) (WARNING|ERROR|CRITICAL) (.+)')
    result = pattern.findall(all_log)

title_col = ['line_id', 'marker', 'date_time', 'description']
path = "reports/all_data.csv"
with open(path, "w", newline='') as f:  # create  file all_data.csv
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(title_col)
    line_id = 1
    for line in result:
        # add rows in our csv-file [line_id, marker, date_time, description]
        list_col = [line_id, line[2], line[0], line[3]]
        writer.writerow(list_col)
        line_id += 1

# count unique rows
unique_list = []
for i in result:
    counter = 0
    for j in result:
        if i[-1] == j[-1]:
            counter += 1
    row_list = (counter, i[2], i[0], i[3])
    unique_list.append(row_list)

# find unique description
unique_desc = []
for i in range(len(unique_list)):
    unique_desc.append(unique_list[i][-1])
unique_desc = set(unique_desc)

# find unique rows and compare them
unique = []
for i in unique_desc:
    for j in unique_list:
        if i in j[-1]:
            unique.append(j)
            break

title_col = ['count', 'marker', 'date_time', 'description']
path = "reports/unique.csv"
with open(path, "a", newline='') as f:  # write unique rows in unique.csv
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(title_col)
    for line in unique:
        list_col = [line[0], line[1], line[2], line[3]]
        writer.writerow(list_col)
