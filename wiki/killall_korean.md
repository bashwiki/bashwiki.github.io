# [리눅스] Bash killall 사용법: 프로세스 종료

## Overview
`killall` 명령은 지정된 이름의 모든 프로세스를 종료하는 데 사용됩니다. 이 명령은 프로세스의 PID(프로세스 ID)를 알 필요 없이 프로세스 이름만으로 작업할 수 있어 유용합니다.

## Usage
기본 구문은 다음과 같습니다.

```bash
killall [옵션] [프로세스 이름]
```

## Common Options
- `-u, --user <사용자>`: 특정 사용자가 소유한 프로세스만 종료합니다.
- `-q, --quiet`: 종료할 프로세스가 없을 경우 오류 메시지를 표시하지 않습니다.
- `-I, --ignore-case`: 프로세스 이름의 대소문자를 구분하지 않습니다.
- `-s, --signal <신호>`: 종료할 때 보낼 신호를 지정합니다. 기본값은 `TERM`입니다.

## Common Examples
- 모든 `firefox` 프로세스 종료하기:
  ```bash
  killall firefox
  ```

- 특정 사용자(`user1`)의 모든 `python` 프로세스 종료하기:
  ```bash
  killall -u user1 python
  ```

- 대소문자 구분 없이 `httpd` 프로세스 종료하기:
  ```bash
  killall -I httpd
  ```

- `SIGKILL` 신호를 사용하여 `myapp` 프로세스 강제 종료하기:
  ```bash
  killall -s KILL myapp
  ```

## Tips
- `killall` 명령을 사용할 때는 프로세스 이름을 정확히 입력해야 합니다. 잘못된 이름을 입력하면 아무런 작업도 수행되지 않습니다.
- 중요한 프로세스를 종료하기 전에 항상 확인하세요. 실수로 시스템 프로세스를 종료하면 시스템에 문제가 발생할 수 있습니다.
- `killall` 명령은 여러 프로세스를 동시에 종료할 수 있으므로, 여러 프로세스 이름을 공백으로 구분하여 나열할 수 있습니다.