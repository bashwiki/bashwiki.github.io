# [리눅스] Bash tee 사용법: 표준 출력을 파일로 저장하고 동시에 출력하기

## Overview
`tee` 명령어는 표준 입력을 받아서 파일에 저장하면서 동시에 표준 출력으로 전달하는 기능을 제공합니다. 이를 통해 데이터를 파일로 기록하면서도 화면에서 결과를 확인할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```
tee [옵션] [파일명]
```

## Common Options
- `-a`, `--append`: 파일에 내용을 추가합니다. 기본적으로 `tee`는 파일을 덮어씁니다.
- `-i`, `--ignore-interrupts`: 인터럽트 신호를 무시합니다.
- `--help`: `tee` 명령어의 도움말을 표시합니다.
- `--version`: `tee` 명령어의 버전을 표시합니다.

## Common Examples
다음은 `tee` 명령어의 몇 가지 실용적인 예시입니다.

1. **기본 사용법**
   ```bash
   echo "Hello, World!" | tee output.txt
   ```
   위 명령은 "Hello, World!"라는 문자열을 `output.txt` 파일에 저장하고 동시에 화면에도 출력합니다.

2. **파일에 추가하기**
   ```bash
   echo "Another line" | tee -a output.txt
   ```
   이 명령은 `output.txt` 파일에 "Another line"을 추가하고 화면에도 출력합니다.

3. **여러 파일에 출력하기**
   ```bash
   echo "Logging to multiple files" | tee file1.txt file2.txt
   ```
   이 명령은 "Logging to multiple files"라는 문자열을 `file1.txt`와 `file2.txt` 두 파일에 저장하고 동시에 화면에 출력합니다.

4. **인터럽트 신호 무시하기**
   ```bash
   some_command | tee -i output.txt
   ```
   이 명령은 `some_command`의 출력을 `output.txt`에 저장하면서 인터럽트 신호를 무시합니다.

## Tips
- `tee`를 사용할 때 `-a` 옵션을 활용하면 기존 파일에 데이터를 추가할 수 있어 유용합니다.
- 파이프라인에서 `tee`를 사용하여 중간 결과를 파일로 저장하고, 이후의 명령어에서 그 파일을 참조할 수 있습니다.
- 스크립트에서 로그를 기록할 때 `tee`를 사용하면 실시간으로 로그를 확인하면서 파일에도 기록할 수 있어 편리합니다.