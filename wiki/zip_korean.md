# [리눅스] Bash zip 사용법: 파일 압축 및 아카이브 생성

## Overview
`zip` 명령어는 파일과 디렉토리를 압축하여 하나의 아카이브 파일로 만드는 데 사용됩니다. 이 명령어는 파일 크기를 줄이고, 여러 파일을 하나로 묶어 관리하기 쉽게 해줍니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
zip [옵션] [아카이브 이름] [압축할 파일들]
```

## Common Options
- `-r`: 디렉토리를 재귀적으로 압축합니다.
- `-e`: 암호로 아카이브를 보호합니다.
- `-9`: 최대 압축률을 사용합니다.
- `-q`: 압축 진행 상황을 표시하지 않습니다.

## Common Examples
1. **기본 파일 압축**
   ```bash
   zip my_archive.zip file1.txt file2.txt
   ```
   위 명령어는 `file1.txt`와 `file2.txt`를 `my_archive.zip`이라는 이름의 아카이브로 압축합니다.

2. **디렉토리 압축**
   ```bash
   zip -r my_archive.zip my_directory/
   ```
   `my_directory`라는 디렉토리와 그 안의 모든 파일을 압축합니다.

3. **암호로 보호된 압축 파일 생성**
   ```bash
   zip -e my_secure_archive.zip file1.txt
   ```
   `file1.txt`를 암호로 보호된 `my_secure_archive.zip`으로 압축합니다.

4. **최대 압축률로 압축**
   ```bash
   zip -9 my_archive.zip file1.txt file2.txt
   ```
   `file1.txt`와 `file2.txt`를 최대 압축률로 압축합니다.

## Tips
- 압축할 파일의 수가 많을 경우, 와일드카드를 사용하여 간편하게 지정할 수 있습니다. 예를 들어, `zip my_archive.zip *.txt`는 모든 텍스트 파일을 압축합니다.
- 암호를 설정할 때는 안전한 암호를 사용하는 것이 좋습니다.
- 압축 파일의 크기를 줄이기 위해 `-9` 옵션을 사용하되, 압축 시간이 길어질 수 있음을 유의하세요.