import csv

with open('loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    #print(csvReader)
    #print(list(csvReader))
    name = []
    status = []
    for row in csvReader:
        name.append(row[0])
        status.append(row[1])
print(name)
print(status)
Index = name.index('Ram')
loanstatus = status[Index]
print('Ram loan status is', loanstatus)


with open('loanapp.csv', 'a') as wFile:
    write = csv.writer(wFile)
    write.writerow(['Bob', 'Rejected'])