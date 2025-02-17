# [Linux] Bash svn Uso: Version control for files and directories

## Overview
The `svn` command is a part of Subversion, a version control system that allows users to manage changes to files and directories over time. It helps in tracking revisions, collaborating with others, and maintaining a history of changes.

## Usage
The basic syntax of the `svn` command is as follows:

```bash
svn [options] [arguments]
```

## Common Options
- `checkout`: Download a working copy from a repository.
- `commit`: Send changes from the working copy to the repository.
- `update`: Synchronize the working copy with the repository.
- `add`: Schedule files or directories for addition to the repository.
- `delete`: Remove files or directories from the repository.
- `status`: Show the status of files in the working copy.
- `log`: Display the commit history for a repository.

## Common Examples
Here are some practical examples of using the `svn` command:

### Checking Out a Repository
To create a local copy of a repository, use the `checkout` command:

```bash
svn checkout https://example.com/svn/myproject/trunk
```

### Committing Changes
After making changes to your files, you can commit them to the repository:

```bash
svn commit -m "Fixed a bug in the application"
```

### Updating Your Working Copy
To update your local copy with the latest changes from the repository, use:

```bash
svn update
```

### Adding a New File
To add a new file to the repository, first create the file, then use:

```bash
svn add newfile.txt
```

### Deleting a File
To remove a file from the repository, use the `delete` command:

```bash
svn delete oldfile.txt
```

### Checking the Status
To see which files have been modified, added, or deleted, run:

```bash
svn status
```

### Viewing Commit History
To view the commit history of the repository, use:

```bash
svn log
```

## Tips
- Always update your working copy before making changes to avoid conflicts.
- Use meaningful commit messages to describe your changes clearly.
- Regularly check the status of your working copy to keep track of modifications.
- Consider branching for significant changes to avoid disrupting the main project.