# [리눅스] Bash alias 사용법: 명령어 단축

## Overview
`alias` 명령어는 자주 사용하는 명령어를 짧고 간단한 이름으로 정의하여, 사용자가 쉽게 호출할 수 있도록 도와줍니다. 이를 통해 명령어 입력을 간소화하고 작업 효율성을 높일 수 있습니다.

## Usage
기본 구문은 다음과 같습니다:

```bash
alias [옵션] [이름]='[명령어]'
```

## Common Options
- `-p`: 현재 정의된 모든 alias 목록을 출력합니다.

## Common Examples
다음은 `alias` 명령어의 몇 가지 일반적인 예입니다.

1. **간단한 alias 생성**:
   ```bash
   alias ll='ls -la'
   ```
   이 명령어는 `ll`을 입력하면 `ls -la` 명령어가 실행되도록 설정합니다.

2. **복잡한 명령어 alias**:
   ```bash
   alias gs='git status'
   ```
   `gs`를 입력하면 `git status`가 실행됩니다.

3. **alias 목록 확인**:
   ```bash
   alias -p
   ```
   현재 설정된 모든 alias를 출력합니다.

4. **alias 삭제**:
   ```bash
   unalias ll
   ```
   `ll` alias를 삭제합니다.

## Tips
- alias는 `.bashrc` 파일에 추가하여 터미널을 시작할 때 자동으로 로드되도록 설정할 수 있습니다.
- alias 이름은 짧고 기억하기 쉬운 것으로 설정하는 것이 좋습니다.
- 복잡한 명령어를 alias로 정의할 때는 작은따옴표(`'`)를 사용하여 공백이나 특수 문자가 포함된 경우에도 문제없이 작동하도록 합니다.