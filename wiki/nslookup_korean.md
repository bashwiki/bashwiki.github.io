# [리눅스] Bash nslookup 사용법

## Overview
`nslookup`은 도메인 이름 시스템(DNS)에서 도메인 이름을 IP 주소로 변환하거나 그 반대의 작업을 수행하는 명령어입니다. 이 명령어는 네트워크 문제를 진단하거나 DNS 레코드를 조회할 때 유용하게 사용됩니다. `nslookup`은 DNS 서버와 직접 통신하여 정보를 요청하고 응답을 반환합니다.

## Usage
`nslookup`의 기본 구문은 다음과 같습니다:

```bash
nslookup [옵션] [도메인 이름 | IP 주소]
```

### 일반적인 옵션
- `-type=TYPE`: 조회할 DNS 레코드의 유형을 지정합니다. 예를 들어, `A`, `MX`, `CNAME` 등의 레코드 유형을 사용할 수 있습니다.
- `-debug`: 디버그 모드를 활성화하여 더 많은 정보를 출력합니다.
- `-timeout=초`: 응답을 기다리는 최대 시간을 설정합니다.

## Examples
### 예제 1: 도메인 이름으로 IP 주소 조회
```bash
nslookup www.example.com
```
위 명령어는 `www.example.com`의 IP 주소를 조회합니다. 결과로 해당 도메인에 대한 IP 주소와 관련된 DNS 서버 정보를 출력합니다.

### 예제 2: 특정 DNS 서버 사용
```bash
nslookup www.example.com 8.8.8.8
```
이 명령어는 Google의 공개 DNS 서버(8.8.8.8)를 사용하여 `www.example.com`의 IP 주소를 조회합니다.

## Tips
- `nslookup`은 대화형 모드에서도 사용할 수 있습니다. 단순히 `nslookup`을 입력하면 프롬프트가 나타나고, 그 후에 도메인 이름을 입력하여 여러 조회를 수행할 수 있습니다.
- DNS 레코드의 문제를 진단할 때는 `-debug` 옵션을 사용하여 더 많은 정보를 확인하는 것이 좋습니다.
- `nslookup`은 기본적으로 시스템의 DNS 설정을 따르지만, 특정 DNS 서버를 지정하여 조회할 수 있으므로, 다양한 DNS 서버의 응답을 비교할 수 있습니다.