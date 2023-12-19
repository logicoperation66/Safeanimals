import csv

with open("./Kopia BAZA DANYCH SCHRONISKO 2023 - Arkusz19.csv", 'r', encoding="UTF-8") as data:
    reader = csv.reader(data)
    for i in reader:
        print(type(i[4]))
