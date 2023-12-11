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


index = input("Enter the index name for pivot table (Case Sensitive) : ")
columns = input("Enter the column name for pivot table (Case Sensitive) : ")
values = input("Enter the Value name for pivot table (Case Sensitive) : ")

# Ask the user to choose a function for the pivot table (Sum / Average / Both)

function = str(input("Sum / Average / both : ")).lower()


# Convert user input to valid pivot table aggregation function

if function == 'sum' : 
    function = 'sum'
elif function == 'average' or function == 'mean' : 
    function = 'mean'
elif function == 'both' : 
    function = ['sum','mean']
else : 
    print("Enter Valid Option") 
