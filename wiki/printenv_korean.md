# [리눅스] Bash printenv 사용법: 환경 변수 출력

## Overview
`printenv` 명령어는 현재 세션의 환경 변수를 출력하는 데 사용됩니다. 이 명령어를 통해 시스템에서 설정된 다양한 환경 변수의 값을 확인할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
printenv [options] [arguments]
```

## Common Options
- `-0`, `--null`: 출력 결과를 널 문자로 구분합니다.
- `NAME`: 특정 환경 변수의 값을 출력합니다. 변수를 지정하지 않으면 모든 환경 변수가 출력됩니다.

## Common Examples
1. 모든 환경 변수 출력하기:
   ```bash
   printenv
   ```

2. 특정 환경 변수 출력하기 (예: `HOME` 변수):
   ```bash
   printenv HOME
   ```

3. 널 문자로 구분된 출력:
   ```bash
   printenv -0
   ```

## Tips
- `printenv` 명령어는 `env` 명령어와 유사하지만, 특정 변수를 출력할 때 더 간단하게 사용할 수 있습니다.
- 스크립트에서 환경 변수를 확인할 때 유용하게 활용할 수 있습니다.