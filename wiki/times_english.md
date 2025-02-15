# [리눅스] Bash times 사용법

## Overview
The `times` command in Bash is used to display the accumulated user and system times for the current shell and its child processes. This command provides insight into how much CPU time has been consumed by the shell and its subprocesses, which can be particularly useful for performance monitoring and optimization.

## Usage
The basic syntax of the `times` command is simply:

```bash
times
```

This command does not take any options or arguments. When executed, it will output the total user and system time in seconds for the current shell session.

## Examples

### Example 1: Basic Usage
To see the accumulated time for the current shell session, simply run:

```bash
times
```

The output will look something like this:

```
0.00 0.00
```

Here, the first number represents the user time, and the second number represents the system time.

### Example 2: After Running Commands
You can run a few commands and then check the accumulated time. For instance:

```bash
sleep 2
ls
times
```

After executing the `times` command, you might see an output like:

```
0.02 0.01
```

This indicates that the user time was 0.02 seconds and the system time was 0.01 seconds for the commands executed in the current shell session.

## Tips
- Use the `times` command after running a series of commands to gauge their performance impact in terms of CPU time.
- Since `times` only displays the time for the current shell session, consider using it in scripts or interactive sessions where you want to monitor resource usage.
- Remember that the output is cumulative; if you run `times` multiple times, it will show the total time since the last shell session started.

By utilizing the `times` command, developers and engineers can better understand the resource utilization of their scripts and commands, aiding in performance tuning and optimization efforts.