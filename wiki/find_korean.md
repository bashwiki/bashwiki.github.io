# [리눅스] Bash find 사용법: 파일 이름 찾기

## Overview
`find` 명령어는 지정된 디렉토리에서 파일과 디렉토리를 검색하는 데 사용됩니다. 사용자는 다양한 조건을 설정하여 원하는 파일을 쉽게 찾을 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
find [옵션] [인수]
```

## Common Options
- `-name`: 특정 이름의 파일을 찾습니다.
- `-type`: 파일 유형을 지정하여 검색합니다. 예: `f` (파일), `d` (디렉토리).
- `-size`: 파일 크기를 기준으로 검색합니다.
- `-mtime`: 파일의 수정 시간을 기준으로 검색합니다.
- `-exec`: 찾은 파일에 대해 명령어를 실행합니다.

## Common Examples
- 특정 이름의 파일 찾기:
  ```bash
  find /path/to/directory -name "filename.txt"
  ```

- 특정 유형의 파일 찾기 (예: 디렉토리):
  ```bash
  find /path/to/directory -type d
  ```

- 10MB 이상 크기의 파일 찾기:
  ```bash
  find /path/to/directory -size +10M
  ```

- 최근 7일 이내에 수정된 파일 찾기:
  ```bash
  find /path/to/directory -mtime -7
  ```

- 찾은 파일에 대해 명령어 실행하기 (예: 삭제):
  ```bash
  find /path/to/directory -name "*.tmp" -exec rm {} \;
  ```

## Tips
- 검색 범위를 좁히기 위해 `-maxdepth` 옵션을 사용하여 하위 디렉토리의 깊이를 제한할 수 있습니다.
- 여러 조건을 조합하여 사용할 수 있으며, `-o` (또는) 및 `-a` (그리고) 연산자를 활용해 복잡한 검색이 가능합니다.
- `-print` 옵션을 사용하여 찾은 파일의 경로를 출력할 수 있습니다. 기본적으로 `find`는 결과를 출력합니다.