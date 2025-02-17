# [Linux] Bash firewalld Cách sử dụng: Quản lý tường lửa

## Tổng quan
Lệnh `firewalld` là một công cụ quản lý tường lửa trên các hệ thống Linux, cho phép người dùng cấu hình và quản lý các quy tắc tường lửa một cách dễ dàng và linh hoạt. Nó hỗ trợ việc quản lý các vùng (zones) và dịch vụ, giúp bảo vệ hệ thống khỏi các mối đe dọa từ mạng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `firewalld` như sau:

```
firewalld [options] [arguments]
```

## Các tùy chọn phổ biến
- `--zone`: Chỉ định vùng mà quy tắc sẽ áp dụng.
- `--add-service`: Thêm một dịch vụ vào vùng.
- `--remove-service`: Xóa một dịch vụ khỏi vùng.
- `--list-all`: Liệt kê tất cả các quy tắc và dịch vụ trong một vùng cụ thể.
- `--reload`: Tải lại cấu hình tường lửa.

## Ví dụ thường gặp
1. **Thêm dịch vụ HTTP vào vùng công cộng:**
   ```bash
   firewall-cmd --zone=public --add-service=http
   ```

2. **Xóa dịch vụ FTP khỏi vùng nội bộ:**
   ```bash
   firewall-cmd --zone=internal --remove-service=ftp
   ```

3. **Liệt kê tất cả các quy tắc trong vùng công cộng:**
   ```bash
   firewall-cmd --zone=public --list-all
   ```

4. **Tải lại cấu hình tường lửa:**
   ```bash
   firewall-cmd --reload
   ```

## Mẹo
- Luôn kiểm tra cấu hình tường lửa sau khi thực hiện thay đổi bằng cách sử dụng `--list-all` để đảm bảo rằng các quy tắc đã được áp dụng chính xác.
- Sử dụng `--permanent` để áp dụng các thay đổi vĩnh viễn, nếu không, các thay đổi sẽ chỉ có hiệu lực cho phiên làm việc hiện tại.
- Để tránh mất kết nối, hãy cẩn thận khi thay đổi các quy tắc liên quan đến SSH, đặc biệt là khi làm việc trên máy chủ từ xa.