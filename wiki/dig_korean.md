# [리눅스] Bash dig 사용법: DNS 정보 조회

## Overview
`dig` 명령어는 DNS(Domain Name System) 정보를 조회하는 데 사용됩니다. 이 명령어는 도메인 이름을 IP 주소로 변환하거나, 특정 DNS 레코드를 확인하는 데 유용합니다.

## Usage
기본 구문은 다음과 같습니다:
```
dig [옵션] [인수]
```

## Common Options
- `@server`: 특정 DNS 서버를 지정하여 쿼리를 보냅니다.
- `-t type`: 조회할 DNS 레코드의 유형을 지정합니다. 예: A, AAAA, MX, TXT 등.
- `+short`: 간단한 출력 형식으로 결과를 표시합니다.
- `+trace`: DNS 쿼리의 전체 경로를 추적하여 보여줍니다.

## Common Examples
1. 기본 도메인 조회:
   ```bash
   dig example.com
   ```

2. 특정 DNS 서버에 대한 조회:
   ```bash
   dig @8.8.8.8 example.com
   ```

3. MX 레코드 조회:
   ```bash
   dig -t MX example.com
   ```

4. 간단한 출력 형식으로 A 레코드 조회:
   ```bash
   dig +short example.com
   ```

5. DNS 쿼리 경로 추적:
   ```bash
   dig +trace example.com
   ```

## Tips
- `dig` 명령어는 DNS 문제를 해결하는 데 매우 유용하므로, 네트워크 문제를 진단할 때 자주 사용하세요.
- 여러 옵션을 조합하여 더 많은 정보를 얻을 수 있습니다. 예를 들어, `dig +short -t TXT example.com`으로 TXT 레코드를 간단히 조회할 수 있습니다.
- 결과를 파일로 저장하고 싶다면, `> output.txt`를 사용하여 출력 결과를 파일로 리디렉션할 수 있습니다.