import csv

name = "test.csv"


while True:
    fields = input("add 3 fields: ").split()

    if len(fields) < 3:
        print("please add more 3 fields..")

    else:
        with open(name, 'a') as f:
            wr = csv.writer(f)
            wr.writerow(fields)
