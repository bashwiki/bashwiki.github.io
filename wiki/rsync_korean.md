# [리눅스] Bash rsync 사용법

## Overview
`rsync`는 파일과 디렉토리를 로컬 및 원격 시스템 간에 효율적으로 동기화하는 데 사용되는 강력한 도구입니다. 이 명령은 파일 전송 시 변경된 부분만 전송하여 대역폭을 절약하고 전송 속도를 높이는 특징이 있습니다. 주로 백업, 미러링, 또는 파일 배포 작업에 사용됩니다.

## Usage
`rsync`의 기본 구문은 다음과 같습니다:

```
rsync [옵션] [소스] [대상]
```

### 일반적인 옵션
- `-a`: 아카이브 모드로, 파일의 소유권, 권한, 타임스탬프 등을 유지합니다.
- `-v`: 진행 상황을 자세히 출력합니다 (verbose).
- `-z`: 전송 중 데이터 압축을 활성화합니다.
- `-r`: 하위 디렉토리를 재귀적으로 복사합니다.
- `--delete`: 대상 디렉토리에서 소스에 없는 파일을 삭제합니다.

## Examples
### 예제 1: 로컬 디렉토리 동기화
로컬 시스템에서 `source_directory`의 내용을 `destination_directory`로 동기화하려면 다음 명령을 사용합니다:

```bash
rsync -av source_directory/ destination_directory/
```

이 명령은 `source_directory`의 모든 파일과 하위 디렉토리를 `destination_directory`로 복사하며, 파일의 메타데이터를 유지합니다.

### 예제 2: 원격 서버로 파일 전송
원격 서버에 파일을 전송하려면 다음과 같이 사용할 수 있습니다:

```bash
rsync -avz /local/path user@remote_host:/remote/path
```

이 명령은 로컬 경로의 파일을 원격 호스트의 지정된 경로로 압축하여 전송합니다.

## Tips
- `--dry-run` 옵션을 사용하여 실제로 파일을 전송하기 전에 어떤 파일이 전송될지를 미리 확인할 수 있습니다. 예를 들어:

```bash
rsync -av --dry-run source_directory/ destination_directory/
```

- 대량의 파일을 전송할 때는 `-z` 옵션을 사용하여 대역폭을 절약할 수 있습니다.
- 정기적인 백업 작업을 위해 `cron`과 함께 `rsync`를 사용할 수 있습니다.