# [리눅스] Bash continue 사용법: 반복문에서 다음 반복으로 건너뛰기

## Overview
`continue` 명령어는 Bash 스크립트에서 반복문 내에서 사용되며, 현재 반복을 종료하고 다음 반복으로 넘어가도록 합니다. 주로 조건에 따라 특정 반복을 건너뛰고 싶을 때 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
continue [n]
```
여기서 `n`은 반복문에서 몇 번째 반복을 건너뛸지를 지정합니다. `n`을 생략하면 기본값은 1입니다.

## Common Options
- `n`: 건너뛸 반복의 수를 지정합니다. 예를 들어, `continue 2`는 현재 반복을 종료하고 다음 두 번째 반복으로 넘어갑니다.

## Common Examples

### 기본 사용 예
```bash
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        continue
    fi
    echo $i
done
```
위의 예제에서는 숫자 1부터 5까지 반복하면서 3일 경우 `continue`를 사용하여 3을 건너뛰고 1, 2, 4, 5만 출력합니다.

### 특정 반복 건너뛰기
```bash
for i in {1..10}; do
    if [ $((i % 2)) -eq 0 ]; then
        continue  # 짝수는 건너뛰기
    fi
    echo $i
done
```
이 예제에서는 짝수인 경우 `continue`를 사용하여 홀수만 출력합니다.

### 중첩 반복문에서 사용하기
```bash
for i in {1..3}; do
    for j in {1..3}; do
        if [ $j -eq 2 ]; then
            continue 2  # 내부 반복문에서 2를 건너뛰기
        fi
        echo "i: $i, j: $j"
    done
done
```
여기서는 내부 반복문에서 `j`가 2일 경우, 내부 반복을 건너뛰고 다음 `j`로 넘어갑니다.

## Tips
- `continue`는 주로 조건문과 함께 사용하여 특정 조건에서 반복을 건너뛰는 데 유용합니다.
- 중첩 반복문에서 `continue n`을 사용할 때는 `n`의 값을 잘 설정하여 원하는 반복을 정확히 건너뛰도록 하세요.
- 코드의 가독성을 높이기 위해 `continue`를 사용할 때는 조건문을 명확하게 작성하는 것이 좋습니다.