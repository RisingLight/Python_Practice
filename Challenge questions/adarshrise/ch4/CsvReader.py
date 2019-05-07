import csv

with open('data.csv') as csvfile:
    readCSV =csv.reader(csvfile,delimiter=',')
    ager=[]
    genderr=[]
    racer=[]
    for row in readCSV:
        age= row[0]
        gender=row[1]
        race=row[2]
        ager.append(age)
        genderr.append(gender)
        racer.append(race)
    print(ager,genderr,racer)
