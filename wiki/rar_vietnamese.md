# [Linux] Bash rar cách sử dụng: Nén và giải nén tệp tin

## Tổng quan
Lệnh `rar` được sử dụng để nén và giải nén các tệp tin trong định dạng RAR. Đây là một công cụ mạnh mẽ giúp tiết kiệm không gian lưu trữ và dễ dàng chia sẻ tệp tin.

## Cách sử dụng
Cú pháp cơ bản của lệnh `rar` như sau:
```
rar [options] [arguments]
```

## Các tùy chọn phổ biến
- `a`: Thêm tệp vào một tệp RAR.
- `x`: Giải nén tệp RAR.
- `t`: Kiểm tra tính toàn vẹn của tệp RAR.
- `v`: Hiển thị thông tin chi tiết trong quá trình nén hoặc giải nén.
- `r`: Nén các tệp trong thư mục con.

## Ví dụ phổ biến
- **Nén một tệp tin**:
```bash
rar a archive.rar file.txt
```
Lệnh này sẽ nén `file.txt` vào tệp `archive.rar`.

- **Giải nén một tệp RAR**:
```bash
rar x archive.rar
```
Lệnh này sẽ giải nén tất cả các tệp trong `archive.rar` vào thư mục hiện tại.

- **Nén một thư mục**:
```bash
rar a archive.rar /path/to/directory
```
Lệnh này sẽ nén toàn bộ thư mục vào tệp `archive.rar`.

- **Kiểm tra tính toàn vẹn của tệp RAR**:
```bash
rar t archive.rar
```
Lệnh này sẽ kiểm tra xem các tệp trong `archive.rar` có bị hỏng hay không.

## Mẹo
- Luôn kiểm tra tính toàn vẹn của tệp RAR sau khi giải nén để đảm bảo không có tệp nào bị hỏng.
- Sử dụng tùy chọn `v` để theo dõi quá trình nén hoặc giải nén, điều này giúp bạn biết được tiến độ của lệnh.
- Khi nén nhiều tệp, hãy sử dụng tùy chọn `r` để bao gồm cả các tệp trong thư mục con, giúp tiết kiệm thời gian và công sức.