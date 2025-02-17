# [리눅스] Bash history 사용법: 명령어 기록 보기

## Overview
`history` 명령어는 Bash 셸에서 사용자가 입력한 명령어의 기록을 보여줍니다. 이를 통해 이전에 실행한 명령어를 쉽게 확인하고 재사용할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
history [options] [arguments]
```

## Common Options
- `-c`: 현재 세션의 명령어 기록을 지웁니다.
- `-d offset`: 지정한 오프셋에 해당하는 명령어를 기록에서 삭제합니다.
- `n`: 마지막 n개의 명령어만 표시합니다.

## Common Examples
- 전체 명령어 기록 보기:
    ```bash
    history
    ```

- 마지막 10개의 명령어만 보기:
    ```bash
    history 10
    ```

- 특정 명령어 삭제 (예: 5번째 명령어):
    ```bash
    history -d 5
    ```

- 현재 세션의 명령어 기록 지우기:
    ```bash
    history -c
    ```

## Tips
- 자주 사용하는 명령어는 `!n` 형식으로 빠르게 실행할 수 있습니다. 여기서 n은 기록 번호입니다.
- `Ctrl + r`을 사용하여 이전 명령어를 검색할 수 있습니다.
- `history` 명령어의 출력을 파일로 저장하여 나중에 참조할 수 있습니다. 예를 들어:
    ```bash
    history > my_history.txt
    ```