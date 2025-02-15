# [리눅스] Bash svn 사용법

## Overview
The `svn` command is a part of Subversion, a version control system that allows developers to manage changes to source code over time. It is primarily used for tracking changes in files and directories, enabling multiple users to collaborate on projects efficiently. With `svn`, users can commit changes, revert to previous versions, and manage branches and tags, making it an essential tool for software development and project management.

## Usage
The basic syntax of the `svn` command is as follows:

```
svn [options] <subcommand> [args]
```

### Common Options
- `--help`: Displays help information about the command and its options.
- `-m <message>`: Provides a commit message for the changes.
- `-q`: Runs the command in quiet mode, suppressing output.
- `--username <username>`: Specifies the username for authentication.
- `--password <password>`: Specifies the password for authentication.

### Subcommands
Some common subcommands include:
- `checkout`: Downloads a working copy from a repository.
- `commit`: Sends changes from the working copy to the repository.
- `update`: Updates the working copy with changes from the repository.
- `add`: Adds new files or directories to version control.
- `delete`: Removes files or directories from version control.

## Examples

### Example 1: Checking Out a Repository
To create a local working copy of a repository, use the `checkout` subcommand:

```bash
svn checkout https://example.com/svn/myproject/trunk myproject
```

This command downloads the contents of the `trunk` directory from the specified repository URL into a local directory named `myproject`.

### Example 2: Committing Changes
After making changes to files in your working copy, you can commit those changes back to the repository:

```bash
svn commit -m "Fixed bug in the login feature"
```

This command commits all modified files in the working copy with the provided commit message.

## Tips
- Always update your working copy with `svn update` before starting new changes to ensure you are working with the latest version.
- Use meaningful commit messages to document the changes you make, as this helps collaborators understand the history of the project.
- Consider using `svn status` to check the status of your working copy before committing, as it shows which files have been modified, added, or deleted.
- Familiarize yourself with branching and tagging in Subversion to manage different versions of your project effectively.