# [리눅스] Bash 7z 사용법: 파일 압축 및 해제

## Overview
7z 명령은 파일 및 디렉토리를 압축하고 해제하는 데 사용되는 강력한 도구입니다. 다양한 압축 형식을 지원하며, 높은 압축률을 자랑합니다.

## Usage
기본 구문은 다음과 같습니다:
```
7z [options] [arguments]
```

## Common Options
- `a`: 파일을 압축하여 아카이브를 생성합니다.
- `x`: 아카이브에서 파일을 추출합니다.
- `t`: 아카이브의 형식을 지정합니다.
- `l`: 아카이브의 내용을 나열합니다.
- `d`: 아카이브에서 파일을 삭제합니다.

## Common Examples
- **파일 압축하기**: 
  ```bash
  7z a archive.7z file1.txt file2.txt
  ```
  위 명령은 `file1.txt`와 `file2.txt`를 `archive.7z`라는 이름으로 압축합니다.

- **아카이브에서 파일 추출하기**:
  ```bash
  7z x archive.7z
  ```
  이 명령은 `archive.7z`에서 모든 파일을 현재 디렉토리로 추출합니다.

- **아카이브 내용 나열하기**:
  ```bash
  7z l archive.7z
  ```
  위 명령은 `archive.7z`의 내용을 나열합니다.

- **특정 파일 삭제하기**:
  ```bash
  7z d archive.7z file1.txt
  ```
  이 명령은 `archive.7z`에서 `file1.txt`를 삭제합니다.

## Tips
- 압축할 파일이 많을 경우, 와일드카드(`*`)를 사용하여 간편하게 지정할 수 있습니다.
- 압축률을 높이려면 `-mx=9` 옵션을 추가하여 최대 압축을 사용할 수 있습니다.
- 대용량 파일을 다룰 때는 `-mmt` 옵션을 사용하여 멀티스레딩을 활성화하면 성능을 개선할 수 있습니다.