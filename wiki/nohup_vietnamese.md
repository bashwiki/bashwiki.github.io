# [리눅스] Bash nohup 사용법

## Tổng quan
Lệnh `nohup` (viết tắt của "no hang up") là một công cụ trong Bash cho phép bạn chạy một lệnh hoặc một chương trình mà không bị ngắt khi bạn đăng xuất khỏi phiên làm việc. Điều này rất hữu ích cho các tác vụ dài hạn hoặc các quy trình nền mà bạn muốn tiếp tục chạy ngay cả khi bạn không còn kết nối với terminal.

## Cách sử dụng
Cú pháp cơ bản của lệnh `nohup` như sau:

```bash
nohup command [arguments] &
```

- `command`: Lệnh hoặc chương trình bạn muốn chạy.
- `[arguments]`: Các tham số tùy chọn cho lệnh.
- `&`: Chạy lệnh trong nền, cho phép bạn tiếp tục sử dụng terminal.

Một số tùy chọn phổ biến khi sử dụng `nohup` bao gồm:
- `-h`: Hiển thị trợ giúp về cách sử dụng lệnh.
- `-v`: Hiển thị thông tin chi tiết về quá trình thực hiện.

## Ví dụ
Dưới đây là một số ví dụ về cách sử dụng lệnh `nohup`.

### Ví dụ 1: Chạy một script trong nền
Giả sử bạn có một script tên là `long_process.sh` mà bạn muốn chạy mà không bị ngắt:

```bash
nohup bash long_process.sh &
```

Khi bạn chạy lệnh này, `long_process.sh` sẽ tiếp tục chạy ngay cả khi bạn đăng xuất khỏi terminal.

### Ví dụ 2: Chạy một lệnh với đầu ra được ghi vào file
Nếu bạn muốn ghi lại đầu ra của lệnh vào một file, bạn có thể làm như sau:

```bash
nohup python my_script.py > output.log 2>&1 &
```

Trong ví dụ này, đầu ra chuẩn và đầu ra lỗi sẽ được ghi vào file `output.log`.

## Mẹo
- **Kiểm tra quá trình**: Bạn có thể kiểm tra các quá trình đang chạy bằng lệnh `ps` hoặc `jobs`.
- **Ghi lại đầu ra**: Luôn ghi lại đầu ra của lệnh để dễ dàng theo dõi và xử lý lỗi sau này.
- **Sử dụng `disown`**: Nếu bạn đã chạy một lệnh mà không sử dụng `nohup`, bạn có thể sử dụng lệnh `disown` để ngắt kết nối lệnh đó với terminal.

Lệnh `nohup` là một công cụ mạnh mẽ cho các nhà phát triển và kỹ sư, giúp họ quản lý các tác vụ dài hạn mà không bị gián đoạn.