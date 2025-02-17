# [Linux] Bash fc Cách sử dụng: Quản lý và chỉnh sửa lịch sử lệnh

## Tổng quan
Lệnh `fc` trong Bash được sử dụng để truy cập và chỉnh sửa các lệnh đã thực hiện trong lịch sử. Nó cho phép người dùng xem, sửa đổi và thực thi lại các lệnh trước đó một cách dễ dàng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `fc` như sau:
```
fc [options] [arguments]
```

## Các tùy chọn phổ biến
- `-l`: Liệt kê các lệnh trong lịch sử.
- `-r`: Đảo ngược thứ tự của các lệnh khi liệt kê.
- `-s`: Thực thi lệnh mà không hiển thị nó trên màn hình.
- `-n`: Không hiển thị số thứ tự của lệnh khi liệt kê.

## Ví dụ thường gặp
1. **Liệt kê lệnh trong lịch sử**
   ```bash
   fc -l
   ```

2. **Liệt kê lệnh trong lịch sử với số thứ tự**
   ```bash
   fc -l -n
   ```

3. **Chỉnh sửa và thực thi lệnh gần nhất**
   ```bash
   fc
   ```

4. **Thực thi lệnh thứ 10 trong lịch sử**
   ```bash
   fc -s 10
   ```

5. **Liệt kê lệnh trong lịch sử theo thứ tự đảo ngược**
   ```bash
   fc -r -l
   ```

## Mẹo
- Sử dụng `fc` để nhanh chóng sửa lỗi trong các lệnh đã thực hiện mà không cần phải gõ lại toàn bộ.
- Kết hợp `fc` với các trình soạn thảo như `vim` hoặc `nano` để chỉnh sửa lệnh một cách thuận tiện hơn.
- Thường xuyên kiểm tra lịch sử lệnh của bạn để cải thiện quy trình làm việc và tiết kiệm thời gian.