# [리눅스] Bash rpm 사용법: 패키지 관리 명령어

## Overview
`rpm` 명령어는 리눅스에서 패키지를 관리하는 데 사용됩니다. 이 명령어는 Red Hat 계열의 배포판에서 주로 사용되며, 소프트웨어 패키지를 설치, 제거, 업데이트 및 쿼리하는 기능을 제공합니다.

## Usage
기본 구문은 다음과 같습니다:

```
rpm [options] [arguments]
```

## Common Options
- `-i`: 패키지를 설치합니다.
- `-e`: 패키지를 제거합니다.
- `-U`: 패키지를 업데이트합니다.
- `-q`: 패키지에 대한 정보를 쿼리합니다.
- `-V`: 패키지의 무결성을 검증합니다.

## Common Examples
패키지를 설치하는 예시:
```bash
rpm -i package.rpm
```

패키지를 제거하는 예시:
```bash
rpm -e package_name
```

패키지를 업데이트하는 예시:
```bash
rpm -U package.rpm
```

패키지 정보를 쿼리하는 예시:
```bash
rpm -q package_name
```

패키지 무결성을 검증하는 예시:
```bash
rpm -V package_name
```

## Tips
- 패키지를 설치하기 전에 항상 의존성을 확인하세요.
- `-v` 옵션을 추가하여 더 많은 정보를 출력할 수 있습니다.
- 패키지 파일의 경로를 정확히 지정해야 합니다.