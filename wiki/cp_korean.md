# [리눅스] Bash cp 사용법: 파일 및 디렉토리 복사

## Overview
`cp` 명령어는 파일이나 디렉토리를 복사하는 데 사용됩니다. 이 명령어를 통해 원본 파일을 다른 위치에 복사하거나, 파일의 이름을 변경할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
cp [옵션] [원본] [대상]
```

## Common Options
- `-r`: 디렉토리를 재귀적으로 복사합니다.
- `-i`: 대상 파일이 존재할 경우, 덮어쓸 것인지 확인합니다.
- `-u`: 원본 파일이 대상 파일보다 새롭거나, 대상 파일이 존재하지 않을 경우에만 복사합니다.
- `-v`: 복사하는 동안 각 파일의 이름을 출력합니다.

## Common Examples
- **단일 파일 복사**:
  ```bash
  cp file.txt /path/to/destination/
  ```
  `file.txt`를 지정된 경로로 복사합니다.

- **파일 이름 변경**:
  ```bash
  cp file.txt newfile.txt
  ```
  `file.txt`를 `newfile.txt`라는 이름으로 복사합니다.

- **디렉토리 복사**:
  ```bash
  cp -r /path/to/source_directory /path/to/destination_directory
  ```
  `source_directory`를 재귀적으로 복사하여 `destination_directory`에 저장합니다.

- **덮어쓰기 확인**:
  ```bash
  cp -i file.txt /path/to/destination/
  ```
  대상 경로에 `file.txt`가 이미 존재할 경우, 덮어쓸 것인지 확인합니다.

## Tips
- 복사하기 전에 항상 원본 파일과 대상 경로를 확인하세요.
- `-v` 옵션을 사용하여 복사 과정을 모니터링하면 유용합니다.
- 대량의 파일을 복사할 때는 `-u` 옵션을 사용하여 불필요한 덮어쓰기를 방지하세요.