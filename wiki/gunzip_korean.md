# [리눅스] Bash gunzip 사용법: 압축 해제하기

## Overview
`gunzip` 명령어는 Gzip 형식으로 압축된 파일을 해제하는 데 사용됩니다. 이 명령어는 파일의 크기를 줄이기 위해 Gzip 알고리즘을 사용하여 압축된 파일을 원래의 상태로 복원합니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
gunzip [options] [arguments]
```

## Common Options
- `-c`: 압축 해제된 내용을 표준 출력으로 보냅니다.
- `-f`: 기존 파일을 덮어쓰도록 강제합니다.
- `-k`: 압축 해제 후 원본 파일을 유지합니다.
- `-r`: 디렉토리 내의 모든 Gzip 파일을 재귀적으로 압축 해제합니다.

## Common Examples
- 단일 Gzip 파일 압축 해제:
```bash
gunzip example.txt.gz
```

- 압축 해제된 내용을 표준 출력으로 보기:
```bash
gunzip -c example.txt.gz
```

- 기존 파일을 덮어쓰면서 압축 해제:
```bash
gunzip -f example.txt.gz
```

- 압축 해제 후 원본 파일 유지:
```bash
gunzip -k example.txt.gz
```

- 디렉토리 내 모든 Gzip 파일 재귀적으로 압축 해제:
```bash
gunzip -r /path/to/directory
```

## Tips
- 압축 해제된 파일이 많을 경우, `-k` 옵션을 사용하여 원본 파일을 유지하는 것이 유용합니다.
- 대량의 파일을 처리할 때는 `-r` 옵션을 사용하여 디렉토리 전체를 한 번에 처리할 수 있습니다.
- `gunzip` 명령어를 사용할 때, 파일의 확장자가 `.gz`인지 확인하는 것이 좋습니다.