# [리눅스] Bash jq 사용법: JSON 데이터 처리

## Overview
`jq`는 JSON 데이터를 필터링하고 변환하는 데 사용되는 강력한 커맨드라인 도구입니다. 이 도구를 사용하면 JSON 형식의 데이터를 쉽게 조회하고 조작할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
jq [options] [arguments]
```

## Common Options
- `-c`: 압축된 JSON 출력을 생성합니다.
- `-r`: 원시 문자열 출력을 생성하여 JSON 형식이 아닌 텍스트로 결과를 출력합니다.
- `-f <file>`: 필터를 정의한 파일을 사용합니다.
- `--arg <name> <value>`: 변수를 정의하여 필터 내에서 사용할 수 있습니다.

## Common Examples
다음은 `jq`의 몇 가지 실용적인 예입니다.

### 예제 1: JSON 파일에서 특정 필드 추출
```bash
jq '.name' data.json
```
위 명령은 `data.json` 파일에서 `name` 필드의 값을 출력합니다.

### 예제 2: 배열의 모든 요소 출력
```bash
jq '.items[]' data.json
```
이 명령은 `data.json` 파일의 `items` 배열에 있는 모든 요소를 출력합니다.

### 예제 3: 조건부 필터링
```bash
jq '.users[] | select(.age > 30)' data.json
```
이 명령은 `data.json` 파일에서 `age`가 30보다 큰 사용자만 필터링하여 출력합니다.

### 예제 4: JSON 데이터 수정
```bash
jq '.price = 19.99' data.json
```
이 명령은 `data.json` 파일의 `price` 필드를 19.99로 변경합니다.

## Tips
- JSON 데이터를 다룰 때는 항상 유효한 형식을 유지하는 것이 중요합니다.
- 복잡한 필터를 사용할 때는 `-f` 옵션을 사용하여 필터를 파일로 저장하면 관리가 용이합니다.
- `jq`의 다양한 기능을 활용하기 위해 공식 문서를 참고하는 것이 좋습니다.