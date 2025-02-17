# [리눅스] Bash source 사용법: 스크립트 실행 및 환경 설정

## Overview
`source` 명령어는 Bash 스크립트를 현재 셸 환경에서 실행할 수 있게 해줍니다. 이 명령어를 사용하면 스크립트 내의 변수나 함수가 현재 셸에 적용되어, 이후의 명령어에서 사용할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
source [옵션] [인수]
```

## Common Options
- `-`: 이 옵션은 `source`와 동일하게 작동하지만, 명령어가 실행된 후에 셸의 상태를 변경하지 않습니다.

## Common Examples
1. **스크립트 실행하기**
   ```bash
   source myscript.sh
   ```
   위 명령어는 `myscript.sh` 파일을 현재 셸에서 실행합니다.

2. **환경 변수 설정하기**
   ```bash
   source ~/.bash_profile
   ```
   이 명령어는 사용자 홈 디렉토리의 `.bash_profile` 파일을 실행하여 환경 변수를 설정합니다.

3. **함수 정의하기**
   ```bash
   source myfunctions.sh
   ```
   `myfunctions.sh` 파일에 정의된 함수들을 현재 셸에서 사용할 수 있게 합니다.

## Tips
- 스크립트를 실행하기 전에 실행 권한이 필요하지 않으므로, `source` 명령어는 파일의 실행 권한을 신경 쓸 필요가 없습니다.
- 스크립트 내에서 정의된 변수는 현재 셸에 영향을 미치므로, 스크립트가 끝난 후에도 변수의 값을 확인할 수 있습니다.
- `source` 대신 `.` (점) 명령어를 사용할 수도 있습니다. 예를 들어, `source myscript.sh`는 `. myscript.sh`와 동일하게 작동합니다.