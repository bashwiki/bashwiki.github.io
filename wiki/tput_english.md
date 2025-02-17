# [Linux] Bash tput Uso: Control terminal display settings

## Overview
The `tput` command is used in Bash to initialize and manipulate terminal settings. It allows users to control various aspects of terminal behavior, such as text formatting, cursor movement, and color output. This command is particularly useful for creating visually appealing scripts and enhancing user interfaces in the terminal.

## Usage
The basic syntax of the `tput` command is as follows:

```bash
tput [options] [arguments]
```

## Common Options
- `setaf [n]`: Set the foreground color to the color represented by the number `n`.
- `setab [n]`: Set the background color to the color represented by the number `n`.
- `clear`: Clear the terminal screen.
- `cup [y] [x]`: Move the cursor to the specified position, where `y` is the row and `x` is the column.
- `bold`: Set the text to bold.
- `rev`: Reverse the foreground and background colors.

## Common Examples
Here are some practical examples of using the `tput` command:

### Change Text Color
To change the text color to red:

```bash
tput setaf 1
echo "This text is red"
tput sgr0  # Reset to default
```

### Clear the Screen
To clear the terminal screen:

```bash
tput clear
```

### Move the Cursor
To move the cursor to the 5th row and 10th column:

```bash
tput cup 5 10
echo "Cursor moved here"
```

### Set Bold Text
To print bold text:

```bash
tput bold
echo "This text is bold"
tput sgr0  # Reset to default
```

### Change Background Color
To change the background color to blue and print text:

```bash
tput setab 4
echo "This text has a blue background"
tput sgr0  # Reset to default
```

## Tips
- Always use `tput sgr0` to reset terminal settings after making changes to avoid affecting subsequent output.
- Experiment with different color codes (0-7 for basic colors) to customize your terminal output.
- Combine multiple `tput` commands in a single script to create a more dynamic and visually appealing user interface.