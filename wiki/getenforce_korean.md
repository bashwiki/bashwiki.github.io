# [리눅스] Bash getenforce 사용법: SELinux 상태 확인

## Overview
getenforce 명령어는 SELinux(Security-Enhanced Linux)의 현재 상태를 확인하는 데 사용됩니다. 이 명령어를 통해 SELinux가 활성화되어 있는지, 비활성화되어 있는지를 쉽게 알 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```
getenforce [options] [arguments]
```

## Common Options
- `-h`, `--help`: 도움말을 표시합니다.
- `-V`, `--version`: 버전 정보를 표시합니다.

## Common Examples
1. **SELinux 상태 확인**
   ```bash
   getenforce
   ```
   이 명령어를 실행하면 SELinux의 현재 상태가 "Enforcing", "Permissive", 또는 "Disabled"로 표시됩니다.

2. **도움말 보기**
   ```bash
   getenforce --help
   ```
   이 명령어를 사용하면 getenforce 명령어에 대한 도움말 정보를 확인할 수 있습니다.

3. **버전 정보 확인**
   ```bash
   getenforce --version
   ```
   이 명령어를 통해 getenforce의 버전 정보를 확인할 수 있습니다.

## Tips
- SELinux의 상태를 정기적으로 확인하여 보안 설정이 올바르게 적용되고 있는지 점검하는 것이 좋습니다.
- "Enforcing" 모드에서 문제가 발생할 경우, "Permissive" 모드로 변경하여 로그를 확인하고 문제를 해결할 수 있습니다.
- SELinux 설정을 변경한 후에는 시스템을 재부팅하거나 서비스를 재시작하여 변경 사항을 적용해야 할 수 있습니다.