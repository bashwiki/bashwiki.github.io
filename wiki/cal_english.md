# [Linux] Bash cal Uso equivalente: Display a calendar

## Overview
The `cal` command in Bash is used to display a calendar in the terminal. It can show the current month's calendar or any specified month and year, making it a handy tool for quick date references.

## Usage
The basic syntax of the `cal` command is as follows:

```bash
cal [options] [month] [year]
```

## Common Options
- `-1`: Display a single month (default).
- `-3`: Display the previous, current, and next month.
- `-m`: Start the week on Monday.
- `-y`: Display the entire year.
- `-A [num]`: Show the specified number of months after the current month.
- `-B [num]`: Show the specified number of months before the current month.

## Common Examples
Here are some practical examples of using the `cal` command:

1. **Display the current month's calendar:**
   ```bash
   cal
   ```

2. **Display a specific month and year (e.g., March 2023):**
   ```bash
   cal 03 2023
   ```

3. **Display the calendar for the entire year (e.g., 2023):**
   ```bash
   cal -y 2023
   ```

4. **Display the previous, current, and next month:**
   ```bash
   cal -3
   ```

5. **Display the current month starting on Monday:**
   ```bash
   cal -m
   ```

## Tips
- Use the `-A` and `-B` options to quickly see upcoming or past months without specifying exact dates.
- Combine options for more customized views, such as `cal -m -3` to see the previous, current, and next month starting on Monday.
- Remember that the `cal` command is a great way to quickly reference dates without needing to open a calendar application.