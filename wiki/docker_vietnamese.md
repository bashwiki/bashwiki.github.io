# [리눅스] Bash docker 사용법

## Tổng quan
Lệnh `docker` là một công cụ mạnh mẽ được sử dụng để phát triển, triển khai và chạy các ứng dụng trong các container. Docker cho phép các nhà phát triển đóng gói ứng dụng và tất cả các phụ thuộc của nó vào một container duy nhất, giúp việc triển khai trở nên dễ dàng và nhất quán trên nhiều môi trường khác nhau. Mục tiêu chính của Docker là giúp đơn giản hóa quy trình phát triển và triển khai ứng dụng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `docker` như sau:

```
docker [OPTIONS] COMMAND [ARG...]
```

Trong đó:
- `OPTIONS`: Các tùy chọn có thể được sử dụng để điều chỉnh hành vi của lệnh.
- `COMMAND`: Lệnh cụ thể mà bạn muốn thực hiện (ví dụ: `run`, `build`, `pull`, `push`, v.v.).
- `ARG...`: Các đối số bổ sung cho lệnh.

### Một số tùy chọn phổ biến:
- `-d`: Chạy container ở chế độ nền (detached mode).
- `--name`: Đặt tên cho container.
- `-p`: Chuyển tiếp cổng từ máy chủ đến container.
- `-v`: Gắn kết một volume vào container.

## Ví dụ
### Ví dụ 1: Chạy một container Nginx
Để chạy một container Nginx, bạn có thể sử dụng lệnh sau:

```bash
docker run -d --name my-nginx -p 8080:80 nginx
```
Lệnh này sẽ:
- Chạy một container Nginx ở chế độ nền (`-d`).
- Đặt tên cho container là `my-nginx`.
- Chuyển tiếp cổng 8080 trên máy chủ đến cổng 80 trong container.

### Ví dụ 2: Xây dựng một image từ Dockerfile
Nếu bạn có một file Dockerfile trong thư mục hiện tại, bạn có thể xây dựng một image như sau:

```bash
docker build -t my-app .
```
Lệnh này sẽ:
- Xây dựng một image với tên `my-app` từ Dockerfile trong thư mục hiện tại (`.`).

## Mẹo
- **Sử dụng Docker Compose**: Nếu bạn đang làm việc với nhiều container, hãy xem xét sử dụng Docker Compose để quản lý cấu hình và chạy nhiều container dễ dàng hơn.
- **Giảm kích thước image**: Sử dụng các image cơ bản nhỏ hơn và tối ưu hóa Dockerfile của bạn để giảm kích thước image, giúp tiết kiệm băng thông và thời gian tải.
- **Theo dõi container**: Sử dụng lệnh `docker logs [container_name]` để theo dõi log của container, giúp bạn dễ dàng phát hiện và sửa lỗi.

Hy vọng bài viết này giúp bạn hiểu rõ hơn về lệnh `docker` và cách sử dụng nó trong các dự án phát triển của mình!