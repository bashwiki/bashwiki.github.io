# [Linux] Bash docker cách sử dụng: Quản lý container và hình ảnh

## Tổng quan
Lệnh `docker` là một công cụ mạnh mẽ cho phép người dùng quản lý các container và hình ảnh Docker. Nó giúp triển khai, chạy và quản lý các ứng dụng trong môi trường ảo hóa, giúp tiết kiệm tài nguyên và dễ dàng hơn trong việc phát triển và triển khai ứng dụng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `docker` như sau:
```bash
docker [options] [arguments]
```

## Các tùy chọn phổ biến
- `docker run`: Tạo và chạy một container mới.
- `docker ps`: Liệt kê các container đang chạy.
- `docker images`: Hiển thị danh sách các hình ảnh Docker có sẵn trên máy.
- `docker pull`: Tải một hình ảnh từ Docker Hub.
- `docker rm`: Xóa một hoặc nhiều container.
- `docker rmi`: Xóa một hoặc nhiều hình ảnh.

## Ví dụ thường gặp
- Tạo và chạy một container từ hình ảnh Ubuntu:
  ```bash
  docker run -it ubuntu
  ```
  
- Liệt kê các container đang chạy:
  ```bash
  docker ps
  ```
  
- Tải hình ảnh nginx từ Docker Hub:
  ```bash
  docker pull nginx
  ```
  
- Xóa một container với ID cụ thể:
  ```bash
  docker rm <container_id>
  ```
  
- Xóa một hình ảnh với tên cụ thể:
  ```bash
  docker rmi <image_name>
  ```

## Mẹo
- Luôn kiểm tra các container và hình ảnh hiện có trước khi tạo mới để tránh lãng phí tài nguyên.
- Sử dụng `docker-compose` cho các ứng dụng phức tạp với nhiều container để quản lý dễ dàng hơn.
- Thường xuyên cập nhật hình ảnh Docker để đảm bảo bạn đang sử dụng phiên bản mới nhất và an toàn nhất.