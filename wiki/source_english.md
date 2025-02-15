# [리눅스] Bash source 사용법

## Overview
The `source` command in Bash is used to execute commands from a file in the current shell environment. This means that any variables, functions, or changes made by the commands in the sourced file will affect the current shell session. The primary purpose of `source` is to load environment variables or functions defined in a script without creating a new subshell, allowing for immediate access to those definitions.

## Usage
The basic syntax for the `source` command is as follows:

```bash
source FILENAME
```

Alternatively, you can use the shorthand dot (`.`) to achieve the same result:

```bash
. FILENAME
```

### Common Options
The `source` command does not have many options, but here are a couple of important points to note:

- If the file specified does not exist or is not readable, `source` will return an error.
- The commands in the sourced file are executed in the current shell context, which means any changes to variables or functions will persist after the command completes.

## Examples

### Example 1: Sourcing a Script to Set Environment Variables
Suppose you have a script named `env_setup.sh` that sets some environment variables:

```bash
# env_setup.sh
export DATABASE_URL="mysql://user:password@localhost/dbname"
export API_KEY="your_api_key_here"
```

You can source this script in your current shell session to set the variables:

```bash
source env_setup.sh
```

After running this command, you can access the environment variables:

```bash
echo $DATABASE_URL
# Output: mysql://user:password@localhost/dbname
```

### Example 2: Sourcing a Script with Functions
You can also use `source` to load functions defined in a script. For example, consider a script named `functions.sh`:

```bash
# functions.sh
greet() {
    echo "Hello, $1!"
}
```

You can source this script and then use the `greet` function:

```bash
source functions.sh
greet "World"
# Output: Hello, World!
```

## Tips
- Always check the existence and readability of the file before sourcing it to avoid runtime errors.
- Use `source` for configuration files or scripts that you want to run in the current shell context, especially when working with environment variables or functions.
- Consider using a dedicated directory for your scripts and configuration files to keep your workspace organized.
- Remember that changes made by sourced scripts will persist in your current shell session, so be cautious with scripts that modify existing variables or functions.