import csv

with open('user.csv','r',encoding="utf-8",newline='') as myFile:
    lines=csv.reader(myFile)
    for line in lines:
        print(line)
myFile.close()

with open('user.csv','a',encoding="utf-8",newline='') as myFile2:
    sample = ['mango','23456']
    csv_writer = csv.writer(myFile2)
    csv_writer.writerow(sample)