# [리눅스] Bash git 사용법: 버전 관리 시스템

## Overview
Git은 소스 코드의 버전 관리를 위한 분산형 시스템입니다. 여러 개발자가 동시에 작업할 수 있도록 하며, 코드 변경 사항을 추적하고 관리하는 데 유용합니다.

## Usage
Git 명령어의 기본 구문은 다음과 같습니다.

```bash
git [options] [arguments]
```

## Common Options
- `clone`: 원격 저장소를 복제합니다.
- `commit`: 변경 사항을 저장소에 커밋합니다.
- `push`: 로컬 변경 사항을 원격 저장소에 업로드합니다.
- `pull`: 원격 저장소의 변경 사항을 로컬로 가져옵니다.
- `status`: 현재 작업 디렉토리의 상태를 확인합니다.

## Common Examples
- 원격 저장소 복제하기:
    ```bash
    git clone https://github.com/user/repo.git
    ```

- 변경 사항 커밋하기:
    ```bash
    git commit -m "커밋 메시지"
    ```

- 로컬 변경 사항을 원격 저장소에 푸시하기:
    ```bash
    git push origin main
    ```

- 원격 저장소의 변경 사항을 로컬로 가져오기:
    ```bash
    git pull origin main
    ```

- 현재 상태 확인하기:
    ```bash
    git status
    ```

## Tips
- 커밋 메시지는 간결하고 명확하게 작성하세요. 나중에 변경 내용을 이해하는 데 도움이 됩니다.
- 자주 커밋하여 작업의 진행 상황을 기록하세요. 이는 문제 발생 시 롤백을 쉽게 할 수 있게 합니다.
- 브랜치를 활용하여 기능 개발이나 버그 수정을 독립적으로 진행하세요.