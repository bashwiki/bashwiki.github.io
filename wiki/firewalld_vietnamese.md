# [리눅스] Bash firewalld 사용법

## Tổng quan
`firewalld` là một công cụ quản lý tường lửa trên hệ điều hành Linux, cho phép người dùng cấu hình và quản lý các quy tắc tường lửa một cách dễ dàng và linh hoạt. Nó cung cấp một giao diện để kiểm soát lưu lượng mạng vào và ra, giúp bảo vệ hệ thống khỏi các mối đe dọa từ bên ngoài. `firewalld` sử dụng các khu vực (zones) để xác định mức độ bảo mật cho các kết nối mạng khác nhau.

## Cách sử dụng
Cú pháp cơ bản của lệnh `firewalld` như sau:

```bash
firewall-cmd [OPTIONS]
```

Một số tùy chọn phổ biến của `firewalld` bao gồm:

- `--state`: Kiểm tra trạng thái hiện tại của `firewalld`.
- `--zone`: Chỉ định khu vực mà bạn muốn cấu hình.
- `--add-service`: Thêm một dịch vụ vào khu vực.
- `--remove-service`: Xóa một dịch vụ khỏi khu vực.
- `--list-all`: Liệt kê tất cả các quy tắc và dịch vụ trong khu vực hiện tại.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `firewalld`:

1. **Kiểm tra trạng thái của firewalld**:
   ```bash
   firewall-cmd --state
   ```
   Lệnh này sẽ trả về trạng thái hiện tại của `firewalld`, cho biết nó đang chạy hay không.

2. **Thêm dịch vụ HTTP vào khu vực public**:
   ```bash
   firewall-cmd --zone=public --add-service=http --permanent
   ```
   Lệnh này sẽ thêm dịch vụ HTTP vào khu vực public và lưu lại thay đổi. Để áp dụng thay đổi, bạn cần khởi động lại `firewalld` bằng lệnh:
   ```bash
   firewall-cmd --reload
   ```

## Mẹo
- **Sử dụng khu vực**: Hãy tận dụng các khu vực để phân loại các kết nối mạng khác nhau. Điều này giúp bạn dễ dàng quản lý và kiểm soát lưu lượng mạng.
- **Kiểm tra cấu hình**: Sau khi thực hiện thay đổi, hãy sử dụng `--list-all` để kiểm tra lại cấu hình tường lửa và đảm bảo rằng các quy tắc đã được áp dụng đúng cách.
- **Sao lưu cấu hình**: Trước khi thực hiện các thay đổi lớn, hãy sao lưu cấu hình hiện tại của `firewalld` để có thể khôi phục lại nếu cần thiết.

Với những thông tin trên, bạn đã có cái nhìn tổng quan về cách sử dụng lệnh `firewalld` trong Bash. Hãy áp dụng các kiến thức này để bảo vệ hệ thống của bạn một cách hiệu quả!