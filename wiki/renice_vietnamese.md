# [리눅스] Bash renice 사용법

## Tổng quan
Lệnh `renice` trong Bash được sử dụng để thay đổi mức độ ưu tiên của một hoặc nhiều tiến trình đang chạy trên hệ thống. Mức độ ưu tiên này quyết định cách thức và tốc độ mà hệ điều hành phân bổ tài nguyên cho các tiến trình. Việc điều chỉnh mức độ ưu tiên có thể giúp cải thiện hiệu suất của các tiến trình quan trọng hoặc giảm thiểu ảnh hưởng của các tiến trình không quan trọng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `renice` như sau:

```bash
renice [n] -p [pid]
```

Trong đó:
- `[n]`: Mức độ ưu tiên mới mà bạn muốn thiết lập cho tiến trình. Giá trị có thể từ -20 (ưu tiên cao nhất) đến 19 (ưu tiên thấp nhất).
- `-p`: Tùy chọn này chỉ định rằng bạn đang thay đổi mức độ ưu tiên cho một tiến trình cụ thể, được xác định bởi `[pid]`, là ID của tiến trình.

### Tùy chọn phổ biến
- `-g [pgid]`: Thay đổi mức độ ưu tiên cho tất cả các tiến trình trong nhóm tiến trình có ID là `[pgid]`.
- `-u [user]`: Thay đổi mức độ ưu tiên cho tất cả các tiến trình của người dùng có tên là `[user]`.

## Ví dụ
### Ví dụ 1: Thay đổi mức độ ưu tiên cho một tiến trình cụ thể
Giả sử bạn có một tiến trình với ID là 1234 và bạn muốn tăng mức độ ưu tiên của nó lên 10:

```bash
renice 10 -p 1234
```

### Ví dụ 2: Thay đổi mức độ ưu tiên cho tất cả các tiến trình của một người dùng
Nếu bạn muốn giảm mức độ ưu tiên của tất cả các tiến trình của người dùng "john" xuống 5:

```bash
renice 5 -u john
```

## Mẹo
- Hãy cẩn thận khi thay đổi mức độ ưu tiên của các tiến trình quan trọng, vì việc giảm mức độ ưu tiên của chúng có thể làm chậm hiệu suất của hệ thống.
- Bạn cần quyền truy cập thích hợp để thay đổi mức độ ưu tiên của các tiến trình do người dùng khác sở hữu. Thường thì bạn sẽ cần chạy lệnh với quyền `sudo` nếu bạn muốn thay đổi mức độ ưu tiên của tiến trình không phải của bạn.
- Kiểm tra mức độ ưu tiên hiện tại của các tiến trình bằng lệnh `ps` hoặc `top` trước khi thực hiện thay đổi để có cái nhìn tổng quan về tình trạng hệ thống.