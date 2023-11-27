# excel_to_pivot_table_convertor
The "Excel Pivot Table Generator" simplifies creating pivot tables from Excel. Users input the file name, and the script reads it into Pandas. They then specify index, columns, and values, with choices for sum, average, or both as aggregation functions.


# Excel Pivot Table Generator

## Overview

The "Excel Pivot Table Generator" is a Python script designed to simplify the creation of pivot tables from Excel data. Users are guided through the process, inputting the Excel file name and specifying pivot table components. The script offers choices for aggregation functions, including sum, average, or both.

## Functionality

### Input Excel File
Users input the name of the Excel file they want to analyze.

### Read Excel Data
The script attempts to read the specified Excel file into a Pandas DataFrame. If the file is not found, users are prompted to enter a valid file name.

### Specify Pivot Table Components
Users provide names for the index, columns, and values of the desired pivot table. These names are case-sensitive.

### Choose Aggregation Function
Users select the aggregation function for the pivot table, choosing from sum, average, or both.

### Generate Pivot Table
The script creates the pivot table using the specified components and aggregation function. Invalid input values prompt the user for corrections.

### Save Pivot Table to CSV
The resulting pivot table is converted to a CSV file and saved in the same directory as the Python script. The file is named "pivot-table-[original Excel file name].csv".

## Technical Aspects

- **Input Validation:** Ensures valid file names and pivot table components are provided by the user.

- **Dynamic File Path:** The resulting pivot table CSV file is saved in the same directory as the Python executable, providing convenience and a clear reference point.

## User Interaction

The script engages users through interactive input prompts, guiding them through the process of creating a tailored pivot table for data analysis needs.

The "Excel Pivot Table Generator" aims to provide a straightforward and efficient solution for simplifying the creation of pivot tables, a crucial tool for data analysis.
