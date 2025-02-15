# [리눅스] Bash jq 사용법

## Overview
`jq` is a powerful command-line tool for processing and manipulating JSON (JavaScript Object Notation) data. It allows users to parse, filter, and transform JSON data structures in a simple and efficient way. With `jq`, engineers and developers can easily extract specific data from JSON files, format the output, and perform complex queries, making it an essential tool for working with APIs and configuration files that use JSON.

## Usage
The basic syntax of the `jq` command is as follows:

```bash
jq [options] 'filter' [file...]
```

### Common Options:
- `-c`: Compact output instead of pretty-printed.
- `-r`: Output raw strings, not JSON-encoded strings.
- `-f <file>`: Read the filter from a file instead of the command line.
- `-s`: Read all inputs into an array and apply the filter to that array.
- `--arg name value`: Pass a variable into the filter.

## Examples

### Example 1: Simple JSON Parsing
Suppose you have a JSON file named `data.json` with the following content:

```json
{
  "name": "Alice",
  "age": 30,
  "city": "Wonderland"
}
```

To extract the `name` field from this JSON file, you can use the following command:

```bash
jq '.name' data.json
```

**Output:**
```
"Alice"
```

### Example 2: Filtering an Array
Consider a JSON array in a file named `users.json`:

```json
[
  { "name": "Alice", "age": 30 },
  { "name": "Bob", "age": 25 },
  { "name": "Charlie", "age": 35 }
]
```

To filter users who are older than 30, you can use:

```bash
jq '.[] | select(.age > 30)' users.json
```

**Output:**
```json
{
  "name": "Charlie",
  "age": 35
}
```

## Tips
- Use the `-r` option when you want to output raw strings instead of JSON-encoded strings. This is particularly useful when you want to use the output in shell scripts.
- For complex queries, consider writing your filters in a separate file and using the `-f` option to keep your command line clean and manageable.
- Familiarize yourself with the `jq` filter syntax, as it allows for powerful data manipulation capabilities, including mapping, reducing, and grouping data.
- Test your `jq` commands with smaller JSON samples to ensure your filters work as expected before applying them to larger datasets.