# [리눅스] Bash let 사용법: 수학적 계산 수행

## Overview
`let` 명령어는 Bash에서 수학적 계산을 수행하는 데 사용됩니다. 이 명령어는 변수에 수치 값을 할당하거나 수식을 평가하는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```
let [options] [arguments]
```

## Common Options
- `-n`: 결과를 출력하지 않고 계산만 수행합니다.
- `-e`: 계산이 성공적으로 완료되면 0을 반환합니다.

## Common Examples
다음은 `let` 명령어의 몇 가지 일반적인 예입니다.

### 예제 1: 변수에 값 할당
```bash
let x=5
echo $x  # 출력: 5
```

### 예제 2: 두 변수의 합 계산
```bash
let a=10
let b=20
let sum=a+b
echo $sum  # 출력: 30
```

### 예제 3: 증가 연산
```bash
let count=0
let count+=1
echo $count  # 출력: 1
```

### 예제 4: 조건부 계산
```bash
let "result = (5 + 3) * 2"
echo $result  # 출력: 16
```

## Tips
- `let` 명령어는 수식에 공백을 허용하지 않으므로, 수식을 작성할 때 주의해야 합니다.
- `let` 대신 `$(( ))` 구문을 사용할 수도 있으며, 이는 더 직관적일 수 있습니다. 예를 들어, `result=$((5 + 3))`.
- 계산 결과를 출력하고 싶다면, `let` 명령어 뒤에 `echo`를 사용하여 결과를 확인할 수 있습니다.