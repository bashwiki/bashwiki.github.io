# [리눅스] Bash typeset 사용법: 변수 속성 설정

## Overview
`typeset` 명령은 Bash에서 변수를 선언하고 속성을 설정하는 데 사용됩니다. 이 명령을 통해 변수의 특성을 정의하고, 특정한 환경에서 변수를 관리할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
typeset [options] [arguments]
```

## Common Options
- `-i`: 변수를 정수형으로 설정합니다. 이 옵션을 사용하면 변수에 대한 모든 수치 연산이 정수로 처리됩니다.
- `-r`: 변수를 읽기 전용으로 설정합니다. 이 경우 변수의 값을 변경할 수 없습니다.
- `-a`: 배열 변수를 선언합니다.
- `-A`: 연관 배열 변수를 선언합니다.
- `-x`: 변수를 환경 변수로 설정하여 자식 프로세스에서 사용할 수 있게 합니다.

## Common Examples

1. 정수형 변수 선언:
   ```bash
   typeset -i num=5
   echo $num  # 출력: 5
   num=10
   echo $num  # 출력: 10
   ```

2. 읽기 전용 변수 설정:
   ```bash
   typeset -r constant=100
   echo $constant  # 출력: 100
   constant=200    # 오류 발생: 읽기 전용 변수
   ```

3. 배열 변수 선언:
   ```bash
   typeset -a fruits
   fruits=(apple banana cherry)
   echo ${fruits[1]}  # 출력: banana
   ```

4. 연관 배열 변수 선언:
   ```bash
   typeset -A colors
   colors[red]="#FF0000"
   colors[green]="#00FF00"
   echo ${colors[red]}  # 출력: #FF0000
   ```

5. 환경 변수 설정:
   ```bash
   typeset -x PATH="/usr/local/bin:$PATH"
   echo $PATH  # /usr/local/bin:/usr/bin:/bin 등 출력
   ```

## Tips
- `typeset` 명령은 주로 스크립트 내에서 변수를 관리할 때 유용합니다. 변수를 명확하게 정의하고, 의도한 대로 작동하도록 설정하는 것이 중요합니다.
- 읽기 전용 변수를 사용하여 중요한 값을 보호할 수 있습니다.
- 배열과 연관 배열을 활용하여 데이터를 구조적으로 관리하면 스크립트의 가독성을 높일 수 있습니다.