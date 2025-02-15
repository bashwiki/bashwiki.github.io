# [리눅스] Bash firewalld 사용법

## Overview
`firewalld`는 리눅스 시스템에서 방화벽을 관리하기 위한 동적 방화벽 관리 도구입니다. 이 명령은 네트워크 트래픽을 필터링하고, 특정 서비스나 포트에 대한 접근을 제어하는 데 사용됩니다. `firewalld`는 zones와 rich rules를 통해 복잡한 방화벽 규칙을 쉽게 설정할 수 있도록 도와줍니다.

## Usage
기본적인 `firewalld` 명령의 구문은 다음과 같습니다:

```bash
firewalld [OPTIONS]
```

주요 옵션은 다음과 같습니다:
- `--state`: 현재 방화벽의 상태를 확인합니다.
- `--zone`: 특정 존(zone)에서의 규칙을 설정하거나 조회합니다.
- `--add-service`: 특정 서비스에 대한 접근을 허용합니다.
- `--remove-service`: 특정 서비스에 대한 접근을 차단합니다.
- `--add-port`: 특정 포트를 열어줍니다.
- `--remove-port`: 특정 포트를 닫아줍니다.
- `--reload`: 방화벽 규칙을 새로 고칩니다.

## Examples
### 예제 1: 방화벽 상태 확인
현재 방화벽의 상태를 확인하려면 다음 명령어를 사용합니다.

```bash
firewalld --state
```

### 예제 2: HTTP 서비스 허용
HTTP 서비스에 대한 접근을 허용하려면 다음과 같이 입력합니다.

```bash
firewalld --add-service=http --permanent
firewalld --reload
```

위 명령어는 HTTP 서비스에 대한 접근을 영구적으로 허용하고, 변경 사항을 적용하기 위해 방화벽을 새로 고칩니다.

## Tips
- `firewalld`를 사용할 때는 항상 변경 사항을 적용하기 위해 `--reload` 옵션을 사용하는 것을 잊지 마세요.
- 방화벽 규칙을 설정하기 전에 현재 설정을 백업해 두는 것이 좋습니다.
- `firewalld`의 zones를 활용하여 네트워크 환경에 따라 다른 규칙을 설정하는 것이 유용합니다. 예를 들어, 공용 네트워크에서는 더 엄격한 규칙을 적용할 수 있습니다.