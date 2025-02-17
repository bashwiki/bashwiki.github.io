# [Linux] Bash virsh: Quản lý máy ảo

## Overview
Lệnh `virsh` là một công cụ dòng lệnh được sử dụng để quản lý các máy ảo trên hệ thống ảo hóa sử dụng libvirt. Nó cho phép người dùng thực hiện các thao tác như khởi động, dừng, và quản lý các máy ảo một cách hiệu quả.

## Usage
Cú pháp cơ bản của lệnh `virsh` như sau:
```
virsh [options] [arguments]
```

## Common Options
- `list`: Hiển thị danh sách các máy ảo đang chạy.
- `start <name>`: Khởi động một máy ảo với tên được chỉ định.
- `shutdown <name>`: Tắt một máy ảo với tên được chỉ định.
- `destroy <name>`: Dừng vĩnh viễn một máy ảo.
- `create <file>`: Tạo một máy ảo mới từ tệp cấu hình XML.
- `edit <name>`: Chỉnh sửa cấu hình của một máy ảo.

## Common Examples
- Hiển thị danh sách các máy ảo đang chạy:
  ```bash
  virsh list
  ```

- Khởi động một máy ảo có tên là "myvm":
  ```bash
  virsh start myvm
  ```

- Tắt một máy ảo có tên là "myvm":
  ```bash
  virsh shutdown myvm
  ```

- Dừng vĩnh viễn một máy ảo có tên là "myvm":
  ```bash
  virsh destroy myvm
  ```

- Tạo một máy ảo mới từ tệp cấu hình XML có tên là "myvm.xml":
  ```bash
  virsh create myvm.xml
  ```

- Chỉnh sửa cấu hình của một máy ảo có tên là "myvm":
  ```bash
  virsh edit myvm
  ```

## Tips
- Luôn kiểm tra trạng thái của máy ảo trước khi thực hiện các thao tác để tránh mất dữ liệu.
- Sử dụng `virsh help` để xem danh sách đầy đủ các lệnh và tùy chọn có sẵn.
- Thực hiện sao lưu cấu hình máy ảo trước khi chỉnh sửa để có thể phục hồi nếu cần thiết.