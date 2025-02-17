# [리눅스] Bash paste 사용법: 여러 파일의 내용을 병합하기

## Overview
`paste` 명령어는 여러 파일의 내용을 수평으로 병합하여 출력하는 데 사용됩니다. 각 파일의 각 줄을 탭으로 구분하여 결합하므로, 데이터 파일을 쉽게 결합할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
paste [options] [arguments]
```

## Common Options
- `-d` : 구분자를 지정합니다. 기본값은 탭입니다.
- `-s` : 각 파일의 내용을 수직으로 병합합니다.
- `-z` : 널 문자(`\0`)로 구분된 입력을 처리합니다.

## Common Examples

1. **기본 사용법**
   두 개의 파일 `file1.txt`와 `file2.txt`의 내용을 병합합니다.
   ```bash
   paste file1.txt file2.txt
   ```

2. **구분자 변경**
   쉼표로 구분하여 파일을 병합합니다.
   ```bash
   paste -d ',' file1.txt file2.txt
   ```

3. **수직 병합**
   파일의 내용을 수직으로 병합하여 출력합니다.
   ```bash
   paste -s file1.txt file2.txt
   ```

4. **여러 파일 병합**
   세 개 이상의 파일을 병합합니다.
   ```bash
   paste file1.txt file2.txt file3.txt
   ```

5. **널 문자로 구분된 파일 처리**
   널 문자로 구분된 파일을 병합합니다.
   ```bash
   paste -z file1.txt file2.txt
   ```

## Tips
- 파일의 내용이 다를 경우, 짧은 파일의 빈 줄은 자동으로 채워지지 않으므로 주의하세요.
- 구분자를 설정할 때 여러 문자도 사용할 수 있습니다. 예를 들어, `-d ' - '`를 사용하면 하이픈으로 구분할 수 있습니다.
- `paste` 명령어는 데이터 처리 시 매우 유용하므로, 스크립트에서 자주 활용할 수 있습니다.