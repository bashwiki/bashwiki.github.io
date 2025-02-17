# [리눅스] Bash ufw 사용법: 방화벽 관리

## Overview
`ufw`(Uncomplicated Firewall)는 리눅스 시스템에서 방화벽을 쉽게 관리할 수 있도록 도와주는 명령어입니다. 사용자가 복잡한 iptables 명령어를 사용하지 않고도 간단하게 방화벽 규칙을 설정하고 관리할 수 있게 해줍니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
ufw [options] [arguments]
```

## Common Options
- `enable`: 방화벽을 활성화합니다.
- `disable`: 방화벽을 비활성화합니다.
- `status`: 현재 방화벽 상태를 확인합니다.
- `allow [port]`: 특정 포트를 허용합니다.
- `deny [port]`: 특정 포트를 차단합니다.
- `delete [rule]`: 특정 규칙을 삭제합니다.

## Common Examples
- 방화벽 활성화:
    ```bash
    sudo ufw enable
    ```

- 방화벽 비활성화:
    ```bash
    sudo ufw disable
    ```

- 현재 방화벽 상태 확인:
    ```bash
    sudo ufw status
    ```

- 80번 포트(HTTP) 허용:
    ```bash
    sudo ufw allow 80
    ```

- 22번 포트(SSH) 허용:
    ```bash
    sudo ufw allow 22
    ```

- 25번 포트(SMTP) 차단:
    ```bash
    sudo ufw deny 25
    ```

- 특정 규칙 삭제:
    ```bash
    sudo ufw delete allow 80
    ```

## Tips
- 방화벽을 설정하기 전에 항상 현재 상태를 확인하는 것이 좋습니다.
- SSH를 사용 중이라면, SSH 포트를 허용한 후 방화벽을 활성화하세요. 그렇지 않으면 원격 접속이 차단될 수 있습니다.
- 규칙을 추가한 후에는 항상 `status` 명령어로 확인하여 적용된 규칙을 검토하세요.