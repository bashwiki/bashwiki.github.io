# [리눅스] Bash xmlstarlet 사용법: XML 파일을 처리하는 도구

## Overview
xmlstarlet은 XML 파일을 생성, 변환, 쿼리 및 수정할 수 있는 강력한 명령줄 도구입니다. 이 도구는 XML 데이터의 구조를 쉽게 조작하고, 필요한 정보를 추출하는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
xmlstarlet [options] [arguments]
```

## Common Options
- `sel`: XML 문서에서 특정 요소를 선택합니다.
- `val`: XML 문서의 유효성을 검사합니다.
- `ed`: XML 문서를 수정합니다.
- `tr`: XML 문서를 변환합니다.
- `fo`: XML 문서를 포맷합니다.

## Common Examples
1. XML 파일에서 특정 요소 선택하기:
   ```bash
   xmlstarlet sel -t -m "/root/element" -v "." -n file.xml
   ```

2. XML 파일의 유효성 검사하기:
   ```bash
   xmlstarlet val -e file.xml
   ```

3. XML 파일 수정하기 (예: 특정 요소의 값을 변경하기):
   ```bash
   xmlstarlet ed -u "/root/element" -v "new_value" file.xml
   ```

4. XML 파일 포맷하기:
   ```bash
   xmlstarlet fo file.xml
   ```

5. XML 파일을 JSON으로 변환하기:
   ```bash
   xmlstarlet xml2json file.xml
   ```

## Tips
- XML 파일을 수정하기 전에 항상 백업을 만들어 두세요.
- 복잡한 XML 구조를 다룰 때는 XPath 표현식을 잘 이해하고 사용하는 것이 중요합니다.
- xmlstarlet의 다양한 옵션을 활용하여 작업을 자동화할 수 있습니다.