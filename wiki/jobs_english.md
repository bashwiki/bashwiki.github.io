# [Linux] Bash jobs uso: Manage background jobs in the shell

## Overview
The `jobs` command in Bash is used to display the status of jobs that are running in the background or have been stopped in the current shell session. It provides information about each job, including its job number, status, and command line.

## Usage
The basic syntax of the `jobs` command is as follows:

```bash
jobs [options]
```

## Common Options
- `-l`: Show the process IDs (PIDs) of the jobs.
- `-n`: Show only jobs that have changed status since the last notification.
- `-p`: Display only the process IDs of the jobs.

## Common Examples

### Displaying Current Jobs
To see the list of current jobs running in the background:

```bash
jobs
```

### Displaying Jobs with Process IDs
To display the jobs along with their process IDs:

```bash
jobs -l
```

### Displaying Only Changed Jobs
To show only jobs that have changed status since the last command:

```bash
jobs -n
```

### Displaying Only Process IDs
To list only the process IDs of the jobs:

```bash
jobs -p
```

## Tips
- Use `bg %job_number` to resume a stopped job in the background.
- Use `fg %job_number` to bring a background job to the foreground.
- Remember that job numbers are specific to the current shell session; they may change if you open a new terminal or session.