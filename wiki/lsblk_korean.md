# [리눅스] Bash lsblk 사용법: 블록 장치 목록 표시

## Overview
`lsblk` 명령어는 시스템의 블록 장치 목록을 표시하는 데 사용됩니다. 이 명령어는 디스크, 파티션, 그리고 그에 따른 마운트 지점 등을 확인하는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
lsblk [options] [arguments]
```

## Common Options
- `-a`, `--all`: 모든 장치를 표시합니다. 마운트되지 않은 장치도 포함됩니다.
- `-f`, `--fs`: 파일 시스템 정보를 함께 표시합니다.
- `-l`, `--list`: 리스트 형식으로 출력합니다.
- `-o`, `--output`: 출력할 열을 지정합니다.
- `-p`, `--paths`: 장치의 전체 경로를 표시합니다.

## Common Examples
- 기본 블록 장치 목록 보기:
```bash
lsblk
```

- 모든 장치와 마운트되지 않은 장치 포함하여 보기:
```bash
lsblk -a
```

- 파일 시스템 정보와 함께 보기:
```bash
lsblk -f
```

- 특정 열만 출력하기 (예: NAME, SIZE, TYPE):
```bash
lsblk -o NAME,SIZE,TYPE
```

- 장치의 전체 경로 표시하기:
```bash
lsblk -p
```

## Tips
- `lsblk` 명령어는 `grep`과 함께 사용하여 특정 장치를 쉽게 찾을 수 있습니다. 예를 들어, `lsblk | grep sda`를 사용하면 `sda` 장치에 대한 정보만 필터링할 수 있습니다.
- `lsblk`의 출력 결과를 파일로 저장하려면 리다이렉션을 사용할 수 있습니다. 예를 들어, `lsblk > devices.txt` 명령어를 사용하면 장치 목록이 `devices.txt` 파일에 저장됩니다.
- `lsblk` 명령어는 시스템의 디스크 상태를 점검할 때 유용하므로, 정기적으로 확인하는 것이 좋습니다.