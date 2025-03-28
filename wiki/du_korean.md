# [리눅스] Bash du 사용법: 디스크 사용량 확인

## Overview
`du` 명령어는 디스크 사용량을 확인하는 데 사용됩니다. 특정 디렉토리나 파일이 차지하는 공간을 측정하여, 시스템의 저장 공간을 효율적으로 관리하는 데 도움을 줍니다.

## Usage
기본 구문은 다음과 같습니다.
```bash
du [옵션] [인수]
```

## Common Options
- `-h`: 사람이 읽기 쉬운 형식으로 출력합니다 (예: KB, MB).
- `-s`: 각 인수에 대한 총합만을 표시합니다.
- `-a`: 모든 파일과 디렉토리의 크기를 표시합니다.
- `-c`: 총합을 포함하여 모든 항목의 크기를 표시합니다.

## Common Examples
- 현재 디렉토리의 디스크 사용량 확인:
```bash
du -h
```

- 특정 디렉토리의 총 디스크 사용량 확인:
```bash
du -sh /path/to/directory
```

- 모든 파일과 디렉토리의 크기를 확인:
```bash
du -ah /path/to/directory
```

- 여러 디렉토리의 총 디스크 사용량 확인:
```bash
du -sh /path/to/directory1 /path/to/directory2
```

## Tips
- `du` 명령어는 `-h` 옵션과 함께 사용하면 결과를 더 쉽게 이해할 수 있습니다.
- 큰 디렉토리의 사용량을 확인할 때는 `-s` 옵션을 사용하여 요약 정보를 얻는 것이 유용합니다.
- `du`와 `sort` 명령어를 조합하여 디스크 사용량이 큰 파일이나 디렉토리를 쉽게 찾을 수 있습니다. 예를 들어:
```bash
du -ah /path/to/directory | sort -hr | head -n 10
```