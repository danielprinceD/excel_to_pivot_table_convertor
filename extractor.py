import pandas 
import sys,os

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

# Remove any trailing whitespaces from the user input

index = str(index).rstrip()
columns = str(columns).rstrip()
values = str(values).rstrip()

# Try to create a pivot table, exit if the pivot table values are invalid

try : 
    pt = df.pivot_table(index=index , columns=columns ,values =values ,aggfunc=function)
except : 
    print("Enter Valid Pivot table Values")
    exit()


# Define the file path for saving the pivot table CSV file

file_name = os.path.dirname((sys.executable))

# Convert the pivot table to CSV and save it to the specified file path

f_path = os.path.join(file_name,f'pivot-table{xl_file}')

# Print a success message with the file path

convert_pivot = pt.to_csv(f_path)