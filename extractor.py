import pandas 
import sys,os
#import pandas for data processing
# Ask the user to input the Excel file name

xl_file = input("Enter the Excel file name : ")
xl_file=str(xl_file) 


try : 
    df = pandas.read_excel(f'{xl_file}')
except : 
    print("Enter Valid FileName")
    exit()
    


index = input("Enter the index name for pivot table (Case Sensitive) : ")
columns = input("Enter the column name for pivot table (Case Sensitive) : ")
values = input("Enter the Value name for pivot table (Case Sensitive) : ")


function = str(input("Sum / Average / both : ")).lower()




if function == 'sum' : 
    function = 'sum'
elif function == 'average' or function == 'mean' : 
    function = 'mean'
elif function == 'both' : 
    function = ['sum','mean']
else : 
    print("Enter Valid Option") 


index = str(index).rstrip()
columns = str(columns).rstrip()
values = str(values).rstrip()


try : 
    pt = df.pivot_table(index=index , columns=columns ,values =values ,aggfunc=function)
except : 
    print("Enter Valid Pivot table Values")
    exit()



file_name = os.path.dirname((sys.executable))


f_path = os.path.join(file_name,f'pivot-table{xl_file}')

# Print a success message with the file path

convert_pivot = pt.to_csv(f_path)