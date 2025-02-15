# [리눅스] Bash xmlstarlet 사용법

## Overview
`xmlstarlet`은 XML 파일을 처리하고 변환하는 데 사용되는 강력한 명령줄 도구입니다. 이 도구는 XML 문서를 읽고, 수정하고, 생성하며, 다양한 형식으로 출력할 수 있는 기능을 제공합니다. XML 데이터를 쉽게 조작할 수 있도록 도와주며, 스크립트와 자동화 작업에서 유용하게 사용됩니다.

## Usage
`xmlstarlet`의 기본 구문은 다음과 같습니다:

```
xmlstarlet [옵션] [명령] [인자]
```

### 일반적인 옵션
- `-e`, `--eval`: XPath 표현식을 평가합니다.
- `-r`, `--replace`: XML 문서 내의 특정 노드를 대체합니다.
- `-d`, `--delete`: XML 문서에서 특정 노드를 삭제합니다.
- `-s`, `--substitute`: XML 문서에 새로운 노드를 추가합니다.
- `-t`, `--transform`: XSLT 변환을 수행합니다.

## Examples
### 예제 1: XML 파일에서 특정 요소 추출하기
다음 명령은 `example.xml` 파일에서 `<title>` 요소의 값을 추출합니다.

```bash
xmlstarlet sel -t -m "//title" -v "." -n example.xml
```

### 예제 2: XML 파일에서 특정 요소 수정하기
다음 명령은 `example.xml` 파일의 `<author>` 요소를 "John Doe"로 변경합니다.

```bash
xmlstarlet ed -u "//author" -v "John Doe" example.xml
```

## Tips
- XML 파일을 수정하기 전에 항상 원본 파일의 백업을 만들어 두는 것이 좋습니다.
- 복잡한 XPath 표현식을 사용할 때는 `xmlstarlet`의 `sel` 명령을 활용하여 원하는 데이터를 정확하게 선택할 수 있습니다.
- `xmlstarlet`의 다양한 기능을 활용하기 위해 공식 문서나 매뉴얼 페이지를 참고하는 것이 유용합니다.