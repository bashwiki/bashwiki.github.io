# [리눅스] Bash dd 사용법: 데이터 복사 및 변환

## Overview
`dd` 명령어는 파일을 복사하고 변환하는 데 사용됩니다. 주로 디스크 이미지 생성, 데이터 백업 및 복원, 파일 형식 변환 등에 활용됩니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
dd [옵션] [인수]
```

## Common Options
- `if=`: 입력 파일을 지정합니다.
- `of=`: 출력 파일을 지정합니다.
- `bs=`: 블록 크기를 설정합니다.
- `count=`: 복사할 블록 수를 지정합니다.
- `status=`: 진행 상태를 출력하는 방법을 설정합니다 (예: `none`, `noxfer`, `progress`).

## Common Examples
- **디스크 이미지 생성**
  ```bash
  dd if=/dev/sda of=/path/to/disk_image.img bs=4M
  ```
  이 명령어는 `/dev/sda`의 내용을 `disk_image.img` 파일로 복사합니다.

- **디스크 복원**
  ```bash
  dd if=/path/to/disk_image.img of=/dev/sda bs=4M
  ```
  이 명령어는 `disk_image.img` 파일의 내용을 `/dev/sda`에 복원합니다.

- **파일 복사**
  ```bash
  dd if=/path/to/source_file of=/path/to/destination_file bs=1M
  ```
  이 명령어는 `source_file`을 `destination_file`로 복사합니다.

- **데이터 덮어쓰기**
  ```bash
  dd if=/dev/zero of=/path/to/file bs=1M count=10
  ```
  이 명령어는 `file`을 10MB 크기의 0으로 덮어씁니다.

## Tips
- `dd` 명령어는 매우 강력하지만, 잘못 사용할 경우 데이터 손실이 발생할 수 있으므로 주의해야 합니다.
- `status=progress` 옵션을 사용하여 진행 상황을 실시간으로 확인할 수 있습니다.
- 중요한 데이터 작업을 수행하기 전에 항상 백업을 만들어 두는 것이 좋습니다.