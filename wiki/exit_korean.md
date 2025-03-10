# [리눅스] Bash exit 사용법: 프로세스 종료

## Overview
`exit` 명령은 현재 셸 세션을 종료하는 데 사용됩니다. 이 명령은 스크립트나 셸에서 실행된 후 종료 상태 코드를 반환하여 프로세스가 어떻게 종료되었는지를 나타냅니다.

## Usage
기본 구문은 다음과 같습니다:
```
exit [options] [n]
```
여기서 `n`은 종료 상태 코드입니다.

## Common Options
- `n`: 종료 상태 코드를 지정합니다. 기본값은 마지막으로 실행된 명령의 종료 상태입니다.

## Common Examples
1. 기본 종료:
   ```bash
   exit
   ```

2. 특정 종료 코드로 종료:
   ```bash
   exit 1
   ```

3. 스크립트에서 종료 코드 반환:
   ```bash
   #!/bin/bash
   echo "스크립트 실행 중..."
   exit 0
   ```

4. 조건에 따라 종료:
   ```bash
   if [ -f "파일.txt" ]; then
       echo "파일이 존재합니다."
       exit 0
   else
       echo "파일이 존재하지 않습니다."
       exit 1
   fi
   ```

## Tips
- 스크립트에서 `exit`를 사용할 때는 명확한 종료 코드를 지정하여 오류를 쉽게 추적할 수 있도록 하세요.
- 종료 상태 코드는 0이 성공을 의미하고, 1 이상의 값은 오류를 나타냅니다. 이를 통해 다른 프로세스나 스크립트에서 결과를 처리할 수 있습니다.
- 셸에서 `exit` 명령을 사용할 때는 현재 셸 세션이 종료되므로 주의해야 합니다.