import csv
import argparse
import os.path
from os import path

parser = argparse.ArgumentParser(description='Append user input to separate fields to an existing csv file')
parser.add_argument('csv',type=str, help="Path to the CSV file to extend with user input")

args = parser.parse_args()
args = vars(args)

csvFilename = args.get("csv")

fieldAmount = 0
delimter = ";"
csvHeader = None
fieldNames = None
csvDialect = None
csvLineToWrite = {}
requestUserInput = True

#Check if csv exists (if not exit)
if path.exists(csvFilename) == False:
    print("Couldn't find csv File")
    exit(0)


# read header
with open(csvFilename, "r") as csvFileHandler:
    reader = csv.reader(csvFileHandler)
    for csvHeader in reader:
        break
    sniffer = csv.Sniffer()
    csvDialect = sniffer.sniff(csvHeader[0])
    delimiter = csvDialect.delimiter
    fieldNames = csvHeader[0].split(delimiter)


#CSV Writer
with open(csvFilename, 'a', newline="") as csvFileHandler:
    writer = csv.DictWriter(csvFileHandler,fieldnames = fieldNames, delimiter = delimiter, dialect=csvDialect)

    while requestUserInput:
        #Get user input  
        for field in fieldNames:
            userIn = input("Input value '"+field+": ")
            csvLineToWrite[field] = userIn

        #Append input to CSV
        writer.writerow(csvLineToWrite)
        print("Row appended.\n")

        #Ask user if he likes to add another row
        reqNextRow = True
        while reqNextRow:
            userIn = input("Do you like to add another row? (y/n)")
            if userIn == "Y" or userIn == "y":
                requestUserInput = True
                reqNextRow = False
            if userIn == "N" or userIn == "n":
                requestUserInput = False
                reqNextRow = False