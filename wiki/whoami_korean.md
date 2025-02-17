# [리눅스] Bash whoami 사용법: 현재 사용자 확인

## Overview
`whoami` 명령어는 현재 로그인한 사용자의 이름을 출력합니다. 이 명령어는 시스템에서 현재 사용자가 누구인지 확인할 때 유용합니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
whoami [옵션]
```

## Common Options
`whoami` 명령어는 특별한 옵션이 필요하지 않지만, 다음과 같은 옵션을 사용할 수 있습니다:

- `--help`: 사용법을 보여줍니다.
- `--version`: 버전 정보를 출력합니다.

## Common Examples

1. 현재 사용자 이름 확인:
   ```bash
   whoami
   ```

2. 도움말 보기:
   ```bash
   whoami --help
   ```

3. 버전 정보 확인:
   ```bash
   whoami --version
   ```

## Tips
- `whoami` 명령어는 스크립트에서 현재 사용자를 확인할 때 유용합니다.
- 여러 사용자가 시스템에 로그인할 수 있는 환경에서, `whoami`를 사용하여 자신이 어떤 권한으로 작업하고 있는지 확인하는 것이 좋습니다.