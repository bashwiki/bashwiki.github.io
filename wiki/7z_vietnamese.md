# [리눅스] Bash 7z 사용법

## Tổng quan
Lệnh `7z` là một công cụ nén và giải nén file mạnh mẽ, thuộc về phần mềm 7-Zip. Nó hỗ trợ nhiều định dạng nén khác nhau và cho phép người dùng nén, giải nén, và quản lý các file nén một cách hiệu quả. Lệnh này rất hữu ích cho các kỹ sư và nhà phát triển khi cần tiết kiệm không gian lưu trữ hoặc chia sẻ nhiều file trong một gói.

## Cách sử dụng
Cú pháp cơ bản của lệnh `7z` như sau:

```
7z [tùy chọn] [hành động] [file đầu vào] [file đầu ra]
```

### Một số tùy chọn phổ biến:
- `a`: Thêm file vào archive (nén file).
- `x`: Giải nén file từ archive.
- `l`: Liệt kê nội dung của archive.
- `d`: Xóa file từ archive.
- `t`: Kiểm tra tính toàn vẹn của archive.

## Ví dụ
### Ví dụ 1: Nén file
Để nén một file có tên `example.txt` thành file nén `example.7z`, bạn có thể sử dụng lệnh sau:

```bash
7z a example.7z example.txt
```

### Ví dụ 2: Giải nén file
Để giải nén file `example.7z` vào thư mục hiện tại, bạn có thể sử dụng lệnh sau:

```bash
7z x example.7z
```

## Mẹo
- Khi nén nhiều file, bạn có thể sử dụng ký tự đại diện (`*`) để chọn nhiều file cùng loại. Ví dụ: `7z a archive.7z *.txt` sẽ nén tất cả các file `.txt` trong thư mục hiện tại.
- Để tăng tốc độ nén, bạn có thể sử dụng tùy chọn `-mx=9` để nén ở mức cao nhất, nhưng điều này có thể làm tăng thời gian nén.
- Hãy kiểm tra tính toàn vẹn của archive bằng cách sử dụng tùy chọn `t` để đảm bảo rằng file nén không bị hỏng.

Lệnh `7z` là một công cụ rất hữu ích cho việc quản lý file nén, và với các tùy chọn linh hoạt, nó có thể đáp ứng nhiều nhu cầu khác nhau của người dùng.