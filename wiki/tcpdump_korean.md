# [리눅스] Bash tcpdump 사용법: 네트워크 패킷 캡처

## Overview
tcpdump는 네트워크 인터페이스를 통해 흐르는 패킷을 캡처하고 분석하는 데 사용되는 강력한 명령어입니다. 이 도구는 네트워크 문제를 진단하거나 보안 분석을 수행하는 데 유용합니다.

## Usage
tcpdump의 기본 구문은 다음과 같습니다:

```bash
tcpdump [options] [arguments]
```

## Common Options
- `-i <interface>`: 패킷을 캡처할 네트워크 인터페이스를 지정합니다.
- `-n`: IP 주소와 포트 번호를 숫자로 표시하여 DNS 조회를 방지합니다.
- `-v`: 패킷에 대한 자세한 정보를 출력합니다. `-vv` 또는 `-vvv`를 사용하면 더욱 상세한 정보를 얻을 수 있습니다.
- `-c <count>`: 캡처할 패킷의 수를 지정합니다.
- `-w <file>`: 캡처한 패킷을 파일로 저장합니다.
- `-r <file>`: 저장된 패킷 파일을 읽어 분석합니다.

## Common Examples
- 특정 인터페이스에서 패킷 캡처하기:
  ```bash
  tcpdump -i eth0
  ```

- 패킷 수 제한하여 캡처하기:
  ```bash
  tcpdump -i eth0 -c 10
  ```

- 캡처한 패킷을 파일로 저장하기:
  ```bash
  tcpdump -i eth0 -w packets.pcap
  ```

- 저장된 패킷 파일 읽기:
  ```bash
  tcpdump -r packets.pcap
  ```

- DNS 조회를 방지하고 IP 주소로만 출력하기:
  ```bash
  tcpdump -i eth0 -n
  ```

## Tips
- tcpdump는 관리자 권한이 필요할 수 있으므로 `sudo`를 사용하여 실행하는 것이 좋습니다.
- 캡처할 패킷의 양이 많을 경우, 필터를 사용하여 필요한 패킷만 캡처하는 것이 효율적입니다.
- 캡처한 데이터를 분석할 때 Wireshark와 같은 GUI 도구를 활용하면 더욱 편리합니다.