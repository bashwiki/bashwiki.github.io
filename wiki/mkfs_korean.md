# [리눅스] Bash mkfs 사용법: 파일 시스템 생성

## Overview
`mkfs` 명령어는 리눅스에서 파일 시스템을 생성하는 데 사용됩니다. 이 명령어는 주로 디스크 파티션이나 저장 장치에 새로운 파일 시스템을 설정할 때 사용됩니다.

## Usage
기본 구문은 다음과 같습니다:
```
mkfs [options] [arguments]
```

## Common Options
- `-t, --type`: 생성할 파일 시스템의 유형을 지정합니다. 예: `ext4`, `vfat` 등.
- `-L, --label`: 파일 시스템에 레이블을 지정합니다.
- `-n, --no-progress`: 진행 상태를 표시하지 않습니다.
- `-V, --version`: mkfs의 버전을 표시합니다.

## Common Examples
1. **ext4 파일 시스템 생성**
   ```bash
   mkfs.ext4 /dev/sdX1
   ```

2. **vfat 파일 시스템 생성**
   ```bash
   mkfs.vfat /dev/sdX1
   ```

3. **파일 시스템에 레이블 지정**
   ```bash
   mkfs.ext4 -L mylabel /dev/sdX1
   ```

4. **진행 상태 표시하지 않기**
   ```bash
   mkfs.ext4 -n /dev/sdX1
   ```

## Tips
- 파일 시스템을 생성하기 전에 해당 장치의 데이터를 백업하세요. `mkfs` 명령어는 기존 데이터를 삭제합니다.
- 올바른 장치를 선택했는지 항상 확인하세요. 잘못된 장치를 지정하면 데이터 손실이 발생할 수 있습니다.
- 파일 시스템 유형을 선택할 때, 사용 목적에 맞는 유형을 선택하는 것이 중요합니다.