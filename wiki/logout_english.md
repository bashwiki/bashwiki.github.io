# [리눅스] Bash logout 사용법

## Overview
The `logout` command is used in Bash to terminate a login shell session. Its primary purpose is to log out the user from the current shell session, effectively closing the terminal window or returning to the previous shell if nested. This command is particularly useful when working in multi-user environments or when you want to ensure that your session is securely closed.

## Usage
The basic syntax of the `logout` command is simply:

```bash
logout
```

This command does not take any options or arguments. It is important to note that `logout` can only be used in a login shell. If you attempt to use it in a non-login shell, you will receive an error message indicating that the command is not valid.

## Examples

### Example 1: Logging Out from a Terminal Session
To log out from a terminal session, simply type the following command:

```bash
logout
```

Upon executing this command, the current session will be terminated, and you will be returned to the login prompt or the previous shell.

### Example 2: Using `logout` in a Nested Shell
If you have opened a new shell session within an existing terminal, you can log out of the nested session by typing:

```bash
bash  # Start a new shell
# ... perform some tasks ...
logout  # Log out of the nested shell
```

This will close the nested shell and return you to the previous shell session.

## Tips
- Always ensure that you save your work before using the `logout` command, as it will terminate the session immediately.
- If you are using a graphical terminal emulator, closing the terminal window will also log you out of the session, but using `logout` ensures that all processes are properly terminated.
- If you encounter an error stating that `logout` is not a valid command, check if you are in a login shell. You can start a login shell by using the command `bash --login`.

By following these guidelines, you can effectively manage your Bash sessions and ensure a secure logout process.