# [Linux] Bash tr Usage equivalent in English: Translate or delete characters

## Overview
The `tr` command in Bash is a utility that translates or deletes characters from standard input. It is commonly used for tasks such as changing case, removing unwanted characters, or replacing specific characters in text streams.

## Usage
The basic syntax of the `tr` command is as follows:

```bash
tr [options] [arguments]
```

## Common Options
- `-d`: Deletes characters specified in the arguments.
- `-s`: Squeezes multiple adjacent occurrences of a character into a single occurrence.
- `-c`: Complements the set of characters specified in the arguments, meaning it operates on all characters except those listed.

## Common Examples

1. **Convert lowercase to uppercase:**
   ```bash
   echo "hello world" | tr 'a-z' 'A-Z'
   ```
   This command converts all lowercase letters in the input string to uppercase.

2. **Delete specific characters:**
   ```bash
   echo "hello 123" | tr -d '0-9'
   ```
   This example removes all digits from the input string, resulting in "hello ".

3. **Squeeze multiple spaces:**
   ```bash
   echo "hello    world" | tr -s ' '
   ```
   This command replaces multiple spaces with a single space, outputting "hello world".

4. **Complement a character set:**
   ```bash
   echo "hello world!" | tr -c 'a-zA-Z ' '*'
   ```
   This replaces all characters that are not letters or spaces with an asterisk, resulting in "hello world*".

5. **Replace characters:**
   ```bash
   echo "hello world" | tr 'l' 'x'
   ```
   This command replaces all occurrences of the letter 'l' with 'x', producing "hexxo worxd".

## Tips
- Always test your `tr` command with sample input to ensure it behaves as expected.
- Use `echo` or `cat` to pipe text into `tr` for quick testing.
- Combine `tr` with other commands using pipes to create powerful text processing workflows.