# [리눅스] Bash local 사용법

## Overview
`local` 명령어는 Bash 스크립트 내에서 변수를 지역적으로 정의하는 데 사용됩니다. 이는 함수 내에서만 유효한 변수를 생성하여, 함수 외부에서의 변수 충돌을 방지하고 코드의 가독성을 높이는 데 도움을 줍니다. `local`을 사용하면 함수가 종료된 후에도 변수가 남아있지 않으므로, 메모리 관리 측면에서도 유리합니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
local VARIABLE_NAME=value
```

여기서 `VARIABLE_NAME`은 정의할 변수의 이름이며, `value`는 그 변수에 할당할 값입니다. `local` 명령어는 반드시 함수 내부에서 사용해야 하며, 함수 외부에서는 사용할 수 없습니다.

### Common Options
`local` 명령어는 특별한 옵션이 필요하지 않으며, 단순히 변수를 지역적으로 정의하는 역할만 수행합니다.

## Examples

### 예제 1: 기본 사용법
다음은 `local`을 사용하여 함수 내에서 지역 변수를 정의하는 간단한 예제입니다.

```bash
#!/bin/bash

my_function() {
    local my_var="Hello, World!"
    echo $my_var
}

my_function
# 출력: Hello, World!
echo $my_var
# 출력: (빈 값)
```

위의 예제에서 `my_var`는 `my_function` 함수 내에서만 유효하며, 함수가 종료된 후에는 접근할 수 없습니다.

### 예제 2: 지역 변수와 전역 변수
아래 예제에서는 지역 변수와 전역 변수를 비교합니다.

```bash
#!/bin/bash

global_var="I am global"

my_function() {
    local local_var="I am local"
    echo $local_var
}

my_function
echo $global_var
# 출력: I am local
# 출력: I am global
```

이 예제에서 `local_var`는 함수 내에서만 유효하고, `global_var`는 스크립트 전체에서 접근할 수 있습니다.

## Tips
- `local` 변수를 사용할 때는 항상 함수 내부에서 정의해야 하며, 이를 통해 코드의 유지보수성을 높일 수 있습니다.
- 지역 변수를 사용하여 함수의 입력값을 조작할 때, 다른 함수나 스크립트의 변수와 충돌하지 않도록 주의하세요.
- 여러 변수를 한 번에 정의하고 싶다면, `local`을 여러 번 사용할 필요 없이 다음과 같이 할 수 있습니다:

```bash
my_function() {
    local var1="value1" var2="value2"
    echo $var1 $var2
}
```

이와 같이 `local`을 활용하면 함수의 범위 내에서만 변수를 안전하게 사용할 수 있습니다.