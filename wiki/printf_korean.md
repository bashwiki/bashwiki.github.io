# [리눅스] Bash printf 사용법: 형식화된 출력을 위한 명령어

## Overview
`printf` 명령어는 형식화된 출력을 생성하는 데 사용됩니다. C 언어의 `printf` 함수와 유사하게, 다양한 데이터 형식을 지정하여 출력할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
printf [options] [arguments]
```

## Common Options
- `-v`: 변수를 사용하여 출력할 문자열을 저장합니다.
- `-f`: 포맷 문자열을 지정합니다.
- `-n`: 출력 후 줄 바꿈을 하지 않습니다.

## Common Examples
1. **기본 문자열 출력**
   ```bash
   printf "Hello, World!\n"
   ```
   이 명령어는 "Hello, World!"를 출력합니다.

2. **형식 지정 출력**
   ```bash
   printf "Name: %s, Age: %d\n" "Alice" 30
   ```
   이 명령어는 "Name: Alice, Age: 30"을 출력합니다.

3. **소수점 출력**
   ```bash
   printf "Pi is approximately %.2f\n" 3.14159
   ```
   이 명령어는 "Pi is approximately 3.14"를 출력합니다.

4. **여러 줄 출력**
   ```bash
   printf "Line 1\nLine 2\nLine 3\n"
   ```
   이 명령어는 3개의 줄을 출력합니다.

## Tips
- `printf`는 `echo`보다 더 많은 형식 옵션을 제공하므로, 복잡한 출력을 다룰 때 유용합니다.
- 출력 형식을 명확히 지정하면, 예기치 않은 결과를 피할 수 있습니다.
- 줄 바꿈을 원하지 않을 경우 `-n` 옵션을 사용하여 출력 후 줄 바꿈을 방지할 수 있습니다.