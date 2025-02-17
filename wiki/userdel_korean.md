# [리눅스] Bash userdel 사용법: 사용자 계정 삭제

## Overview
`userdel` 명령어는 리눅스 시스템에서 사용자 계정을 삭제하는 데 사용됩니다. 이 명령어를 통해 시스템에서 더 이상 필요하지 않은 사용자 계정을 안전하게 제거할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
userdel [옵션] [사용자 이름]
```

## Common Options
- `-r`: 사용자 홈 디렉토리와 메일 스풀을 함께 삭제합니다.
- `-f`: 사용자가 로그인 중일 경우에도 강제로 계정을 삭제합니다.
- `-Z`: SELinux 사용자 컨텍스트를 삭제합니다.

## Common Examples
1. 기본 사용자 삭제:
   ```bash
   userdel username
   ```

2. 사용자와 그 홈 디렉토리 삭제:
   ```bash
   userdel -r username
   ```

3. 로그인 중인 사용자 강제로 삭제:
   ```bash
   userdel -f username
   ```

4. SELinux 사용자 컨텍스트 삭제:
   ```bash
   userdel -Z username
   ```

## Tips
- 사용자 계정을 삭제하기 전에 해당 사용자의 데이터 백업을 고려하세요.
- `-r` 옵션을 사용할 때는 주의하여 홈 디렉토리의 중요한 파일이 삭제되지 않도록 확인하세요.
- 시스템의 사용자 목록을 확인하려면 `/etc/passwd` 파일을 열어보세요.