# [리눅스] Bash systemctl 사용법: 시스템 서비스 관리

## Overview
`systemctl` 명령어는 시스템의 서비스와 유닛을 관리하는 데 사용됩니다. 이 명령어를 통해 서비스의 시작, 중지, 재시작, 상태 확인 등을 수행할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
systemctl [옵션] [인수]
```

## Common Options
- `start`: 서비스 시작
- `stop`: 서비스 중지
- `restart`: 서비스 재시작
- `status`: 서비스 상태 확인
- `enable`: 부팅 시 서비스 자동 시작 설정
- `disable`: 부팅 시 서비스 자동 시작 해제

## Common Examples
- 서비스 시작하기:
  ```bash
  systemctl start nginx
  ```

- 서비스 중지하기:
  ```bash
  systemctl stop nginx
  ```

- 서비스 상태 확인하기:
  ```bash
  systemctl status nginx
  ```

- 서비스 재시작하기:
  ```bash
  systemctl restart nginx
  ```

- 부팅 시 서비스 자동 시작 설정하기:
  ```bash
  systemctl enable nginx
  ```

- 부팅 시 서비스 자동 시작 해제하기:
  ```bash
  systemctl disable nginx
  ```

## Tips
- 서비스의 상태를 자주 확인하여 문제가 발생하지 않도록 관리하세요.
- `systemctl` 명령어를 사용할 때는 관리자 권한이 필요할 수 있으므로 `sudo`를 사용하는 것이 좋습니다.
- 서비스의 로그를 확인하려면 `journalctl -u [서비스명]` 명령어를 사용할 수 있습니다.