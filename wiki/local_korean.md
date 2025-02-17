# [리눅스] Bash local 사용법: 함수 내 지역 변수 생성

## 개요
`local` 명령은 Bash 스크립트에서 함수 내에서 사용할 수 있는 지역 변수를 생성하는 데 사용됩니다. 이 명령을 사용하면 변수의 범위를 제한하여 함수가 종료되면 변수의 값이 사라지도록 할 수 있습니다.

## 사용법
기본 구문은 다음과 같습니다:
```bash
local [options] [variable_name]=[value]
```

## 일반 옵션
- `-n`: 변수의 이름을 지정하지만 값을 할당하지 않습니다. 주로 변수의 참조를 위해 사용됩니다.

## 일반 예제
다음은 `local` 명령을 사용하는 몇 가지 예제입니다.

### 예제 1: 기본 사용법
```bash
my_function() {
    local my_var="Hello, World!"
    echo $my_var
}
my_function
```
이 예제에서 `my_var`는 `my_function` 내에서만 유효하며, 함수가 종료되면 사라집니다.

### 예제 2: 지역 변수의 범위
```bash
my_function() {
    local my_var="Inside Function"
    echo $my_var
}
my_function
echo $my_var  # 이 줄은 아무것도 출력하지 않습니다.
```
여기서 `my_var`는 함수 내에서만 사용 가능하므로 함수 외부에서 접근할 수 없습니다.

### 예제 3: 여러 지역 변수
```bash
my_function() {
    local var1="First"
    local var2="Second"
    echo "$var1 and $var2"
}
my_function  # 출력: First and Second
```
이 예제에서는 두 개의 지역 변수를 생성하고, 이를 사용하여 값을 출력합니다.

## 팁
- 지역 변수를 사용하면 함수의 독립성을 유지할 수 있어, 다른 함수나 스크립트와의 변수 충돌을 방지할 수 있습니다.
- 지역 변수를 사용하여 함수의 결과를 저장하고, 이를 다른 함수에서 사용할 필요가 없도록 할 수 있습니다.
- `local` 명령은 함수 내에서만 유효하므로, 함수가 종료된 후에는 메모리를 절약할 수 있습니다.