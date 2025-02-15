# [리눅스] Bash git 사용법

## Overview
The `git` command is a powerful version control system used for tracking changes in source code during software development. It allows multiple developers to work on a project simultaneously without interfering with each other's work. Git provides features such as branching, merging, and version history, making it an essential tool for collaborative software development.

## Usage
The basic syntax for the `git` command is as follows:

```
git [command] [options] [arguments]
```

### Common Options
- `git init`: Initializes a new Git repository in the current directory.
- `git clone [url]`: Creates a copy of an existing repository from a remote source.
- `git add [file]`: Stages changes in the specified file(s) for the next commit.
- `git commit -m "[message]"`: Commits the staged changes to the repository with a descriptive message.
- `git status`: Displays the state of the working directory and staging area.
- `git push [remote] [branch]`: Uploads local repository content to a remote repository.
- `git pull [remote] [branch]`: Fetches and merges changes from a remote repository to the local branch.

## Examples

### Example 1: Initializing a New Repository
To create a new Git repository in your current directory, use the following command:

```bash
git init
```
This command sets up a new `.git` directory, allowing you to start tracking changes in your project.

### Example 2: Cloning an Existing Repository
To clone a repository from a remote source, you can use:

```bash
git clone https://github.com/user/repo.git
```
This command creates a local copy of the specified repository, allowing you to work on it locally.

## Tips
- Always write clear and concise commit messages to describe the changes made. This practice helps maintain a clear project history.
- Use branches to manage different features or bug fixes. This allows you to work on multiple tasks simultaneously without affecting the main codebase.
- Regularly pull changes from the remote repository to stay updated with the latest changes made by other developers.
- Use `git status` frequently to check the state of your working directory and staging area, ensuring you know what changes are staged, unstaged, or untracked.