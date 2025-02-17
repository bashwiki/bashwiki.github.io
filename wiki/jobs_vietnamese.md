# [Linux] Bash jobs sử dụng: Quản lý các tiến trình nền

## Overview
Lệnh `jobs` trong Bash được sử dụng để hiển thị danh sách các tiến trình nền mà người dùng đã khởi động trong phiên làm việc hiện tại. Nó giúp bạn theo dõi và quản lý các tiến trình này một cách dễ dàng.

## Usage
Cú pháp cơ bản của lệnh `jobs` như sau:
```
jobs [options] [arguments]
```

## Common Options
- `-l`: Hiển thị PID (Process ID) của các tiến trình.
- `-n`: Chỉ hiển thị các tiến trình đã thay đổi trạng thái kể từ lần gọi lệnh trước.
- `-p`: Chỉ hiển thị PID của các tiến trình.

## Common Examples
- Hiển thị tất cả các tiến trình nền:
  ```bash
  jobs
  ```

- Hiển thị các tiến trình nền với PID:
  ```bash
  jobs -l
  ```

- Hiển thị các tiến trình nền đã thay đổi trạng thái:
  ```bash
  jobs -n
  ```

- Hiển thị chỉ PID của các tiến trình:
  ```bash
  jobs -p
  ```

## Tips
- Sử dụng lệnh `bg` để tiếp tục một tiến trình nền đã bị tạm dừng.
- Sử dụng lệnh `fg` để đưa một tiến trình nền về foreground (tiến trình chính).
- Kiểm tra thường xuyên danh sách các tiến trình nền để quản lý tài nguyên hệ thống hiệu quả hơn.