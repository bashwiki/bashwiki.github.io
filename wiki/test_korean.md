# [리눅스] Bash test 사용법: 조건 평가

## Overview
`test` 명령어는 주어진 조건이 참인지 거짓인지 평가하는 데 사용됩니다. 이 명령어는 주로 스크립트에서 조건문을 작성할 때 유용하게 사용됩니다.

## Usage
기본 구문은 다음과 같습니다:
```
test [options] [arguments]
```

## Common Options
- `-e FILE`: 파일이 존재하는지 확인합니다.
- `-d FILE`: 주어진 경로가 디렉토리인지 확인합니다.
- `-f FILE`: 주어진 경로가 일반 파일인지 확인합니다.
- `-z STRING`: 문자열의 길이가 0인지 확인합니다.
- `-n STRING`: 문자열의 길이가 0이 아닌지 확인합니다.
- `STRING1 = STRING2`: 두 문자열이 같은지 비교합니다.

## Common Examples
다음은 `test` 명령어의 몇 가지 일반적인 사용 예입니다.

1. 파일 존재 여부 확인:
   ```bash
   test -e /path/to/file && echo "파일이 존재합니다."
   ```

2. 디렉토리 확인:
   ```bash
   test -d /path/to/directory && echo "디렉토리가 존재합니다."
   ```

3. 일반 파일 확인:
   ```bash
   test -f /path/to/file && echo "일반 파일입니다."
   ```

4. 문자열 길이 확인:
   ```bash
   STRING="Hello"
   test -n "$STRING" && echo "문자열이 비어 있지 않습니다."
   ```

5. 문자열 비교:
   ```bash
   test "abc" = "abc" && echo "문자열이 같습니다."
   ```

## Tips
- `test` 명령어는 `[`와 `]`로 대체할 수 있습니다. 예를 들어, `test -e FILE`는 `[ -e FILE ]`와 동일합니다.
- 조건문을 사용할 때는 `&&`와 `||`를 활용하여 복잡한 조건을 쉽게 처리할 수 있습니다.
- 스크립트에서 `test`를 사용할 때는 항상 조건이 참일 때 수행할 작업을 명확히 하세요.