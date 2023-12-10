import pandas 
import sys,os
#import pandas for data processing
# Ask the user to input the Excel file name

xl_file = input("Enter the Excel file name : ")
xl_file=str(xl_file) 

# Try to read the Excel file, exit if the file is not found

try : 
    df = pandas.read_excel(f'{xl_file}')
except : 
    print("Enter Valid FileName")
    exit()
    
# Ask the user to input names for pivot table index, columns, and values
