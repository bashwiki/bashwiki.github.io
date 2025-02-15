# [리눅스] Bash nice 사용법

## Tổng quan
Lệnh `nice` trong Bash được sử dụng để điều chỉnh mức độ ưu tiên của một tiến trình khi nó chạy trên hệ thống. Mục đích chính của lệnh này là cho phép người dùng khởi động một tiến trình với một mức độ ưu tiên thấp hơn, giúp hệ thống có thể phân phối tài nguyên một cách hiệu quả hơn, đặc biệt trong các tình huống mà nhiều tiến trình đang chạy đồng thời.

## Cú pháp
Cú pháp cơ bản của lệnh `nice` như sau:

```bash
nice [OPTION] [COMMAND [ARGUMENTS...]]
```

### Các tùy chọn phổ biến:
- `-n, --adjustment=N`: Điều chỉnh mức độ ưu tiên của tiến trình. Giá trị `N` có thể là một số nguyên từ -20 (ưu tiên cao nhất) đến 19 (ưu tiên thấp nhất). Mặc định là 10.
- `-h, --help`: Hiển thị thông tin trợ giúp về lệnh.
- `--version`: Hiển thị phiên bản của lệnh `nice`.

## Ví dụ
### Ví dụ 1: Khởi động một tiến trình với mức độ ưu tiên thấp hơn
Giả sử bạn muốn chạy một tiến trình `my_script.sh` với mức độ ưu tiên thấp hơn:

```bash
nice -n 10 ./my_script.sh
```

### Ví dụ 2: Khởi động một tiến trình với mức độ ưu tiên cao hơn
Nếu bạn muốn khởi động một tiến trình với mức độ ưu tiên cao hơn, bạn có thể sử dụng giá trị âm:

```bash
nice -n -5 ./my_important_script.sh
```

## Mẹo
- Sử dụng `nice` khi bạn chạy các tiến trình không cần tài nguyên hệ thống cao, như sao lưu dữ liệu hoặc xử lý tệp lớn, để không làm ảnh hưởng đến các tiến trình quan trọng khác.
- Kết hợp `nice` với lệnh `renice` để thay đổi mức độ ưu tiên của một tiến trình đang chạy.
- Hãy cẩn thận khi sử dụng giá trị âm, vì điều này có thể làm giảm hiệu suất của các tiến trình khác nếu không được quản lý đúng cách.