# [Linux] Bash podman sử dụng: Quản lý container

## Overview
Podman là một công cụ dòng lệnh dùng để quản lý container và image container. Nó cho phép người dùng tạo, chạy và quản lý các container mà không cần một daemon chạy nền, giúp tăng cường tính bảo mật và tính linh hoạt.

## Usage
Cú pháp cơ bản của lệnh podman như sau:
```
podman [options] [arguments]
```

## Common Options
- `run`: Chạy một container mới.
- `pull`: Tải một image từ kho chứa.
- `ps`: Liệt kê các container đang chạy.
- `stop`: Dừng một container đang chạy.
- `rm`: Xóa một container đã dừng.

## Common Examples
- **Chạy một container mới từ image**:
    ```bash
    podman run -d nginx
    ```
    Lệnh này sẽ chạy một container mới từ image `nginx` trong chế độ nền.

- **Tải một image từ kho chứa**:
    ```bash
    podman pull ubuntu
    ```
    Lệnh này sẽ tải image `ubuntu` về máy.

- **Liệt kê các container đang chạy**:
    ```bash
    podman ps
    ```
    Lệnh này sẽ hiển thị danh sách các container đang hoạt động.

- **Dừng một container**:
    ```bash
    podman stop <container_id>
    ```
    Thay `<container_id>` bằng ID của container bạn muốn dừng.

- **Xóa một container đã dừng**:
    ```bash
    podman rm <container_id>
    ```
    Lệnh này sẽ xóa container đã dừng có ID tương ứng.

## Tips
- Sử dụng tùy chọn `-it` khi chạy container để có thể tương tác với nó:
    ```bash
    podman run -it ubuntu /bin/bash
    ```
- Để xem log của một container, bạn có thể sử dụng lệnh:
    ```bash
    podman logs <container_id>
    ```
- Thường xuyên kiểm tra các image và container không còn sử dụng để tiết kiệm không gian lưu trữ bằng cách sử dụng:
    ```bash
    podman image prune
    ```