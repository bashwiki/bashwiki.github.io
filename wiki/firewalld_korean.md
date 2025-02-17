# [리눅스] Bash firewalld 사용법: 방화벽 관리

## Overview
firewalld는 리눅스 시스템에서 방화벽을 관리하는 도구입니다. 이 명령어를 사용하면 네트워크 트래픽을 제어하고, 보안 규칙을 설정하며, 다양한 서비스에 대한 접근을 허용하거나 차단할 수 있습니다.

## Usage
firewalld의 기본 구문은 다음과 같습니다:

```bash
firewalld [options] [arguments]
```

## Common Options
- `--zone`: 특정 영역에서 규칙을 설정합니다.
- `--add-service`: 특정 서비스를 방화벽 규칙에 추가합니다.
- `--remove-service`: 특정 서비스를 방화벽 규칙에서 제거합니다.
- `--add-port`: 특정 포트를 방화벽 규칙에 추가합니다.
- `--remove-port`: 특정 포트를 방화벽 규칙에서 제거합니다.
- `--list-all`: 현재 설정된 모든 방화벽 규칙을 표시합니다.

## Common Examples
- 특정 서비스 추가하기 (예: HTTP 서비스):
```bash
firewalld --zone=public --add-service=http
```

- 특정 포트 추가하기 (예: 8080 포트):
```bash
firewalld --zone=public --add-port=8080/tcp
```

- 특정 서비스 제거하기 (예: SSH 서비스):
```bash
firewalld --zone=public --remove-service=ssh
```

- 현재 방화벽 규칙 확인하기:
```bash
firewalld --list-all
```

## Tips
- 방화벽 규칙을 변경하기 전에 현재 설정을 백업하는 것이 좋습니다.
- 변경 후에는 항상 방화벽 상태를 확인하여 예상대로 작동하는지 확인하세요.
- 특정 서비스나 포트를 추가하기 전에 해당 서비스가 실제로 실행 중인지 확인하세요.