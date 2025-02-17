# [Linux] Bash paste cách sử dụng: Nối các dòng từ nhiều tệp

## Tổng quan
Lệnh `paste` trong Bash được sử dụng để nối các dòng từ nhiều tệp lại với nhau. Nó cho phép bạn kết hợp nội dung của các tệp theo chiều ngang, tạo ra một tệp mới với các dòng được phân tách.

## Cách sử dụng
Cú pháp cơ bản của lệnh `paste` như sau:
```bash
paste [options] [arguments]
```

## Các tùy chọn phổ biến
- `-d` : Chỉ định ký tự phân tách giữa các cột (mặc định là tab).
- `-s` : Nối các dòng theo chiều dọc thay vì chiều ngang.
- `-z` : Xử lý các tệp như là một dòng duy nhất, phân tách bằng ký tự null.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `paste`:

1. Nối hai tệp với nhau:
```bash
paste file1.txt file2.txt
```

2. Sử dụng ký tự phân tách khác (ví dụ: dấu phẩy):
```bash
paste -d ',' file1.txt file2.txt
```

3. Nối các dòng theo chiều dọc:
```bash
paste -s file1.txt
```

4. Nối nhiều tệp và sử dụng ký tự phân tách là dấu chấm phẩy:
```bash
paste -d ';' file1.txt file2.txt file3.txt
```

## Mẹo
- Hãy chắc chắn rằng các tệp bạn muốn nối có cùng số lượng dòng để tránh kết quả không mong muốn.
- Sử dụng tùy chọn `-d` để tùy chỉnh ký tự phân tách, giúp dữ liệu dễ đọc hơn.
- Khi làm việc với nhiều tệp, hãy kiểm tra xem các tệp có tồn tại trước khi sử dụng lệnh để tránh lỗi.