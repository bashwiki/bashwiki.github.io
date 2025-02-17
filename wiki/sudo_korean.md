# [리눅스] Bash sudo 사용법: 관리자 권한으로 명령 실행

## Overview
`sudo` 명령은 사용자가 관리자 권한으로 명령을 실행할 수 있도록 해주는 도구입니다. 이 명령을 사용하면 시스템의 중요한 작업을 수행할 수 있으며, 일반 사용자 계정으로는 접근할 수 없는 파일이나 명령에 접근할 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
sudo [options] [arguments]
```

## Common Options
- `-u [user]`: 지정된 사용자로 명령을 실행합니다. 기본적으로는 root 사용자로 실행됩니다.
- `-i`: 로그인 셸을 시작하여 root 사용자로 전환합니다.
- `-s`: 현재 사용자의 환경을 유지하면서 root 사용자로 명령을 실행합니다.
- `-k`: 다음에 sudo를 사용할 때 비밀번호를 다시 입력하도록 강제합니다.

## Common Examples
1. **패키지 설치**:
   ```bash
   sudo apt-get install package-name
   ```

2. **파일 편집**:
   ```bash
   sudo nano /etc/hosts
   ```

3. **서비스 재시작**:
   ```bash
   sudo systemctl restart service-name
   ```

4. **디렉토리 권한 변경**:
   ```bash
   sudo chown user:user /path/to/directory
   ```

## Tips
- `sudo`를 사용할 때는 항상 신중해야 하며, 명령어가 시스템에 미치는 영향을 이해하고 있어야 합니다.
- 자주 사용하는 명령은 `sudo`와 함께 사용하기 전에 테스트 환경에서 확인하는 것이 좋습니다.
- `sudo`를 사용할 때 비밀번호를 입력하는 것이 번거롭다면, `visudo` 명령을 사용하여 특정 사용자에게 비밀번호 없이 sudo 권한을 부여할 수 있습니다.