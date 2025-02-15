# [리눅스] Bash env 사용법

## Tổng quan
Lệnh `env` trong Bash được sử dụng để hiển thị hoặc thiết lập biến môi trường. Biến môi trường là các giá trị được sử dụng bởi hệ thống và các chương trình để xác định các thông tin như đường dẫn, cài đặt ngôn ngữ và nhiều thông tin khác. Lệnh này rất hữu ích trong việc kiểm tra các biến môi trường hiện tại hoặc chạy một chương trình trong một môi trường cụ thể.

## Cách sử dụng
Cú pháp cơ bản của lệnh `env` như sau:

```bash
env [OPTION]... [COMMAND [ARGUMENTS]...]
```

### Tùy chọn phổ biến:
- `-i`: Khởi tạo một môi trường trống, không có biến môi trường nào được thiết lập.
- `-u NAME`: Xóa biến môi trường có tên là `NAME`.
- `VAR=value`: Thiết lập một biến môi trường mới với tên `VAR` và giá trị `value` trước khi chạy `COMMAND`.

## Ví dụ
### Ví dụ 1: Hiển thị các biến môi trường hiện tại
Để hiển thị tất cả các biến môi trường hiện tại, bạn có thể sử dụng lệnh sau:

```bash
env
```

### Ví dụ 2: Chạy một lệnh với biến môi trường tùy chỉnh
Bạn có thể thiết lập một biến môi trường tạm thời và chạy một lệnh với biến đó. Ví dụ, để thiết lập biến `MY_VAR` và chạy lệnh `printenv` để kiểm tra:

```bash
env MY_VAR=HelloWorld printenv MY_VAR
```

Kết quả sẽ là:
```
HelloWorld
```

## Mẹo
- Sử dụng `env -i` để khởi tạo một môi trường sạch sẽ khi bạn muốn chạy một lệnh mà không bị ảnh hưởng bởi các biến môi trường hiện tại.
- Khi thiết lập biến môi trường tạm thời, hãy nhớ rằng chúng chỉ tồn tại trong phạm vi của lệnh được gọi, không ảnh hưởng đến các lệnh khác trong phiên làm việc hiện tại.
- Kiểm tra các biến môi trường có thể giúp bạn xác định các vấn đề liên quan đến cấu hình môi trường trong các ứng dụng hoặc script.