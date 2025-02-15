# [리눅스] Bash tput 사용법

## Overview
`tput` is a command-line utility in Unix-like operating systems that allows users to manipulate terminal capabilities. Its primary purpose is to enable the control of terminal features such as colors, cursor movement, and text formatting. By using `tput`, developers can create more visually appealing and user-friendly command-line interfaces.

## Usage
The basic syntax of the `tput` command is as follows:

```
tput [option] [parameter]
```

### Common Options
- `setaf`: Set the foreground color (text color).
- `setab`: Set the background color.
- `clear`: Clear the terminal screen.
- `cup`: Move the cursor to a specified position (row and column).
- `bold`: Set text to bold.
- `smso`: Start standout mode (usually bold or highlighted text).
- `rmso`: End standout mode.

## Examples
### Example 1: Changing Text Color
To change the text color to green, you can use the following command:

```bash
tput setaf 2; echo "This text is green"; tput sgr0
```
In this example, `setaf 2` sets the text color to green (where `2` represents green), and `sgr0` resets the terminal to its default settings after displaying the message.

### Example 2: Moving the Cursor
To move the cursor to the 5th row and 10th column of the terminal and print a message, you can use:

```bash
tput cup 5 10; echo "Hello, World!"
```
Here, `cup 5 10` moves the cursor to the specified position before printing "Hello, World!".

## Tips
- Always reset terminal settings after using `tput` to avoid leaving the terminal in an unexpected state. Use `tput sgr0` to reset all attributes.
- You can find the numeric values for different colors by using `tput colors`, which returns the number of colors supported by the terminal.
- Combine multiple `tput` commands in a single script to create complex terminal interfaces, but ensure to manage cursor positions and text attributes carefully to avoid confusion.

By utilizing `tput`, you can enhance your command-line applications and scripts, making them more interactive and visually appealing.