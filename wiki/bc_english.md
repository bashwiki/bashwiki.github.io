# [리눅스] Bash bc 사용법

## Overview
The `bc` command in Bash stands for "Basic Calculator." It is an arbitrary precision calculator language that allows users to perform mathematical calculations in a command-line environment. `bc` is particularly useful for engineers and developers who need to handle complex calculations or require precision beyond standard floating-point arithmetic. It supports various mathematical operations, including addition, subtraction, multiplication, division, and more advanced functions like square roots and trigonometric calculations.

## Usage
The basic syntax for using `bc` is as follows:

```bash
bc [options] [file]
```

### Common Options:
- `-l`: Loads the standard math library, which provides additional mathematical functions such as sine, cosine, and logarithm.
- `-q`: Suppresses the introductory message and prompts, providing a quieter interface.
- `-e`: Allows you to execute a command directly from the command line without entering the interactive mode.

## Examples

### Example 1: Basic Arithmetic
To perform a simple arithmetic calculation, you can echo a command into `bc`:

```bash
echo "5 + 3" | bc
```
This command will output `8`, which is the result of adding 5 and 3.

### Example 2: Using the Math Library
To calculate the square root of a number using the math library, use the `-l` option:

```bash
echo "scale=2; sqrt(16)" | bc -l
```
This command will output `4.00`, where `scale=2` specifies that the result should be displayed with two decimal places.

## Tips
- **Setting Scale**: The `scale` variable determines the number of decimal places for division operations. Set it at the beginning of your calculation to control precision.
  
  ```bash
  echo "scale=4; 10 / 3" | bc
  ```
  This will output `3.3333`.

- **Using Variables**: You can assign values to variables in `bc` for more complex calculations:

  ```bash
  echo "a=5; b=10; a + b" | bc
  ```
  This will output `15`.

- **Interactive Mode**: You can enter `bc` without any arguments to start an interactive session, allowing you to perform calculations directly:

  ```bash
  bc
  ```
  Then you can enter expressions line by line.

By utilizing `bc`, engineers and developers can efficiently perform calculations directly from the command line, making it a powerful tool for scripting and automation tasks.