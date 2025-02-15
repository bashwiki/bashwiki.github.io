# [리눅스] Bash mapfile 사용법

## Tổng quan
Lệnh `mapfile` trong Bash được sử dụng để đọc các dòng từ một tệp tin và lưu chúng vào một mảng. Lệnh này rất hữu ích khi bạn cần xử lý dữ liệu từ tệp mà không cần phải lặp qua từng dòng bằng cách sử dụng các vòng lặp truyền thống. `mapfile` giúp bạn dễ dàng quản lý và thao tác với dữ liệu.

## Cách sử dụng
Cú pháp cơ bản của lệnh `mapfile` như sau:

```bash
mapfile [options] array_name < input_file
```

Trong đó:
- `array_name`: Tên của mảng mà bạn muốn lưu trữ các dòng từ tệp.
- `input_file`: Tệp tin chứa dữ liệu mà bạn muốn đọc vào mảng.

### Các tùy chọn phổ biến
- `-t`: Xóa ký tự xuống dòng ở cuối mỗi dòng khi lưu vào mảng.
- `-n count`: Đọc tối đa `count` dòng từ tệp.
- `-O index`: Bắt đầu lưu vào mảng từ chỉ số `index`.

## Ví dụ
### Ví dụ 1: Đọc toàn bộ tệp vào mảng
```bash
mapfile lines < myfile.txt
echo "${lines[@]}"
```
Trong ví dụ này, tất cả các dòng trong `myfile.txt` sẽ được lưu vào mảng `lines` và sau đó được in ra.

### Ví dụ 2: Đọc một số dòng nhất định
```bash
mapfile -t -n 5 lines < myfile.txt
echo "${lines[@]}"
```
Ở đây, chỉ 5 dòng đầu tiên từ `myfile.txt` sẽ được đọc và lưu vào mảng `lines`, và sau đó in ra.

## Mẹo
- Sử dụng tùy chọn `-t` để loại bỏ ký tự xuống dòng, giúp bạn dễ dàng xử lý dữ liệu mà không cần phải xử lý các ký tự không cần thiết.
- Khi làm việc với các tệp lớn, hãy cân nhắc sử dụng tùy chọn `-n` để giới hạn số dòng đọc vào mảng, giúp tiết kiệm bộ nhớ.
- Kiểm tra kích thước của mảng sau khi sử dụng `mapfile` bằng cách sử dụng `${#array_name[@]}` để đảm bảo rằng bạn đã đọc đúng số dòng mong muốn.

Hy vọng bài viết này sẽ giúp bạn hiểu rõ hơn về cách sử dụng lệnh `mapfile` trong Bash!