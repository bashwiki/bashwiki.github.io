# [리눅스] Bash getenforce 사용법

## Overview
`getenforce` 명령어는 Linux 시스템에서 SELinux(Security-Enhanced Linux)의 현재 상태를 확인하는 데 사용됩니다. SELinux는 시스템의 보안을 강화하기 위해 접근 제어 정책을 적용하는 보안 모듈입니다. `getenforce`를 사용하면 SELinux가 현재 어떤 모드에서 실행되고 있는지를 확인할 수 있습니다. 주로 "Enforcing", "Permissive", "Disabled" 중 하나의 상태를 반환합니다.

## Usage
기본적인 구문은 다음과 같습니다:

```bash
getenforce
```

이 명령어는 추가적인 옵션 없이도 사용할 수 있으며, SELinux의 현재 모드를 출력합니다. 특별한 옵션은 제공되지 않지만, 명령어 자체가 간단하여 사용하기 쉽습니다.

## Examples
1. **SELinux 상태 확인하기**:
   다음 명령어를 입력하면 SELinux의 현재 모드를 확인할 수 있습니다.

   ```bash
   getenforce
   ```

   출력 예시:
   ```
   Enforcing
   ```

2. **스크립트에서 사용하기**:
   `getenforce` 명령어를 스크립트에서 사용하여 SELinux 모드에 따라 다른 작업을 수행할 수 있습니다.

   ```bash
   if [ "$(getenforce)" == "Enforcing" ]; then
       echo "SELinux는 Enforcing 모드입니다."
   else
       echo "SELinux는 Enforcing 모드가 아닙니다."
   fi
   ```

## Tips
- `getenforce` 명령어는 SELinux의 상태를 확인하는 간단하고 빠른 방법입니다. 시스템의 보안 상태를 점검할 때 유용하게 사용하세요.
- SELinux 모드가 "Permissive"인 경우, 보안 정책 위반이 로그에 기록되지만 차단되지는 않으므로, 문제를 디버깅할 때 유용할 수 있습니다.
- SELinux의 설정을 변경해야 하는 경우, `setenforce` 명령어를 사용하여 모드를 변경할 수 있습니다.