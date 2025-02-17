# [리눅스] Bash kill 사용법: 프로세스 종료

## Overview
`kill` 명령어는 특정 프로세스를 종료하는 데 사용됩니다. 이 명령어는 프로세스 ID(PID)를 기반으로 작동하며, 시스템에서 실행 중인 프로세스를 제어하는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:

```
kill [options] [arguments]
```

## Common Options
- `-l`: 신호 목록을 표시합니다.
- `-s SIGNAL`: 특정 신호를 지정하여 프로세스를 종료합니다.
- `-n NUMBER`: 신호 번호를 사용하여 프로세스를 종료합니다.

## Common Examples
- 특정 PID를 가진 프로세스를 종료하기:
  ```bash
  kill 1234
  ```

- 특정 신호를 사용하여 프로세스를 종료하기 (예: SIGTERM):
  ```bash
  kill -s SIGTERM 1234
  ```

- 모든 프로세스를 종료하기 (예: SIGKILL):
  ```bash
  kill -9 1234
  ```

- 현재 실행 중인 프로세스의 PID를 찾고 종료하기:
  ```bash
  ps aux | grep myprocess
  kill <PID>
  ```

## Tips
- `kill` 명령어를 사용할 때는 종료하려는 프로세스의 PID를 정확히 확인하세요.
- 신호를 지정할 때는 기본적으로 SIGTERM이 사용되지만, 필요에 따라 SIGKILL을 사용할 수 있습니다. SIGKILL은 프로세스를 강제로 종료하므로 주의가 필요합니다.
- 시스템 관리자 권한이 필요한 프로세스를 종료하려면 `sudo`를 사용할 수 있습니다.