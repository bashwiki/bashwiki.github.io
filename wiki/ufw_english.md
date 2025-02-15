# [리눅스] Bash ufw 사용법

## Overview
`ufw` (Uncomplicated Firewall) is a user-friendly command-line interface for managing a netfilter firewall on Linux systems. Its primary purpose is to simplify the process of configuring and managing firewall rules, making it easier for users to secure their systems against unauthorized access while allowing legitimate traffic.

## Usage
The basic syntax for the `ufw` command is as follows:

```
ufw [OPTIONS] [COMMAND]
```

### Common Options
- `enable`: Activates the firewall and applies the current rules.
- `disable`: Deactivates the firewall.
- `status`: Displays the current status of the firewall and its rules.
- `allow [PORT]`: Allows incoming traffic on the specified port.
- `deny [PORT]`: Denies incoming traffic on the specified port.
- `delete [RULE]`: Removes a specified rule from the firewall.
- `logging [on|off|level]`: Enables or disables logging, or sets the logging level.

## Examples

### Example 1: Allowing SSH Traffic
To allow incoming SSH connections (default port 22), you can use the following command:

```bash
sudo ufw allow 22
```

After executing this command, you can check the status of the firewall to confirm that the rule has been added:

```bash
sudo ufw status
```

### Example 2: Blocking a Specific Port
If you want to block incoming traffic on a specific port, for example, port 80 (HTTP), you can run:

```bash
sudo ufw deny 80
```

Again, verify the updated rules with:

```bash
sudo ufw status
```

## Tips
- Always check the status of your firewall after making changes to ensure that the rules are applied correctly.
- Use `ufw logging on` to enable logging, which can help in troubleshooting and monitoring the traffic.
- Consider using `ufw allow from [IP_ADDRESS]` to allow traffic only from specific IP addresses for enhanced security.
- Remember to run `ufw enable` after configuring your rules to activate the firewall.
- Be cautious when enabling or disabling the firewall, especially on remote servers, as it may affect your ability to connect.