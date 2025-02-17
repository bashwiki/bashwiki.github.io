# [리눅스] Bash traceroute 사용법: 네트워크 경로 추적

## Overview
traceroute 명령은 네트워크에서 특정 호스트까지의 경로를 추적하는 데 사용됩니다. 이 명령은 패킷이 목적지에 도달하기 위해 거치는 각 중간 라우터의 IP 주소와 응답 시간을 보여줍니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
traceroute [options] [arguments]
```

## Common Options
- `-m <max_ttl>`: 최대 TTL(Time To Live) 값을 설정합니다.
- `-n`: 호스트 이름 대신 IP 주소를 표시합니다.
- `-p <port>`: 지정한 포트 번호를 사용하여 패킷을 전송합니다.
- `-w <timeout>`: 응답 대기 시간을 설정합니다.

## Common Examples
1. 기본 traceroute 실행:
   ```bash
   traceroute example.com
   ```

2. 최대 TTL 값 설정:
   ```bash
   traceroute -m 15 example.com
   ```

3. IP 주소만 표시:
   ```bash
   traceroute -n example.com
   ```

4. 특정 포트 사용:
   ```bash
   traceroute -p 80 example.com
   ```

5. 응답 대기 시간 조정:
   ```bash
   traceroute -w 2 example.com
   ```

## Tips
- traceroute 명령은 네트워크 문제를 진단하는 데 유용합니다. 응답 시간이 긴 라우터를 확인하여 병목 현상을 찾아보세요.
- 방화벽이나 보안 설정으로 인해 traceroute가 차단될 수 있으므로, 이 점을 염두에 두고 사용하세요.
- traceroute의 결과를 분석하여 네트워크 성능을 개선할 수 있는 방법을 모색해 보세요.