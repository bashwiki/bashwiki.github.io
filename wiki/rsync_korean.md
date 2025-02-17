# [리눅스] Bash rsync 사용법: 파일 및 디렉토리 동기화

## Overview
`rsync` 명령어는 파일과 디렉토리를 효율적으로 동기화하고 전송하는 데 사용됩니다. 로컬 및 원격 시스템 간에 데이터를 복사할 수 있으며, 변경된 부분만 전송하여 대역폭을 절약합니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
rsync [options] [source] [destination]
```

## Common Options
- `-a`: 아카이브 모드로, 파일의 권한, 시간, 심볼릭 링크 등을 유지합니다.
- `-v`: 진행 상황을 자세히 출력합니다.
- `-z`: 전송 중 데이터를 압축하여 대역폭을 절약합니다.
- `-r`: 하위 디렉토리를 재귀적으로 복사합니다.
- `--delete`: 대상에서 소스에 없는 파일을 삭제합니다.

## Common Examples
- 로컬 디렉토리 복사:
```bash
rsync -av /path/to/source/ /path/to/destination/
```

- 원격 서버로 파일 전송:
```bash
rsync -avz /local/path user@remote:/remote/path
```

- 원격 서버에서 로컬로 파일 다운로드:
```bash
rsync -avz user@remote:/remote/path /local/path
```

- 특정 파일 유형만 동기화 (예: `.jpg` 파일만):
```bash
rsync -av --include='*.jpg' --exclude='*' /path/to/source/ /path/to/destination/
```

## Tips
- `--dry-run` 옵션을 사용하여 실제 전송 없이 어떤 파일이 복사될지를 미리 확인할 수 있습니다.
- 대량의 파일을 전송할 때는 `-z` 옵션을 사용하여 전송 속도를 높일 수 있습니다.
- 정기적인 백업을 위해 cron 작업을 설정하여 자동으로 `rsync`를 실행할 수 있습니다.