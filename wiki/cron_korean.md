# [리눅스] Bash cron 사용법: 주기적으로 명령 실행

## Overview
cron 명령은 리눅스 및 유닉스 계열 운영 체제에서 주기적으로 특정 작업이나 명령을 실행하는 데 사용됩니다. 시스템 관리자는 cron을 통해 정기적인 백업, 시스템 모니터링, 스크립트 실행 등을 자동화할 수 있습니다.

## Usage
cron의 기본 구문은 다음과 같습니다:

```bash
crontab [options] [file]
```

## Common Options
- `-e`: 현재 사용자의 crontab을 편집합니다.
- `-l`: 현재 사용자의 crontab 목록을 출력합니다.
- `-r`: 현재 사용자의 crontab을 삭제합니다.
- `-i`: crontab 삭제 시 확인 메시지를 표시합니다.

## Common Examples
다음은 cron을 사용하는 몇 가지 일반적인 예입니다.

1. 매일 오전 2시에 스크립트 실행:
   ```bash
   0 2 * * * /path/to/script.sh
   ```

2. 매주 월요일 오전 8시에 백업 실행:
   ```bash
   0 8 * * 1 /path/to/backup.sh
   ```

3. 매 5분마다 로그 파일 정리:
   ```bash
   */5 * * * * /path/to/cleanup.sh
   ```

4. 매달 1일 자정에 데이터베이스 백업:
   ```bash
   0 0 1 * * /path/to/db_backup.sh
   ```

## Tips
- crontab 파일을 편집할 때는 항상 주석을 추가하여 어떤 작업이 수행되는지 설명하는 것이 좋습니다.
- 로그 파일을 사용하여 cron 작업의 출력을 기록하면 문제를 진단하는 데 도움이 됩니다.
- 시스템의 시간대 설정을 확인하여 cron 작업이 예상한 시간에 실행되는지 확인하세요.