# [리눅스] Bash scp 사용법: 원격 파일 전송

## Overview
`scp` (Secure Copy Protocol) 명령은 네트워크를 통해 파일이나 디렉토리를 안전하게 복사하는 데 사용됩니다. SSH(Secure Shell) 프로토콜을 기반으로 하여 데이터 전송 중 보안을 제공합니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
scp [options] [source] [destination]
```

## Common Options
- `-r`: 디렉토리를 재귀적으로 복사합니다.
- `-P`: 원격 호스트의 포트를 지정합니다. (대문자 P)
- `-p`: 파일의 수정 시간, 접근 시간 및 모드를 유지합니다.
- `-q`: 진행 상태를 표시하지 않습니다.
- `-C`: 전송 중 데이터를 압축합니다.

## Common Examples
- **로컬에서 원격 서버로 파일 복사**
```bash
scp localfile.txt username@remotehost:/path/to/destination/
```

- **원격 서버에서 로컬로 파일 복사**
```bash
scp username@remotehost:/path/to/remotefile.txt /local/destination/
```

- **디렉토리 전체를 원격 서버로 복사**
```bash
scp -r /local/directory username@remotehost:/path/to/destination/
```

- **특정 포트를 사용하여 파일 복사**
```bash
scp -P 2222 localfile.txt username@remotehost:/path/to/destination/
```

## Tips
- 비밀번호 입력을 자동화하려면 SSH 키를 설정하는 것이 좋습니다.
- 대량의 파일을 전송할 때는 `-C` 옵션을 사용하여 전송 속도를 높일 수 있습니다.
- `-v` 옵션을 사용하여 디버깅 정보를 출력받아 문제를 해결할 수 있습니다.