# [리눅스] Bash tar 사용법: 파일 아카이브 및 압축

## Overview
`tar` 명령어는 파일과 디렉토리를 아카이브하고 압축하는 데 사용됩니다. 여러 파일을 하나의 파일로 묶어 관리하기 쉽게 만들고, 전송 및 저장을 용이하게 합니다.

## Usage
기본 구문은 다음과 같습니다:
```
tar [options] [arguments]
```

## Common Options
- `-c`: 새로운 아카이브 파일을 생성합니다.
- `-x`: 아카이브에서 파일을 추출합니다.
- `-f`: 아카이브 파일의 이름을 지정합니다.
- `-v`: 진행 상황을 자세히 출력합니다.
- `-z`: gzip으로 압축하거나 압축을 해제합니다.
- `-j`: bzip2로 압축하거나 압축을 해제합니다.

## Common Examples
1. **아카이브 생성하기**
   ```bash
   tar -cvf archive.tar /path/to/directory
   ```
   위 명령어는 `/path/to/directory`의 내용을 `archive.tar`라는 아카이브 파일로 생성합니다.

2. **gzip으로 압축된 아카이브 생성하기**
   ```bash
   tar -czvf archive.tar.gz /path/to/directory
   ```
   이 명령어는 `archive.tar.gz`라는 이름으로 gzip으로 압축된 아카이브를 생성합니다.

3. **아카이브에서 파일 추출하기**
   ```bash
   tar -xvf archive.tar
   ```
   이 명령어는 `archive.tar`에서 모든 파일을 현재 디렉토리로 추출합니다.

4. **gzip으로 압축된 아카이브에서 파일 추출하기**
   ```bash
   tar -xzvf archive.tar.gz
   ```
   이 명령어는 gzip으로 압축된 아카이브에서 파일을 추출합니다.

## Tips
- 아카이브 파일의 내용을 확인하려면 `-t` 옵션을 사용할 수 있습니다:
  ```bash
  tar -tvf archive.tar
  ```
- 대용량 파일을 다룰 때는 `-j` 옵션을 사용하여 bzip2로 압축하면 더 높은 압축률을 얻을 수 있습니다.
- 아카이브 파일을 생성할 때, `-C` 옵션을 사용하여 특정 디렉토리로 이동한 후 아카이브를 생성하면 경로를 간단하게 관리할 수 있습니다.