# [리눅스] Bash journalctl 사용법: 시스템 로그 보기

## Overview
`journalctl` 명령어는 시스템의 로그 메시지를 조회하는 데 사용됩니다. 이 명령어는 시스템의 상태를 모니터링하고 문제를 해결하는 데 유용합니다. `systemd`의 저널 시스템을 기반으로 하며, 다양한 필터링 옵션을 제공합니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
journalctl [options] [arguments]
```

## Common Options
- `-b`: 현재 부팅 이후의 로그만 표시합니다.
- `-f`: 실시간으로 로그를 추적합니다.
- `--since "시간"`: 지정한 시간 이후의 로그를 표시합니다.
- `--until "시간"`: 지정한 시간 이전의 로그를 표시합니다.
- `-u [서비스명]`: 특정 서비스의 로그만 표시합니다.

## Common Examples
- 현재 부팅 이후의 로그 보기:
  ```bash
  journalctl -b
  ```
  
- 실시간 로그 추적:
  ```bash
  journalctl -f
  ```

- 특정 서비스의 로그 보기 (예: `nginx`):
  ```bash
  journalctl -u nginx
  ```

- 특정 시간 이후의 로그 보기:
  ```bash
  journalctl --since "2023-10-01 12:00:00"
  ```

- 특정 시간 이전의 로그 보기:
  ```bash
  journalctl --until "2023-10-02 12:00:00"
  ```

## Tips
- 로그를 더 잘 이해하기 위해 `-p` 옵션을 사용하여 로그의 우선순위를 필터링할 수 있습니다.
- 로그를 파일로 저장하고 싶다면, `>` 연산자를 사용하여 출력 결과를 파일로 리다이렉트할 수 있습니다.
- `--no-pager` 옵션을 사용하면 로그를 페이지 없이 한 번에 출력할 수 있습니다.