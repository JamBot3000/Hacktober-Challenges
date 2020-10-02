import csv

file = open("text.csv",'w')
writer = csv.writer(file, ',')
inputData = input("Enter your data ")
lst = list(inputData)
with file:
    write = csv.writer(file)
    write.writerows(lst)
