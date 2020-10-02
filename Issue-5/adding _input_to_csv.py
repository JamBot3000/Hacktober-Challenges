#This is a python script which takes input from console and writes it to csv file
import csv 
fields = ['Name', 'Mobile', 'Email', 'Country'] 
  
# data rows of csv file 
name=input("enter name : ")
mobile=input("enter mobile : ")
email=input("enter email : ")
country=input("enter country: ")

row=[name,mobile,email,country]
  
# name of csv file 
filename = "records.csv"
  
# writing to csv file 
with open(filename, 'w') as csvfile: 
    
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields)  
    csvwriter.writerow(row)
