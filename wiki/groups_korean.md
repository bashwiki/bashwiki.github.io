# [리눅스] Bash groups 사용법: 사용자 그룹 정보 확인

## Overview
`groups` 명령어는 현재 사용자 또는 지정된 사용자가 속한 그룹 정보를 표시합니다. 이 명령어는 시스템에서 사용자 권한 및 그룹 관리에 유용하게 사용됩니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
groups [options] [arguments]
```

## Common Options
- `-h`, `--help`: 도움말 정보를 표시합니다.
- `-v`, `--version`: 버전 정보를 표시합니다.

## Common Examples
1. 현재 사용자 그룹 확인:
   ```bash
   groups
   ```

2. 특정 사용자의 그룹 확인:
   ```bash
   groups username
   ```

3. 도움말 정보 보기:
   ```bash
   groups --help
   ```

4. 버전 정보 확인:
   ```bash
   groups --version
   ```

## Tips
- `groups` 명령어는 사용자 계정의 권한을 이해하는 데 도움이 됩니다. 따라서 시스템 관리 시 유용하게 활용할 수 있습니다.
- 여러 사용자의 그룹 정보를 확인할 때는 사용자 이름을 명시적으로 지정하는 것이 좋습니다.
- `groups` 명령어는 간단하지만, 사용자 관리 및 보안 설정에 중요한 역할을 합니다.