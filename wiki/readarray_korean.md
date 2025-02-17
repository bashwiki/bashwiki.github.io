# [리눅스] Bash readarray 사용법: 배열에 데이터 읽기

## Overview
`readarray` 명령은 입력 데이터를 배열로 읽어들이는 Bash 내장 명령입니다. 주로 파일이나 표준 입력에서 데이터를 읽어 배열 변수에 저장할 때 사용됩니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
readarray [options] [arguments]
```

## Common Options
- `-n N`: 배열에 읽어들일 줄 수를 N으로 제한합니다.
- `-s N`: N번째 줄부터 읽기 시작합니다.
- `-t`: 각 줄의 끝에 있는 개행 문자를 제거합니다.

## Common Examples

1. **파일에서 배열로 읽기**
   ```bash
   readarray lines < filename.txt
   ```
   이 명령은 `filename.txt` 파일의 각 줄을 `lines` 배열에 저장합니다.

2. **표준 입력에서 읽기**
   ```bash
   echo -e "line1\nline2\nline3" | readarray my_array
   ```
   위 명령은 표준 입력에서 데이터를 읽어 `my_array` 배열에 저장합니다.

3. **특정 줄 수만 읽기**
   ```bash
   readarray -n 2 lines < filename.txt
   ```
   이 명령은 `filename.txt` 파일에서 처음 2줄만 읽어 `lines` 배열에 저장합니다.

4. **줄 끝 개행 문자 제거**
   ```bash
   readarray -t lines < filename.txt
   ```
   이 명령은 `filename.txt` 파일의 각 줄을 읽어 `lines` 배열에 저장하며, 각 줄의 끝에 있는 개행 문자를 제거합니다.

## Tips
- 배열의 내용을 확인하려면 `printf '%s\n' "${lines[@]}"`와 같은 명령을 사용할 수 있습니다.
- `readarray`는 대량의 데이터를 처리할 때 유용하며, 파일의 각 줄을 쉽게 배열로 변환할 수 있습니다.
- 배열의 크기를 확인하려면 `echo ${#lines[@]}`를 사용하세요.