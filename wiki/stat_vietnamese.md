# [리눅스] Bash stat 사용법

## Tổng Quan
Lệnh `stat` trong Bash được sử dụng để hiển thị thông tin chi tiết về các tệp tin và thư mục trong hệ thống tệp. Nó cung cấp các thông tin như kích thước tệp, thời gian sửa đổi, quyền truy cập, và nhiều thông tin khác liên quan đến tệp. Mục đích chính của lệnh này là giúp người dùng hiểu rõ hơn về các thuộc tính của tệp và thư mục.

## Cách Sử Dụng
Cú pháp cơ bản của lệnh `stat` như sau:

```bash
stat [tùy chọn] [tệp]
```

### Các Tùy Chọn Thông Dụng
- `-c, --format=FORMAT`: Cho phép người dùng chỉ định định dạng đầu ra. Bạn có thể sử dụng các ký tự đặc biệt để tùy chỉnh thông tin hiển thị.
- `-f, --file-system`: Hiển thị thông tin về hệ thống tệp chứa tệp được chỉ định.
- `--help`: Hiển thị thông tin trợ giúp về lệnh `stat`.
- `--version`: Hiển thị phiên bản của lệnh `stat`.

## Ví Dụ
### Ví Dụ 1: Hiển Thị Thông Tin Cơ Bản
Để hiển thị thông tin cơ bản về một tệp tin, bạn có thể sử dụng lệnh sau:

```bash
stat myfile.txt
```

Kết quả sẽ hiển thị các thông tin như kích thước, thời gian sửa đổi, quyền truy cập, và nhiều thông tin khác về `myfile.txt`.

### Ví Dụ 2: Tùy Chỉnh Định Dạng Đầu Ra
Nếu bạn muốn chỉ hiển thị kích thước và thời gian sửa đổi của tệp, bạn có thể sử dụng tùy chọn `-c` như sau:

```bash
stat -c "Kích thước: %s bytes, Thời gian sửa đổi: %y" myfile.txt
```

Kết quả sẽ chỉ hiển thị kích thước và thời gian sửa đổi của tệp `myfile.txt` theo định dạng mà bạn đã chỉ định.

## Mẹo
- Sử dụng tùy chọn `-f` để kiểm tra thông tin về hệ thống tệp nếu bạn cần biết thông tin về hệ thống tệp mà tệp thuộc về.
- Thử nghiệm với các định dạng khác nhau khi sử dụng tùy chọn `-c` để tìm ra định dạng đầu ra phù hợp nhất với nhu cầu của bạn.
- Kết hợp lệnh `stat` với các lệnh khác trong Bash để tạo ra các kịch bản tự động hóa mạnh mẽ hơn, ví dụ như kiểm tra kích thước tệp trước khi thực hiện các thao tác sao lưu.