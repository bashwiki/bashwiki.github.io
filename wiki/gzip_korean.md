# [리눅스] Bash gzip 사용법: 파일 압축 및 해제

## Overview
gzip은 파일을 압축하는 데 사용되는 명령어로, 주로 텍스트 파일의 크기를 줄이는 데 유용합니다. 이 명령어는 GNU zip의 약자로, 데이터 전송 속도를 높이고 저장 공간을 절약하는 데 도움을 줍니다.

## Usage
기본 구문은 다음과 같습니다:
```
gzip [옵션] [파일명]
```

## Common Options
- `-d`, `--decompress`: 압축 해제 모드로 사용합니다.
- `-k`, `--keep`: 원본 파일을 유지하면서 압축합니다.
- `-v`, `--verbose`: 압축 과정의 상세 정보를 출력합니다.
- `-r`, `--recursive`: 디렉토리 내의 모든 파일을 재귀적으로 압축합니다.

## Common Examples
- **파일 압축하기**
  ```bash
  gzip example.txt
  ```
  이 명령어는 `example.txt` 파일을 압축하여 `example.txt.gz`라는 파일을 생성합니다.

- **압축 해제하기**
  ```bash
  gzip -d example.txt.gz
  ```
  이 명령어는 `example.txt.gz` 파일의 압축을 해제하여 원본 파일인 `example.txt`를 복원합니다.

- **원본 파일 유지하며 압축하기**
  ```bash
  gzip -k example.txt
  ```
  이 명령어는 `example.txt`를 압축하되, 원본 파일을 그대로 유지합니다.

- **디렉토리 내 모든 파일 압축하기**
  ```bash
  gzip -r my_directory/
  ```
  이 명령어는 `my_directory` 내의 모든 파일을 재귀적으로 압축합니다.

## Tips
- gzip으로 압축한 파일은 `.gz` 확장자를 가지므로, 파일 형식을 쉽게 식별할 수 있습니다.
- 대용량 파일을 압축할 때는 `-v` 옵션을 사용하여 진행 상황을 확인하는 것이 좋습니다.
- 압축된 파일을 자주 사용해야 한다면, `-k` 옵션을 사용하여 원본 파일을 보존하는 것이 유용합니다.