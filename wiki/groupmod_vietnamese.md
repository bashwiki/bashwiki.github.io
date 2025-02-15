# [리눅스] Bash groupmod 사용법

## Tổng quan
Lệnh `groupmod` trong Bash được sử dụng để thay đổi các thuộc tính của một nhóm người dùng đã tồn tại trong hệ thống Linux. Lệnh này cho phép người quản trị hệ thống điều chỉnh tên nhóm, GID (Group ID), và các thuộc tính khác của nhóm mà không cần phải xóa và tạo lại nhóm đó.

## Cách sử dụng
Cú pháp cơ bản của lệnh `groupmod` như sau:

```bash
groupmod [tùy chọn] tên_nhóm
```

### Các tùy chọn phổ biến:
- `-n, --new-name tên_mới`: Thay đổi tên của nhóm thành tên mới.
- `-g, --gid GID_mới`: Thay đổi GID của nhóm thành GID mới.

## Ví dụ
### Ví dụ 1: Thay đổi tên nhóm
Giả sử bạn có một nhóm tên là `developers` và bạn muốn thay đổi tên nhóm này thành `dev_team`. Bạn có thể sử dụng lệnh sau:

```bash
groupmod -n dev_team developers
```

### Ví dụ 2: Thay đổi GID của nhóm
Nếu bạn muốn thay đổi GID của nhóm `dev_team` thành `1050`, bạn có thể thực hiện như sau:

```bash
groupmod -g 1050 dev_team
```

## Mẹo
- Trước khi thực hiện thay đổi, hãy đảm bảo rằng không có người dùng nào đang sử dụng nhóm mà bạn muốn thay đổi, để tránh gây ra sự cố cho người dùng.
- Kiểm tra các nhóm hiện có và GID bằng lệnh `cat /etc/group` để đảm bảo rằng GID mới bạn chọn không bị trùng lặp với bất kỳ nhóm nào khác.
- Sử dụng quyền root hoặc sudo để thực hiện lệnh `groupmod`, vì chỉ có người quản trị mới có quyền thay đổi cấu hình nhóm.