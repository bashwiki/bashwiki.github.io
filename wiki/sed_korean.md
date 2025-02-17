# [리눅스] Bash sed 사용법: 텍스트 변환 및 편집

## Overview
`sed`는 스트림 편집기(Stream Editor)로, 주로 텍스트 파일의 내용을 변환하거나 편집하는 데 사용됩니다. 파일의 내용을 실시간으로 수정할 수 있으며, 주로 정규 표현식을 사용하여 패턴을 찾고 변경하는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
sed [options] [arguments]
```

## Common Options
- `-e`: 여러 개의 편집 명령을 사용할 때 사용합니다.
- `-i`: 파일을 직접 수정합니다. 백업 파일을 만들고 싶다면 `-i.bak`와 같이 사용할 수 있습니다.
- `-n`: 기본적으로 출력을 하지 않으며, `p` 명령을 사용한 경우에만 출력을 합니다.
- `s`: 문자열 치환을 수행하는 명령입니다.

## Common Examples
1. **문자열 치환**
   ```bash
   sed 's/old/new/' filename.txt
   ```
   `filename.txt` 파일에서 첫 번째 `old`를 `new`로 변경합니다.

2. **모든 문자열 치환**
   ```bash
   sed 's/old/new/g' filename.txt
   ```
   `filename.txt` 파일에서 모든 `old`를 `new`로 변경합니다.

3. **파일 직접 수정**
   ```bash
   sed -i 's/old/new/g' filename.txt
   ```
   `filename.txt` 파일을 직접 수정하여 모든 `old`를 `new`로 변경합니다.

4. **특정 줄 삭제**
   ```bash
   sed '3d' filename.txt
   ```
   `filename.txt` 파일의 3번째 줄을 삭제합니다.

5. **줄 번호로 특정 줄 변경**
   ```bash
   sed '2s/old/new/' filename.txt
   ```
   `filename.txt` 파일의 2번째 줄에서 `old`를 `new`로 변경합니다.

## Tips
- `-n` 옵션을 사용하여 필요한 출력만 필터링할 수 있습니다.
- 정규 표현식을 활용하여 복잡한 패턴을 쉽게 찾고 수정할 수 있습니다.
- 테스트를 위해 `-e` 옵션을 사용하여 여러 명령을 함께 실행해 볼 수 있습니다.