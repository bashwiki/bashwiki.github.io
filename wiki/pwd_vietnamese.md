# [리눅스] Bash pwd 사용법

## Tổng quan
Lệnh `pwd` (print working directory) trong Bash được sử dụng để hiển thị đường dẫn thư mục hiện tại mà người dùng đang làm việc. Đây là một lệnh cơ bản nhưng rất quan trọng trong môi trường dòng lệnh, giúp người dùng xác định vị trí của họ trong hệ thống tệp.

## Cách sử dụng
Cú pháp cơ bản của lệnh `pwd` rất đơn giản:

```bash
pwd [OPTION]
```

### Tùy chọn phổ biến
- `-L`: Hiển thị đường dẫn thư mục hiện tại theo cách logic, tức là nếu có liên kết tượng trưng, nó sẽ hiển thị đường dẫn mà bạn đã truy cập.
- `-P`: Hiển thị đường dẫn thư mục hiện tại theo cách vật lý, tức là nó sẽ hiển thị đường dẫn thực tế mà không có liên kết tượng trưng.

## Ví dụ
### Ví dụ 1: Hiển thị đường dẫn thư mục hiện tại
```bash
pwd
```
Khi bạn chạy lệnh này, nó sẽ trả về đường dẫn đầy đủ của thư mục mà bạn đang ở, ví dụ: `/home/user/documents`.

### Ví dụ 2: Sử dụng tùy chọn -P
```bash
pwd -P
```
Lệnh này sẽ hiển thị đường dẫn vật lý của thư mục hiện tại, giúp bạn biết chính xác vị trí mà không bị ảnh hưởng bởi các liên kết tượng trưng.

## Mẹo
- Sử dụng `pwd` thường xuyên để xác định vị trí của bạn trong hệ thống tệp, đặc biệt khi bạn làm việc với nhiều thư mục khác nhau.
- Kết hợp `pwd` với các lệnh khác như `cd` để dễ dàng điều hướng trong hệ thống tệp.
- Nếu bạn đang viết script, hãy sử dụng `pwd` để lưu trữ đường dẫn hiện tại vào biến để sử dụng sau này. Ví dụ:
  ```bash
  current_dir=$(pwd)
  echo "Thư mục hiện tại là: $current_dir"
  ``` 

Lệnh `pwd` là một công cụ hữu ích và dễ sử dụng cho bất kỳ kỹ sư hoặc nhà phát triển nào làm việc trong môi trường dòng lệnh.