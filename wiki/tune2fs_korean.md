# [리눅스] Bash tune2fs 사용법: 파일 시스템 조정

## Overview
`tune2fs` 명령어는 ext2, ext3, ext4 파일 시스템의 다양한 파라미터를 조정하는 데 사용됩니다. 이 명령어를 통해 파일 시스템의 성능을 최적화하거나 특정 기능을 활성화할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```
tune2fs [options] [arguments]
```

## Common Options
- `-c <max_mount_count>`: 최대 마운트 횟수를 설정합니다.
- `-i <interval>`: 파일 시스템 점검을 위한 시간 간격을 설정합니다.
- `-m <reserved_blocks_percentage>`: 예약 블록의 비율을 설정합니다.
- `-O <feature>`: 특정 파일 시스템 기능을 활성화합니다.
- `-L <label>`: 파일 시스템 레이블을 설정합니다.

## Common Examples
- 최대 마운트 횟수를 20으로 설정:
  ```bash
  tune2fs -c 20 /dev/sda1
  ```

- 30일마다 파일 시스템 점검을 설정:
  ```bash
  tune2fs -i 30d /dev/sda1
  ```

- 예약 블록 비율을 5%로 설정:
  ```bash
  tune2fs -m 5 /dev/sda1
  ```

- 파일 시스템에 'mydata'라는 레이블 설정:
  ```bash
  tune2fs -L mydata /dev/sda1
  ```

- 특정 기능(예: dir_index) 활성화:
  ```bash
  tune2fs -O dir_index /dev/sda1
  ```

## Tips
- `tune2fs` 명령어를 사용하기 전에 파일 시스템이 마운트 해제되어 있는지 확인하세요.
- 중요한 변경을 수행하기 전에 항상 백업을 유지하는 것이 좋습니다.
- 파일 시스템의 현재 상태를 확인하려면 `tune2fs -l /dev/sda1` 명령어를 사용하여 정보를 확인할 수 있습니다.