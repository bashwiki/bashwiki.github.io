# [리눅스] Bash ufw 사용법

## Tổng quan
`ufw` (Uncomplicated Firewall) là một công cụ dòng lệnh được thiết kế để đơn giản hóa việc quản lý tường lửa trên hệ điều hành Linux. Mục đích chính của `ufw` là cung cấp một giao diện dễ sử dụng cho việc cấu hình tường lửa iptables, giúp người dùng có thể dễ dàng cho phép hoặc từ chối lưu lượng mạng đến và đi từ hệ thống của họ.

## Cách sử dụng
Cú pháp cơ bản của lệnh `ufw` như sau:

```
ufw [các tùy chọn] [các tham số]
```

Một số tùy chọn phổ biến bao gồm:
- `enable`: Bật tường lửa.
- `disable`: Tắt tường lửa.
- `allow`: Cho phép lưu lượng mạng cho một dịch vụ hoặc cổng cụ thể.
- `deny`: Từ chối lưu lượng mạng cho một dịch vụ hoặc cổng cụ thể.
- `status`: Hiển thị trạng thái hiện tại của tường lửa.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `ufw`:

1. **Bật tường lửa**:
   ```bash
   sudo ufw enable
   ```
   Lệnh này sẽ bật tường lửa và bắt đầu áp dụng các quy tắc đã được cấu hình.

2. **Cho phép lưu lượng HTTP**:
   ```bash
   sudo ufw allow http
   ```
   Lệnh này sẽ cho phép lưu lượng đến cổng 80 (HTTP), cho phép người dùng truy cập vào các dịch vụ web.

## Mẹo
- **Kiểm tra trạng thái**: Trước và sau khi thay đổi cấu hình tường lửa, hãy sử dụng lệnh `ufw status` để kiểm tra trạng thái và đảm bảo rằng các quy tắc đã được áp dụng đúng cách.
- **Sao lưu cấu hình**: Trước khi thực hiện các thay đổi lớn, hãy sao lưu cấu hình hiện tại của tường lửa để có thể khôi phục nếu cần thiết.
- **Sử dụng các dịch vụ cụ thể**: Thay vì chỉ định cổng, bạn có thể sử dụng tên dịch vụ (như `http`, `ssh`, v.v.) để dễ quản lý hơn.

Hy vọng bài viết này sẽ giúp bạn hiểu rõ hơn về cách sử dụng `ufw` để quản lý tường lửa trên hệ thống Linux của mình!