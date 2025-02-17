# [리눅스] Bash nslookup 사용법: 도메인 이름을 IP 주소로 변환

## Overview
`nslookup` 명령어는 도메인 이름 시스템(DNS)에서 도메인 이름을 IP 주소로 변환하거나 그 반대의 작업을 수행하는 도구입니다. 이 명령어는 네트워크 문제를 진단하거나 도메인 이름과 관련된 정보를 조회하는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:

```
nslookup [옵션] [인수]
```

## Common Options
- `-type=TYPE`: 조회할 레코드의 유형을 지정합니다. 예: A, MX, TXT 등.
- `-timeout=SEC`: 응답 대기 시간을 설정합니다.
- `-retry=NUM`: 요청 실패 시 재시도 횟수를 설정합니다.

## Common Examples
1. 기본 도메인 이름 조회:
   ```bash
   nslookup example.com
   ```

2. 특정 DNS 서버를 사용하여 조회:
   ```bash
   nslookup example.com 8.8.8.8
   ```

3. MX 레코드 조회:
   ```bash
   nslookup -type=MX example.com
   ```

4. TXT 레코드 조회:
   ```bash
   nslookup -type=TXT example.com
   ```

## Tips
- `nslookup` 명령어는 네트워크 문제를 해결하는 데 유용하므로, 자주 사용하는 DNS 서버를 지정해 두면 편리합니다.
- 결과를 해석할 때, IP 주소와 도메인 이름 간의 관계를 이해하는 것이 중요합니다.
- DNS 캐시 문제를 해결하기 위해 `nslookup`을 여러 번 실행해 보세요.