# [리눅스] Bash wc 사용법

## Tổng quan
Lệnh `wc` (word count) trong Bash được sử dụng để đếm số lượng dòng, từ và ký tự trong một hoặc nhiều tệp. Đây là một công cụ hữu ích cho các kỹ sư và nhà phát triển khi cần phân tích nội dung của tệp văn bản hoặc khi cần thống kê thông tin về dữ liệu.

## Cách sử dụng
Cú pháp cơ bản của lệnh `wc` như sau:
```
wc [tùy chọn] [tệp]
```
Một số tùy chọn phổ biến của lệnh `wc` bao gồm:
- `-l`: Đếm số dòng.
- `-w`: Đếm số từ.
- `-c`: Đếm số ký tự.
- `-m`: Đếm số ký tự (bao gồm cả ký tự Unicode).
- `-L`: Hiển thị chiều dài của dòng dài nhất.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng lệnh `wc`:

1. Đếm số dòng, từ và ký tự trong một tệp văn bản:
   ```bash
   wc example.txt
   ```
   Kết quả sẽ hiển thị số dòng, số từ và số ký tự trong `example.txt`.

2. Chỉ đếm số dòng trong một tệp:
   ```bash
   wc -l example.txt
   ```
   Kết quả sẽ chỉ hiển thị số dòng trong `example.txt`.

## Mẹo
- Bạn có thể sử dụng lệnh `wc` kết hợp với các lệnh khác thông qua ống dẫn (pipe). Ví dụ, để đếm số dòng trong kết quả của lệnh `ls`, bạn có thể sử dụng:
  ```bash
  ls | wc -l
  ```
- Khi làm việc với nhiều tệp, bạn có thể chỉ định nhiều tệp cùng một lúc. Kết quả sẽ hiển thị cho từng tệp và tổng số cuối cùng:
  ```bash
  wc file1.txt file2.txt
  ```

Hy vọng rằng bài viết này sẽ giúp bạn hiểu rõ hơn về cách sử dụng lệnh `wc` trong Bash!