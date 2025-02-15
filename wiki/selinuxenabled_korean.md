# [리눅스] Bash selinuxenabled 사용법

## Overview
`selinuxenabled` 명령어는 시스템에서 SELinux(보안 강화 리눅스)가 활성화되어 있는지를 확인하는 데 사용됩니다. SELinux는 리눅스 커널의 보안 모듈로, 시스템의 보안을 강화하기 위해 접근 제어를 적용합니다. 이 명령어는 주로 스크립트나 프로그램에서 SELinux의 상태를 확인하여 조건부 작업을 수행하는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
selinuxenabled
```

이 명령어는 인자를 받지 않으며, SELinux가 활성화되어 있으면 0을 반환하고, 비활성화되어 있으면 1을 반환합니다. 이는 스크립트에서 조건문과 함께 사용될 수 있습니다.

## Examples
다음은 `selinuxenabled` 명령어를 사용하는 몇 가지 예시입니다.

### 예시 1: SELinux 상태 확인
SELinux가 활성화되어 있는지를 확인하고, 그에 따라 메시지를 출력하는 간단한 스크립트입니다.

```bash
if selinuxenabled; then
    echo "SELinux가 활성화되어 있습니다."
else
    echo "SELinux가 비활성화되어 있습니다."
fi
```

### 예시 2: SELinux 활성화에 따른 작업 수행
SELinux가 활성화된 경우에만 특정 작업을 수행하는 예시입니다.

```bash
if selinuxenabled; then
    # SELinux가 활성화된 경우 실행할 명령어
    echo "SELinux가 활성화되어 있으므로, 보안 관련 작업을 수행합니다."
    # 추가 명령어...
else
    echo "SELinux가 비활성화되어 있으므로, 기본 작업을 수행합니다."
    # 다른 명령어...
fi
```

## Tips
- `selinuxenabled` 명령어는 스크립트에서 조건부 로직을 구현할 때 유용합니다. SELinux의 상태에 따라 다른 작업을 수행할 수 있습니다.
- SELinux의 상태를 확인할 때는 `getenforce` 또는 `sestatus` 명령어와 함께 사용하는 것도 좋은 방법입니다. 이들 명령어는 SELinux의 현재 모드(예: Enforcing, Permissive, Disabled)를 보여줍니다.
- SELinux를 관리하는 경우, SELinux가 활성화된 상태에서 테스트를 진행하는 것이 보안 취약점을 방지하는 데 도움이 됩니다.