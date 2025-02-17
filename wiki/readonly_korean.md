# [리눅스] Bash readonly 사용법: 변수의 읽기 전용 설정

## Overview
`readonly` 명령어는 Bash에서 변수를 읽기 전용으로 설정하는 데 사용됩니다. 이 명령어를 사용하면 변수의 값을 변경할 수 없도록 보호할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```
readonly [options] [arguments]
```

## Common Options
- `-p`: 현재 읽기 전용 변수 목록을 출력합니다.

## Common Examples
1. **변수 읽기 전용 설정하기**
   ```bash
   my_var="Hello"
   readonly my_var
   ```

2. **읽기 전용 변수의 값 변경 시도**
   ```bash
   my_var="Hello"
   readonly my_var
   my_var="World"  # 오류 발생: readonly 변수는 변경할 수 없습니다.
   ```

3. **현재 읽기 전용 변수 목록 보기**
   ```bash
   readonly -p
   ```

## Tips
- 읽기 전용 변수를 설정하면 실수로 값을 변경하는 것을 방지할 수 있습니다.
- 스크립트에서 중요한 설정 값을 보호하기 위해 `readonly`를 사용하는 것이 좋습니다.
- 읽기 전용 변수는 스크립트의 가독성을 높이고, 코드 유지보수를 용이하게 합니다.