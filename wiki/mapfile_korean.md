# [리눅스] Bash mapfile 사용법: 파일 내용을 배열로 읽기

## Overview
`mapfile` 명령어는 파일의 내용을 읽어 배열에 저장하는 데 사용됩니다. 이 명령어는 파일의 각 줄을 배열의 요소로 변환하여 쉽게 처리할 수 있게 해줍니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
mapfile [options] [arguments]
```

## Common Options
- `-n N`: N개의 줄만 읽습니다.
- `-s N`: N개의 줄을 건너뛰고 읽기 시작합니다.
- `-t`: 각 줄의 끝에 있는 개행 문자를 제거합니다.

## Common Examples
다음은 `mapfile` 명령어의 몇 가지 실용적인 예입니다.

### 예제 1: 파일 내용을 배열에 저장하기
```bash
mapfile lines < filename.txt
```
이 명령어는 `filename.txt` 파일의 내용을 읽어 `lines` 배열에 저장합니다.

### 예제 2: 특정 줄 수만 읽기
```bash
mapfile -n 5 lines < filename.txt
```
이 명령어는 `filename.txt` 파일에서 처음 5줄만 읽어 `lines` 배열에 저장합니다.

### 예제 3: 줄 건너뛰기
```bash
mapfile -s 2 lines < filename.txt
```
이 명령어는 `filename.txt` 파일의 처음 2줄을 건너뛰고 나머지 줄을 `lines` 배열에 저장합니다.

### 예제 4: 개행 문자 제거하기
```bash
mapfile -t lines < filename.txt
```
이 명령어는 `filename.txt` 파일의 내용을 읽어 각 줄의 끝에 있는 개행 문자를 제거한 후 `lines` 배열에 저장합니다.

## Tips
- `mapfile`을 사용할 때, 파일의 크기가 클 경우 메모리 사용량에 유의하세요.
- 배열의 내용을 확인하려면 `printf '%s\n' "${lines[@]}"` 명령어를 사용하여 출력할 수 있습니다.
- `mapfile`을 사용하여 스크립트에서 파일 내용을 쉽게 처리하고 조작할 수 있습니다.