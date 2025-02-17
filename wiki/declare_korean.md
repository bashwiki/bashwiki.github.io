# [리눅스] Bash declare 사용법: 변수 및 배열 선언

## Overview
`declare` 명령어는 Bash 스크립트에서 변수와 배열을 선언하고, 그 속성을 설정하는 데 사용됩니다. 이 명령어를 통해 변수를 특정 데이터 유형으로 설정하거나, 배열을 정의할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
declare [options] [arguments]
```

## Common Options
- `-a`: 배열 변수를 선언합니다.
- `-i`: 정수형 변수를 선언합니다. 이 변수는 수학적 연산을 수행할 수 있습니다.
- `-r`: 읽기 전용 변수를 선언합니다. 이 변수는 수정할 수 없습니다.
- `-x`: 환경 변수를 선언합니다. 이 변수는 자식 프로세스에 전달됩니다.

## Common Examples
1. **정수형 변수 선언**
   ```bash
   declare -i num=5
   echo $num  # 출력: 5
   ```

2. **읽기 전용 변수 선언**
   ```bash
   declare -r constant=10
   echo $constant  # 출력: 10
   # constant=20  # 오류: 읽기 전용 변수입니다.
   ```

3. **배열 선언**
   ```bash
   declare -a fruits=("apple" "banana" "cherry")
   echo ${fruits[1]}  # 출력: banana
   ```

4. **환경 변수 선언**
   ```bash
   declare -x PATH="/usr/local/bin:$PATH"
   echo $PATH  # 업데이트된 PATH 출력
   ```

## Tips
- 변수를 선언할 때 `declare`를 사용하면 변수의 속성을 명확히 할 수 있어 코드의 가독성이 높아집니다.
- 읽기 전용 변수를 사용하여 중요한 값을 보호할 수 있습니다.
- 배열을 사용할 때는 인덱스를 통해 쉽게 접근할 수 있으므로, 여러 값을 관리하는 데 유용합니다.