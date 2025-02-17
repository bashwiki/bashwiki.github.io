# [리눅스] Bash getopts 사용법: 옵션 파싱을 위한 유틸리티

## Overview
`getopts`는 Bash 스크립트에서 명령줄 옵션을 파싱하는 데 사용되는 내장 명령어입니다. 이 명령어는 사용자로부터 입력된 옵션을 쉽게 처리하고, 스크립트의 동작을 제어할 수 있도록 도와줍니다.

## Usage
`getopts`의 기본 구문은 다음과 같습니다:

```bash
getopts optstring variable
```

- `optstring`: 처리할 옵션의 문자열. 각 옵션은 하나의 문자로 표현되며, 선택적 인자는 콜론(`:`)으로 표시합니다.
- `variable`: 옵션 값을 저장할 변수의 이름입니다.

## Common Options
- `-a`: 옵션을 추가할 때 사용합니다.
- `-b`: 옵션을 제거할 때 사용합니다.
- `-c`: 특정 작업을 수행할 때 사용되는 옵션입니다.

## Common Examples

### 기본 사용 예
```bash
#!/bin/bash

while getopts "ab:c:" opt; do
  case $opt in
    a)
      echo "Option A selected"
      ;;
    b)
      echo "Option B selected with value: $OPTARG"
      ;;
    c)
      echo "Option C selected with value: $OPTARG"
      ;;
    *)
      echo "Invalid option"
      ;;
  esac
done
```

### 옵션과 인자 사용 예
```bash
#!/bin/bash

while getopts "f:n:" opt; do
  case $opt in
    f)
      echo "File name: $OPTARG"
      ;;
    n)
      echo "Number: $OPTARG"
      ;;
    *)
      echo "Usage: $0 -f filename -n number"
      ;;
  esac
done
```

### 여러 옵션 처리 예
```bash
#!/bin/bash

while getopts "abc" opt; do
  case $opt in
    a)
      echo "Option A"
      ;;
    b)
      echo "Option B"
      ;;
    c)
      echo "Option C"
      ;;
    *)
      echo "Usage: $0 -a -b -c"
      ;;
  esac
done
```

## Tips
- `getopts`는 옵션을 처리할 때 자동으로 인덱스를 관리하므로, 스크립트에서 옵션을 쉽게 추적할 수 있습니다.
- 옵션 문자열에서 콜론(`:`)을 사용하여 인자가 필요한 옵션을 정의할 수 있습니다.
- `OPTARG` 변수를 사용하여 현재 처리 중인 옵션의 인자 값을 참조할 수 있습니다.
- 스크립트의 사용법을 명확히 하기 위해, 잘못된 옵션이 입력될 경우 사용자에게 안내 메시지를 제공하는 것이 좋습니다.