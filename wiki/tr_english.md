# [리눅스] Bash tr 사용법

## Overview
The `tr` command in Bash is a utility for translating or deleting characters from standard input. It is commonly used for text processing tasks, such as replacing specific characters, removing unwanted characters, or converting text to different cases. The primary purpose of `tr` is to facilitate simple transformations of text streams in a straightforward and efficient manner.

## Usage
The basic syntax of the `tr` command is as follows:

```bash
tr [OPTION]... SET1 [SET2]
```

### Common Options:
- `-d`: Delete characters in SET1, without replacing them.
- `-s`: Squeeze multiple adjacent occurrences of a character in SET1 into a single occurrence.
- `-c`: Complement the first set, meaning it will match all characters not in SET1.
- `-t`: Translate characters in SET1 to those in SET2. If SET2 is shorter than SET1, the last character of SET2 is repeated as necessary.

## Examples

### Example 1: Translating Characters
To replace all lowercase letters 'a' with 'o' in a given input:

```bash
echo "banana" | tr 'a' 'o'
```
**Output:**
```
bonono
```

### Example 2: Deleting Characters
To remove all digits from a string:

```bash
echo "Hello123World456" | tr -d '0-9'
```
**Output:**
```
HelloWorld
```

## Tips
- When using `tr`, remember that it operates on standard input, so you often need to pipe input into it or redirect from a file.
- For more complex text transformations, consider combining `tr` with other text processing tools like `sed` or `awk`.
- Be cautious with the `-c` option, as it can lead to unexpected results if not properly understood. Always test your command with sample data first.
- Use the `-s` option to clean up repeated characters, which can be particularly useful when processing user input or cleaning up data files.