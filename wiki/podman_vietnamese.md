# [리눅스] Bash podman 사용법

## Tổng quan
`podman` là một công cụ quản lý container không cần daemon, cho phép người dùng tạo, chạy và quản lý các container và pod. Nó được thiết kế để hoạt động tương tự như Docker nhưng không yêu cầu một dịch vụ nền (daemon) chạy liên tục. `podman` hỗ trợ việc chạy các container trong môi trường không có quyền root, giúp tăng cường bảo mật và dễ dàng tích hợp vào các quy trình CI/CD.

## Cách sử dụng
Cú pháp cơ bản của lệnh `podman` như sau:

```
podman [tùy chọn] [lệnh] [tham số]
```

Một số tùy chọn và lệnh phổ biến của `podman` bao gồm:

- `podman run`: Tạo và chạy một container mới.
- `podman ps`: Liệt kê các container đang chạy.
- `podman images`: Hiển thị danh sách các hình ảnh container có sẵn.
- `podman stop`: Dừng một hoặc nhiều container đang chạy.
- `podman rm`: Xóa một hoặc nhiều container.

## Ví dụ
### Ví dụ 1: Chạy một container Nginx
Để chạy một container Nginx, bạn có thể sử dụng lệnh sau:

```bash
podman run -d -p 8080:80 nginx
```

Trong lệnh này:
- `-d`: Chạy container ở chế độ nền (detached).
- `-p 8080:80`: Chuyển tiếp cổng 8080 trên máy chủ đến cổng 80 trong container.

### Ví dụ 2: Liệt kê các container đang chạy
Để xem danh sách các container đang chạy, bạn có thể sử dụng lệnh:

```bash
podman ps
```

Lệnh này sẽ hiển thị thông tin về các container đang hoạt động, bao gồm ID, tên, trạng thái và cổng.

## Mẹo
- Sử dụng `podman --help` để xem danh sách đầy đủ các lệnh và tùy chọn có sẵn.
- Để tiết kiệm tài nguyên, hãy dọn dẹp các container và hình ảnh không còn sử dụng bằng cách sử dụng `podman rm` và `podman rmi`.
- Xem xét việc sử dụng `podman-compose` nếu bạn cần quản lý nhiều container cùng một lúc, tương tự như Docker Compose.

Hy vọng rằng bài viết này sẽ giúp bạn hiểu rõ hơn về cách sử dụng `podman` trong các dự án phát triển của mình!