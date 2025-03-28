# [리눅스] Bash expr 사용법: 수학적 표현 및 문자열 조작

## Overview
`expr` 명령어는 수학적 계산, 문자열 조작 및 논리 연산을 수행하는 데 사용됩니다. 이 명령어는 주로 스크립트에서 간단한 계산이나 조건 검사를 위해 활용됩니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
expr [옵션] [인수]
```

## Common Options
- `+` : 덧셈
- `-` : 뺄셈
- `*` : 곱셈 (곱셈 기호는 이스케이프 필요)
- `/` : 나눗셈
- `%` : 나머지
- `=` : 문자열 비교
- `!=` : 문자열 불일치 비교

## Common Examples
1. 두 숫자의 덧셈:
   ```bash
   expr 5 + 3
   ```
   출력: `8`

2. 두 숫자의 뺄셈:
   ```bash
   expr 10 - 4
   ```
   출력: `6`

3. 문자열 길이 계산:
   ```bash
   expr length "Hello, World!"
   ```
   출력: `13`

4. 두 문자열 비교:
   ```bash
   expr "apple" = "apple"
   ```
   출력: `1` (참)

5. 곱셈을 위한 이스케이프:
   ```bash
   expr 4 \* 5
   ```
   출력: `20`

## Tips
- `expr`는 기본적으로 정수 연산을 수행하므로, 실수 계산이 필요할 경우 다른 도구를 사용하는 것이 좋습니다.
- 문자열 비교 시, 따옴표를 사용하여 공백이 포함된 문자열을 안전하게 처리하세요.
- `expr`는 스크립트에서 간단한 계산을 수행할 때 유용하지만, 복잡한 계산에는 `bc`와 같은 다른 도구를 고려하는 것이 좋습니다.