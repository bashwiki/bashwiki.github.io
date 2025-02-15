# [리눅스] Bash scp 사용법

## 개요
`scp` (Secure Copy Protocol)는 네트워크를 통해 파일을 안전하게 복사하는 데 사용되는 명령어입니다. SSH 프로토콜을 기반으로 하여 원격 서버와 로컬 시스템 간에 파일을 전송할 수 있습니다. `scp`는 데이터 전송 중 암호화를 제공하여 보안성을 높입니다.

## 사용법
`scp` 명령어의 기본 구문은 다음과 같습니다:

```
scp [옵션] [소스] [대상]
```

### 일반적인 옵션
- `-r`: 디렉토리를 재귀적으로 복사합니다.
- `-P`: 원격 호스트의 포트를 지정합니다. (대문자 P)
- `-i`: SSH 키 파일을 지정합니다.
- `-v`: 자세한 출력을 표시하여 디버깅에 유용합니다.

## 예제
1. 로컬 파일을 원격 서버로 복사하기:
   ```bash
   scp /path/to/local/file.txt username@remote_host:/path/to/remote/directory/
   ```
   이 명령은 로컬의 `file.txt`를 원격 서버의 지정된 디렉토리로 복사합니다.

2. 원격 서버에서 로컬로 파일 복사하기:
   ```bash
   scp username@remote_host:/path/to/remote/file.txt /path/to/local/directory/
   ```
   이 명령은 원격 서버의 `file.txt`를 로컬의 지정된 디렉토리로 복사합니다.

## 팁
- `-r` 옵션을 사용하여 전체 디렉토리를 복사할 수 있습니다. 예를 들어, `scp -r /local/directory username@remote_host:/remote/directory/`와 같이 사용할 수 있습니다.
- SSH 키를 사용하여 비밀번호 입력 없이 자동으로 인증할 수 있습니다. 이를 위해 `-i` 옵션을 사용하여 키 파일을 지정하세요.
- 대량의 파일을 전송할 때는 `-v` 옵션을 사용하여 진행 상황을 모니터링하는 것이 좋습니다.