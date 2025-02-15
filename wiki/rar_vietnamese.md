# [리눅스] Bash rar 사용법

## Tổng quan
Lệnh `rar` là một công cụ dòng lệnh được sử dụng để nén và giải nén các tệp tin trong định dạng RAR. Được phát triển bởi Eugene Roshal, RAR là một trong những định dạng nén phổ biến, cho phép nén tệp tin hiệu quả và hỗ trợ nhiều tính năng như mã hóa và phân chia tệp tin. Lệnh `rar` thường được sử dụng trong các môi trường Unix/Linux để quản lý các tệp tin nén.

## Cách sử dụng
Cú pháp cơ bản của lệnh `rar` như sau:

```
rar [tùy chọn] [lệnh] [tệp tin]
```

### Các tùy chọn phổ biến:
- `a`: Thêm tệp tin vào một tệp RAR.
- `x`: Giải nén tệp tin từ một tệp RAR.
- `v`: Hiển thị thông tin chi tiết về quá trình nén hoặc giải nén.
- `m`: Chỉ định mức độ nén (0-5), với 0 là không nén và 5 là nén tối đa.
- `p`: Thiết lập mật khẩu cho tệp RAR.

## Ví dụ
### Ví dụ 1: Nén tệp tin
Để nén một tệp tin có tên `file.txt` thành tệp RAR có tên `archive.rar`, bạn có thể sử dụng lệnh sau:

```bash
rar a archive.rar file.txt
```

### Ví dụ 2: Giải nén tệp RAR
Để giải nén tệp `archive.rar` vào thư mục hiện tại, bạn có thể sử dụng lệnh sau:

```bash
rar x archive.rar
```

## Mẹo
- Khi nén nhiều tệp tin, bạn có thể sử dụng ký tự đại diện (wildcard) để chọn nhiều tệp tin cùng lúc. Ví dụ: `rar a archive.rar *.txt` sẽ nén tất cả các tệp tin có đuôi `.txt` trong thư mục hiện tại.
- Để tăng cường bảo mật, hãy sử dụng tùy chọn `p` để thiết lập mật khẩu cho tệp RAR của bạn, ví dụ: `rar a -pYourPassword archive.rar file.txt`.
- Hãy kiểm tra tệp RAR sau khi nén bằng cách sử dụng tùy chọn `t` để đảm bảo rằng tệp đã được nén đúng cách: `rar t archive.rar`.

Sử dụng lệnh `rar` một cách hiệu quả sẽ giúp bạn quản lý các tệp tin nén một cách dễ dàng và an toàn.