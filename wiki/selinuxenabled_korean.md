# [리눅스] Bash selinuxenabled 사용법: SELinux 활성화 여부 확인

## Overview
`selinuxenabled` 명령어는 시스템에서 SELinux(Security-Enhanced Linux)가 활성화되어 있는지를 확인하는 데 사용됩니다. 이 명령어는 간단하게 SELinux의 상태를 체크할 수 있는 유용한 도구입니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
selinuxenabled [options] [arguments]
```

## Common Options
`selinuxenabled` 명령어는 특별한 옵션을 필요로 하지 않으며, 기본적으로 SELinux의 활성화 여부만을 확인합니다.

## Common Examples
다음은 `selinuxenabled` 명령어의 몇 가지 실용적인 예입니다:

1. **SELinux 상태 확인**
   ```bash
   selinuxenabled
   ```
   이 명령어를 실행하면 SELinux가 활성화되어 있으면 0을 반환하고, 비활성화되어 있으면 1을 반환합니다.

2. **조건부 명령 실행**
   ```bash
   if selinuxenabled; then
       echo "SELinux is enabled."
   else
       echo "SELinux is disabled."
   fi
   ```
   이 스크립트는 SELinux의 상태에 따라 다른 메시지를 출력합니다.

## Tips
- `selinuxenabled` 명령어는 스크립트 내에서 조건문과 함께 사용하여 SELinux의 상태에 따라 다른 작업을 수행할 수 있습니다.
- SELinux의 상태를 확인한 후, 필요에 따라 설정을 조정하는 것이 좋습니다.