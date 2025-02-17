# [리눅스] Bash curl 사용법: 웹에서 데이터를 전송하고 가져오기

## Overview
`curl` 명령은 URL을 통해 데이터를 전송하거나 가져오는 데 사용되는 강력한 도구입니다. HTTP, HTTPS, FTP 등 다양한 프로토콜을 지원하여 웹 서버와의 상호작용을 가능하게 합니다.

## Usage
기본 구문은 다음과 같습니다:
```bash
curl [options] [arguments]
```

## Common Options
- `-X, --request <command>`: 사용할 HTTP 메서드 지정 (예: GET, POST).
- `-d, --data <data>`: POST 요청 시 전송할 데이터를 지정.
- `-H, --header <header>`: 요청에 추가할 HTTP 헤더를 지정.
- `-o, --output <file>`: 응답 내용을 지정한 파일에 저장.
- `-I, --head`: 서버의 헤더 정보만 요청.

## Common Examples
- **웹 페이지 가져오기**:
  ```bash
  curl https://www.example.com
  ```
  
- **POST 요청 보내기**:
  ```bash
  curl -X POST -d "name=John&age=30" https://www.example.com/api
  ```

- **특정 헤더 추가하기**:
  ```bash
  curl -H "Authorization: Bearer token" https://www.example.com/protected
  ```

- **응답을 파일에 저장하기**:
  ```bash
  curl -o output.html https://www.example.com
  ```

- **헤더 정보만 요청하기**:
  ```bash
  curl -I https://www.example.com
  ```

## Tips
- `-v` 옵션을 사용하여 요청과 응답의 자세한 정보를 확인할 수 있습니다.
- `-L` 옵션을 추가하면 리다이렉션을 자동으로 따라갑니다.
- API와 상호작용할 때는 `-H` 옵션을 사용하여 필요한 인증 정보를 추가하는 것이 중요합니다.