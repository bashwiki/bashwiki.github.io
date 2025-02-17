# [리눅스] Bash break 사용법: 루프를 종료합니다.

## Overview
`break` 명령은 Bash 스크립트에서 루프를 종료하는 데 사용됩니다. 주로 `for`, `while`, 또는 `until` 루프 내에서 사용되며, 특정 조건이 충족되었을 때 루프를 즉시 종료할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
break [n]
```

여기서 `n`은 종료할 루프의 레벨을 지정합니다. 기본값은 1로, 가장 가까운 루프를 종료합니다.

## Common Options
- `n`: 종료할 루프의 깊이를 지정합니다. 예를 들어, `n=2`이면 두 개의 중첩된 루프를 모두 종료합니다.

## Common Examples

### 예제 1: 기본 사용법
가장 간단한 형태로, `break`를 사용하여 `for` 루프를 종료하는 예입니다.

```bash
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        break
    fi
    echo $i
done
```
이 코드는 1과 2를 출력하고, 3에서 루프를 종료합니다.

### 예제 2: 중첩 루프에서의 사용
중첩된 루프에서 `break`를 사용하는 방법입니다.

```bash
for i in {1..3}; do
    for j in {1..3}; do
        if [ $j -eq 2 ]; then
            break 2
        fi
        echo "i: $i, j: $j"
    done
done
```
이 코드는 `i`와 `j`의 값을 출력하다가 `j`가 2일 때 두 개의 루프를 모두 종료합니다.

### 예제 3: 사용자 입력에 따른 종료
사용자의 입력에 따라 루프를 종료하는 예입니다.

```bash
while true; do
    read -p "종료하려면 'exit'를 입력하세요: " input
    if [ "$input" == "exit" ]; then
        break
    fi
    echo "입력한 값: $input"
done
```
사용자가 'exit'를 입력할 때까지 루프가 계속 실행됩니다.

## Tips
- `break`를 사용할 때는 루프의 종료 조건을 명확히 설정하여 의도하지 않은 종료를 방지하세요.
- 중첩된 루프에서 `break n`을 사용할 때는 종료할 레벨을 정확히 지정하는 것이 중요합니다.
- 디버깅 시, `echo` 명령을 사용하여 루프의 진행 상황을 출력하면 도움이 됩니다.