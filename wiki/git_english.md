# [Linux] Bash git uso: Control de versiones y gestión de código

## Overview
The `git` command is a powerful version control system used to track changes in source code during software development. It allows multiple developers to collaborate on projects, manage revisions, and maintain a history of changes.

## Usage
The basic syntax of the `git` command is as follows:

```bash
git [options] [arguments]
```

## Common Options
- `clone`: Create a copy of a remote repository.
- `commit`: Record changes to the repository.
- `push`: Upload local repository content to a remote repository.
- `pull`: Fetch and integrate changes from a remote repository.
- `status`: Show the working tree status.
- `branch`: List, create, or delete branches.

## Common Examples
Here are some practical examples of using the `git` command:

1. **Cloning a repository:**
   ```bash
   git clone https://github.com/user/repo.git
   ```

2. **Checking the status of your repository:**
   ```bash
   git status
   ```

3. **Adding changes to staging:**
   ```bash
   git add filename.txt
   ```

4. **Committing changes with a message:**
   ```bash
   git commit -m "Add new feature"
   ```

5. **Pushing changes to a remote repository:**
   ```bash
   git push origin main
   ```

6. **Pulling changes from a remote repository:**
   ```bash
   git pull origin main
   ```

7. **Creating a new branch:**
   ```bash
   git branch new-feature
   ```

8. **Switching to a different branch:**
   ```bash
   git checkout new-feature
   ```

## Tips
- Always write clear commit messages to describe your changes.
- Use branches to work on new features or fixes without affecting the main codebase.
- Regularly pull changes from the remote repository to stay updated with your team's work.
- Use `git status` frequently to keep track of your changes and the state of your repository.