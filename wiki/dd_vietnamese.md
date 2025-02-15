# [리눅스] Bash dd 사용법

## Tổng quan
Lệnh `dd` trong Bash là một công cụ mạnh mẽ được sử dụng để sao chép và chuyển đổi dữ liệu. Nó thường được sử dụng để tạo bản sao của các thiết bị lưu trữ, tạo hình ảnh đĩa, hoặc chuyển đổi định dạng dữ liệu. `dd` cho phép người dùng thao tác trực tiếp với các byte và khối dữ liệu, điều này làm cho nó trở thành một công cụ hữu ích trong nhiều tình huống liên quan đến quản lý dữ liệu.

## Cách sử dụng
Cú pháp cơ bản của lệnh `dd` như sau:

```bash
dd if=<input_file> of=<output_file> [options]
```

Trong đó:
- `if=<input_file>`: Chỉ định tệp đầu vào (input file) hoặc thiết bị mà bạn muốn sao chép dữ liệu từ đó.
- `of=<output_file>`: Chỉ định tệp đầu ra (output file) hoặc thiết bị mà bạn muốn sao chép dữ liệu đến đó.

Một số tùy chọn phổ biến:
- `bs=<size>`: Chỉ định kích thước khối (block size) cho quá trình sao chép. Kích thước mặc định là 512 byte.
- `count=<number>`: Chỉ định số lượng khối sẽ được sao chép từ tệp đầu vào.
- `status=<level>`: Chỉ định mức độ thông tin hiển thị trong quá trình thực hiện. Các giá trị có thể là `none`, `noxfer`, hoặc `progress`.

## Ví dụ
### Ví dụ 1: Tạo bản sao của một ổ đĩa
Để tạo một bản sao của ổ đĩa `/dev/sda` và lưu vào tệp `backup.img`, bạn có thể sử dụng lệnh sau:

```bash
dd if=/dev/sda of=backup.img bs=4M status=progress
```

### Ví dụ 2: Khôi phục một hình ảnh đĩa vào ổ đĩa
Để khôi phục một hình ảnh đĩa từ tệp `backup.img` vào ổ đĩa `/dev/sdb`, bạn có thể sử dụng lệnh sau:

```bash
dd if=backup.img of=/dev/sdb bs=4M status=progress
```

## Mẹo
- **Sử dụng `status=progress`**: Tùy chọn này giúp bạn theo dõi tiến trình của lệnh `dd`, rất hữu ích khi sao chép các tệp lớn.
- **Cẩn thận với thiết bị đầu ra**: Khi sử dụng `dd`, hãy chắc chắn rằng bạn đã chỉ định đúng thiết bị đầu ra. Việc ghi đè lên một thiết bị không đúng có thể dẫn đến mất dữ liệu.
- **Kiểm tra dữ liệu**: Sau khi sao chép, bạn có thể sử dụng lệnh `md5sum` hoặc `sha256sum` để kiểm tra tính toàn vẹn của dữ liệu giữa tệp đầu vào và đầu ra.

Lệnh `dd` là một công cụ mạnh mẽ nhưng cũng có thể gây ra rủi ro nếu không được sử dụng cẩn thận. Hãy luôn đảm bảo rằng bạn đã sao lưu dữ liệu quan trọng trước khi thực hiện các thao tác với `dd`.