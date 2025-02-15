# [리눅스] Bash column 사용법

## Overview
The `column` command in Bash is a utility that formats text input into a well-structured table. Its primary purpose is to take a list of data and align it into columns, making it easier to read and analyze. This command is particularly useful when dealing with output from other commands or files that contain delimited data, as it helps to present the information in a more organized manner.

## Usage
The basic syntax of the `column` command is as follows:

```bash
column [options] [file]
```

### Common Options
- `-t`: This option tells `column` to create a table by determining the number of columns based on the input data. It will automatically adjust the width of each column to fit the content.
- `-s CHAR`: This option allows you to specify a custom delimiter (CHAR) that separates the columns in the input data. The default delimiter is whitespace.
- `-n`: Prevents the command from treating the input as a table, which can be useful for formatting without alignment.

## Examples

### Example 1: Basic Column Formatting
Suppose you have a text file named `data.txt` with the following content:

```
Name Age City
Alice 30 NewYork
Bob 25 LosAngeles
Charlie 35 Chicago
```

You can format this data into aligned columns using the following command:

```bash
column -t < data.txt
```

**Output:**
```
Name     Age  City      
Alice    30   NewYork   
Bob      25   LosAngeles 
Charlie  35   Chicago    
```

### Example 2: Using a Custom Delimiter
If you have a CSV file named `data.csv` with the following content:

```
Name,Age,City
Alice,30,NewYork
Bob,25,LosAngeles
Charlie,35,Chicago
```

You can format this data using a comma as the delimiter:

```bash
column -t -s, < data.csv
```

**Output:**
```
Name     Age  City      
Alice    30   NewYork   
Bob      25   LosAngeles 
Charlie  35   Chicago    
```

## Tips
- When using `column`, always ensure that your input data is consistently formatted. Inconsistent spacing or delimiters can lead to misalignment in the output.
- For large datasets, consider piping the output of other commands into `column` to quickly format the results. For example, you can use `ps aux | column -t` to format the output of running processes.
- If you need to export the formatted output to a file, you can redirect the output using `>` like so: `column -t < data.txt > formatted_data.txt`.

By utilizing the `column` command effectively, you can enhance the readability of your data and streamline your workflow in the terminal.