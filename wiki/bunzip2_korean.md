# [리눅스] Bash bunzip2 사용법: bzip2 압축 해제

## Overview
`bunzip2` 명령어는 bzip2 형식으로 압축된 파일을 해제하는 데 사용됩니다. 이 명령어는 파일의 크기를 줄이기 위해 bzip2 알고리즘으로 압축된 파일을 원래 상태로 복원합니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
bunzip2 [옵션] [파일명]
```

## Common Options
- `-k`: 원본 파일을 삭제하지 않고 압축 해제합니다.
- `-f`: 기존 파일을 강제로 덮어씁니다.
- `-v`: 압축 해제 진행 상황을 자세히 보여줍니다.

## Common Examples
1. 기본적인 압축 해제:
   ```bash
   bunzip2 example.bz2
   ```

2. 원본 파일을 유지하면서 압축 해제:
   ```bash
   bunzip2 -k example.bz2
   ```

3. 기존 파일을 덮어쓰면서 압축 해제:
   ```bash
   bunzip2 -f example.bz2
   ```

4. 압축 해제 진행 상황을 자세히 보기:
   ```bash
   bunzip2 -v example.bz2
   ```

## Tips
- 압축 해제할 파일이 많은 경우, `-k` 옵션을 사용하여 원본 파일을 유지하는 것이 유용합니다.
- 압축 해제할 파일의 크기가 큰 경우, 충분한 디스크 공간이 있는지 확인하세요.
- `bunzip2`는 bzip2 형식의 파일만 해제할 수 있으므로, 다른 압축 형식의 파일에는 적합하지 않습니다.