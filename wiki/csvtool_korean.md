# [리눅스] Bash csvtool 사용법: CSV 파일 처리 도구

## Overview
csvtool은 CSV(Comma-Separated Values) 파일을 쉽게 처리하고 조작할 수 있는 명령어입니다. 이 도구를 사용하면 CSV 파일의 내용을 필터링, 변환 및 출력할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
csvtool [options] [arguments]
```

## Common Options
- `-c, --columns`: 특정 열을 선택하여 출력합니다.
- `-r, --rows`: 특정 행을 선택하여 출력합니다.
- `-t, --type`: CSV 파일의 구분자를 지정합니다. 기본값은 쉼표입니다.
- `-h, --header`: 헤더가 포함된 CSV 파일에서 헤더를 처리합니다.

## Common Examples
- 특정 열 선택하기:
```bash
csvtool -c 1,3 data.csv
```
위 명령어는 `data.csv` 파일에서 첫 번째와 세 번째 열을 출력합니다.

- 특정 행 선택하기:
```bash
csvtool -r 2,4 data.csv
```
이 명령어는 `data.csv` 파일에서 두 번째와 네 번째 행을 출력합니다.

- 구분자 변경하기:
```bash
csvtool -t ";" data.csv
```
위 명령어는 `data.csv` 파일에서 세미콜론을 구분자로 사용하여 데이터를 처리합니다.

- 헤더 포함하여 출력하기:
```bash
csvtool -h -c 1,2 data.csv
```
이 명령어는 `data.csv` 파일에서 첫 번째와 두 번째 열을 헤더와 함께 출력합니다.

## Tips
- CSV 파일의 구조를 미리 확인한 후 필요한 열과 행을 선택하는 것이 좋습니다.
- 대량의 데이터를 처리할 때는 필터링 옵션을 활용하여 필요한 정보만 추출하세요.
- 다양한 구분자를 사용하는 CSV 파일을 다룰 때는 `-t` 옵션을 적절히 사용하여 정확한 결과를 얻으세요.