# [리눅스] Bash wget 사용법: 웹에서 파일 다운로드

## Overview
`wget`은 웹에서 파일을 다운로드하는 데 사용되는 강력한 명령어입니다. HTTP, HTTPS, FTP 프로토콜을 통해 파일을 쉽게 가져올 수 있으며, 재귀 다운로드와 같은 다양한 기능을 지원합니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
wget [옵션] [인수]
```

## Common Options
- `-O [파일명]`: 다운로드한 파일의 이름을 지정합니다.
- `-r`: 재귀적으로 다운로드합니다. 웹사이트의 모든 링크를 따라가며 파일을 다운로드합니다.
- `-p`: 웹 페이지를 완전하게 다운로드합니다. 페이지에 필요한 모든 요소(이미지, 스타일시트 등)를 포함합니다.
- `-c`: 중단된 다운로드를 이어서 진행합니다.
- `--limit-rate=[속도]`: 다운로드 속도를 제한합니다.

## Common Examples
- 단일 파일 다운로드:
```bash
wget https://example.com/file.zip
```

- 파일 이름 지정하여 다운로드:
```bash
wget -O myfile.zip https://example.com/file.zip
```

- 재귀적으로 웹사이트 다운로드:
```bash
wget -r https://example.com
```

- 중단된 다운로드 이어서 진행:
```bash
wget -c https://example.com/largefile.zip
```

- 다운로드 속도 제한:
```bash
wget --limit-rate=200k https://example.com/largefile.zip
```

## Tips
- 대량의 파일을 다운로드할 때는 `-r` 옵션을 사용하여 전체 사이트를 다운로드할 수 있지만, 서버에 과부하를 주지 않도록 주의하세요.
- 다운로드 중에 문제가 발생하면 `-c` 옵션을 사용하여 다운로드를 이어서 진행할 수 있습니다.
- 다운로드 속도를 제한하는 `--limit-rate` 옵션을 활용하여 네트워크 대역폭을 관리하세요.