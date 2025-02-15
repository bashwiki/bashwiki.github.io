# [리눅스] Bash uuidgen 사용법

## Overview
`uuidgen` is a command-line utility in Linux that generates universally unique identifiers (UUIDs). UUIDs are 128-bit values that are used to uniquely identify information in computer systems. The primary purpose of `uuidgen` is to create these identifiers, which can be useful in various applications such as database keys, session identifiers, and more, ensuring that the generated values are unique across different systems and time.

## Usage
The basic syntax of the `uuidgen` command is as follows:

```bash
uuidgen [OPTION]
```

### Common Options
- `-r`, `--random`: Generate a random UUID.
- `-s`, `--sha1`: Generate a UUID based on the SHA-1 hash of a namespace identifier and a name.
- `-n`, `--namespace`: Specify a namespace for the SHA-1 UUID generation.
- `-h`, `--help`: Display help information about the command and its options.

If no options are provided, `uuidgen` will generate a random UUID by default.

## Examples

### Example 1: Generate a Random UUID
To generate a random UUID, simply run the command without any options:

```bash
uuidgen
```

**Output:**
```
3f6b4c2e-8e8f-4d7b-8b5c-3d8c4e2f8b6e
```

### Example 2: Generate a UUID Based on SHA-1
To generate a UUID based on a specific namespace and name, you can use the `--namespace` option along with the `--sha1` option. For example:

```bash
uuidgen --namespace=6ba7b810-9dad-11d1-80b4-00c04fd430c8 --sha1
```

**Output:**
```
f47ac10b-58cc-4372-a567-0e02b2c3d479
```

## Tips
- When generating UUIDs for database keys, ensure that you use the random option to avoid collisions.
- If you need to generate UUIDs in a script, consider capturing the output of `uuidgen` into a variable for further processing.
- Always check for the latest version of `uuidgen` as there may be updates or additional options available that can enhance its functionality.