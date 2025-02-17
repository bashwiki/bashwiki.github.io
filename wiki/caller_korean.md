# [리눅스] Bash caller 사용법: 명령어 호출

## Overview
`caller` 명령어는 현재 실행 중인 스크립트에서 호출된 함수의 정보를 출력합니다. 주로 디버깅 목적으로 사용되며, 함수 호출의 위치와 관련된 정보를 제공합니다.

## Usage
기본 구문은 다음과 같습니다:
```
caller [옵션]
```

## Common Options
- `-p`: 호출된 함수의 매개변수를 포함하여 출력합니다.
- `-n`: 호출된 함수의 이름만 출력합니다.

## Common Examples
1. 기본 호출 정보 출력:
   ```bash
   function test {
       caller
   }
   test
   ```

2. 매개변수 포함하여 호출 정보 출력:
   ```bash
   function test {
       caller -p
   }
   test
   ```

3. 함수 이름만 출력:
   ```bash
   function test {
       caller -n
   }
   test
   ```

## Tips
- `caller` 명령어는 주로 복잡한 스크립트에서 함수 호출을 추적할 때 유용합니다.
- 디버깅을 위해 `set -x`와 함께 사용하면, 호출된 함수의 정보를 더 쉽게 확인할 수 있습니다.
- 여러 함수가 중첩되어 호출될 때, `caller`를 사용하여 호출 스택을 명확히 파악할 수 있습니다.