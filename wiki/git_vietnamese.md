# [Linux] Bash git cách sử dụng: Quản lý mã nguồn

## Tổng quan
Lệnh git là một hệ thống quản lý phiên bản phân tán, cho phép người dùng theo dõi và quản lý các thay đổi trong mã nguồn. Git rất phổ biến trong phát triển phần mềm, giúp nhiều lập trình viên làm việc cùng nhau một cách hiệu quả.

## Cách sử dụng
Cú pháp cơ bản của lệnh git như sau:
```
git [tùy chọn] [tham số]
```

## Các tùy chọn phổ biến
- `clone`: Sao chép một kho lưu trữ từ xa về máy tính cục bộ.
- `add`: Thêm tệp vào khu vực tạm thời để chuẩn bị cho việc commit.
- `commit`: Lưu lại các thay đổi đã được thêm vào khu vực tạm thời.
- `push`: Đẩy các thay đổi từ kho lưu trữ cục bộ lên kho lưu trữ từ xa.
- `pull`: Tải về và hợp nhất các thay đổi từ kho lưu trữ từ xa.

## Ví dụ thường gặp
- **Sao chép kho lưu trữ từ xa:**
  ```bash
  git clone https://github.com/username/repo.git
  ```
  
- **Thêm tệp vào khu vực tạm thời:**
  ```bash
  git add filename.txt
  ```

- **Lưu lại các thay đổi:**
  ```bash
  git commit -m "Thông điệp commit"
  ```

- **Đẩy thay đổi lên kho lưu trữ từ xa:**
  ```bash
  git push origin main
  ```

- **Tải về và hợp nhất thay đổi từ kho lưu trữ từ xa:**
  ```bash
  git pull origin main
  ```

## Mẹo
- Luôn viết thông điệp commit rõ ràng và súc tích để dễ dàng theo dõi lịch sử thay đổi.
- Sử dụng nhánh (branch) để phát triển các tính năng mới mà không làm ảnh hưởng đến mã nguồn chính.
- Thường xuyên đẩy (push) các thay đổi lên kho lưu trữ từ xa để tránh mất mát dữ liệu.