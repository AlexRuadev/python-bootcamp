import csv

data = open('example.csv', encoding='utf-8')

# Convert it into csv data
csv_data = csv.reader(data)

#  reformat into a python object list of lists
data_lines = list(csv_data)

# print(data_lines)

# get our column label
data_lines[0]

# print the number of lines of our csv file
len(data_lines)

for line in data_lines[:5]:
    print(line)


# Grqb 10th column, on the 3rd line
data_lines[10][3]

# all emails, located on line 3
all_emails = []

for line in data_lines[1:15]:
    all_emails.append(line[3])