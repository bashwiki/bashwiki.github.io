# [리눅스] Bash passwd 사용법: 사용자 비밀번호 관리

## Overview
`passwd` 명령어는 리눅스 시스템에서 사용자 계정의 비밀번호를 변경하거나 관리하는 데 사용됩니다. 이 명령어를 통해 사용자는 자신의 비밀번호를 수정할 수 있으며, 시스템 관리자는 다른 사용자의 비밀번호를 변경할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
passwd [options] [username]
```

## Common Options
- `-d`: 사용자 비밀번호를 삭제합니다.
- `-e`: 사용자의 비밀번호를 즉시 만료시킵니다.
- `-l`: 사용자의 계정을 잠급니다.
- `-u`: 잠긴 사용자의 계정을 활성화합니다.
- `-S`: 사용자의 비밀번호 상태를 표시합니다.

## Common Examples
1. **자신의 비밀번호 변경**
   ```bash
   passwd
   ```

2. **특정 사용자의 비밀번호 변경 (관리자 권한 필요)**
   ```bash
   sudo passwd username
   ```

3. **비밀번호 삭제**
   ```bash
   sudo passwd -d username
   ```

4. **비밀번호 만료**
   ```bash
   sudo passwd -e username
   ```

5. **사용자 비밀번호 상태 확인**
   ```bash
   passwd -S username
   ```

## Tips
- 비밀번호는 강력하게 설정하여 보안을 유지하세요.
- 비밀번호 변경 후에는 반드시 새 비밀번호를 기억해 두세요.
- 시스템 관리자는 사용자의 비밀번호를 변경할 때 주의하여야 하며, 사용자에게 변경 사실을 알려야 합니다.