# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
fileScan= open(csvpath, 'r')  #Opens file
csvreader = csv.reader(csvpath, delimiter=',')
print(csvreader)

#with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    #csvreader = csv.reader(csvfile, delimiter=',')


