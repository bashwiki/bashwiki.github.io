# [리눅스] Bash dirname 사용법

## 개요
`dirname` 명령어는 주어진 파일 경로에서 디렉토리 부분을 추출하는 데 사용됩니다. 주로 파일의 경로에서 디렉토리 이름만 필요할 때 유용합니다. 이 명령어는 스크립트나 명령어 줄에서 파일 경로를 처리할 때 자주 사용됩니다.

## 사용법
`dirname`의 기본 구문은 다음과 같습니다:

```bash
dirname [옵션] <경로>
```

### 일반적인 옵션
- `-z`, `--zero`: 입력 경로가 널 문자로 구분된 경우 사용합니다. 이 옵션을 사용하면 여러 경로를 한 번에 처리할 수 있습니다.

## 예제
### 예제 1: 기본 사용법
다음은 파일 경로에서 디렉토리 이름을 추출하는 간단한 예입니다.

```bash
$ dirname /home/user/documents/file.txt
/home/user/documents
```

위의 명령어는 `/home/user/documents/file.txt` 경로에서 디렉토리 부분인 `/home/user/documents`를 반환합니다.

### 예제 2: 상대 경로 사용
상대 경로를 사용할 때도 `dirname`은 유용합니다.

```bash
$ dirname ./projects/my_project/main.py
./projects/my_project
```

이 경우, 현재 디렉토리에서 `main.py` 파일이 위치한 디렉토리 경로를 반환합니다.

## 팁
- `dirname`은 스크립트에서 파일 경로를 동적으로 처리할 때 매우 유용합니다. 예를 들어, 특정 디렉토리 내의 모든 파일에 대해 작업을 수행할 때 `dirname`을 사용하여 경로를 쉽게 관리할 수 있습니다.
- `dirname`과 `basename`을 함께 사용하면 파일 경로에서 디렉토리와 파일 이름을 모두 쉽게 추출할 수 있습니다. 예를 들어:

```bash
$ file_path="/home/user/documents/file.txt"
$ dir=$(dirname "$file_path")
$ base=$(basename "$file_path")
echo "Directory: $dir"
echo "File: $base"
```

이렇게 하면 디렉토리와 파일 이름을 각각 변수에 저장하여 사용할 수 있습니다.