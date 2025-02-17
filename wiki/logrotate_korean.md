# [리눅스] Bash logrotate 사용법: 로그 파일 관리

## Overview
logrotate 명령어는 시스템의 로그 파일을 관리하는 데 사용됩니다. 이 명령어는 로그 파일의 크기를 조절하고, 오래된 로그 파일을 압축하거나 삭제하여 디스크 공간을 절약하는 데 도움을 줍니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
logrotate [options] [arguments]
```

## Common Options
- `-f`: 강제로 로그 회전을 수행합니다.
- `-s`: 상태 파일의 경로를 지정합니다.
- `-v`: 자세한 출력을 표시합니다.
- `-d`: 실제로 회전을 수행하지 않고 어떤 일이 일어날지를 보여줍니다.

## Common Examples
1. 기본 설정 파일을 사용하여 로그 회전 수행:
   ```bash
   logrotate /etc/logrotate.conf
   ```

2. 특정 설정 파일을 사용하여 로그 회전 수행:
   ```bash
   logrotate -f /etc/logrotate.d/myapp
   ```

3. 로그 회전 상태 확인 (실제 회전하지 않음):
   ```bash
   logrotate -d /etc/logrotate.conf
   ```

4. 로그 회전의 자세한 정보 출력:
   ```bash
   logrotate -v /etc/logrotate.conf
   ```

## Tips
- 주기적으로 로그 파일을 회전하도록 cron 작업을 설정하면 자동으로 로그를 관리할 수 있습니다.
- 설정 파일에서 로그 파일의 최대 크기와 보관 기간을 적절히 조정하여 디스크 공간을 효율적으로 사용할 수 있습니다.
- 로그 파일 회전 후 압축을 설정하면 저장 공간을 더욱 절약할 수 있습니다.