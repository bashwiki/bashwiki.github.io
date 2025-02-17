# [리눅스] Bash nohup 사용법: 프로세스를 백그라운드에서 실행하기

## Overview
`nohup` 명령어는 사용자가 로그아웃하더라도 프로세스가 계속 실행될 수 있도록 하는 명령어입니다. 주로 서버에서 긴 작업을 실행할 때 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
nohup [옵션] [명령어] [인수] &
```

## Common Options
- `&`: 명령어를 백그라운드에서 실행합니다.
- `-h`: 도움말을 표시합니다.
- `-v`: 버전을 표시합니다.

## Common Examples
1. **단순한 nohup 사용 예**
   ```bash
   nohup long_running_script.sh &
   ```
   이 명령어는 `long_running_script.sh`를 백그라운드에서 실행합니다.

2. **출력을 파일로 리디렉션**
   ```bash
   nohup my_process > output.log &
   ```
   이 명령어는 `my_process`의 출력을 `output.log` 파일로 저장합니다.

3. **표준 오류도 파일로 리디렉션**
   ```bash
   nohup my_process > output.log 2>&1 &
   ```
   이 명령어는 표준 출력과 표준 오류를 모두 `output.log` 파일로 리디렉션합니다.

## Tips
- `nohup`을 사용할 때는 항상 `&`를 추가하여 프로세스가 백그라운드에서 실행되도록 하세요.
- 출력 파일을 지정하지 않으면 기본적으로 `nohup.out` 파일에 출력이 저장됩니다.
- 긴 작업을 실행할 때는 `ps` 명령어로 프로세스 상태를 확인할 수 있습니다.