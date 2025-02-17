# [Linux] Bash xz Cách sử dụng: Nén và giải nén tệp tin

## Tổng quan
Lệnh `xz` là một công cụ nén tệp tin mạnh mẽ, sử dụng thuật toán nén LZMA để giảm kích thước tệp. Nó thường được sử dụng để nén các tệp lớn, giúp tiết kiệm không gian lưu trữ và tăng tốc độ truyền tải dữ liệu.

## Cách sử dụng
Cú pháp cơ bản của lệnh `xz` như sau:
```bash
xz [options] [arguments]
```

## Tùy chọn phổ biến
- `-d`, `--decompress`: Giải nén tệp tin.
- `-k`, `--keep`: Giữ lại tệp tin gốc sau khi nén.
- `-f`, `--force`: Buộc ghi đè lên tệp tin đã tồn tại.
- `-9`: Sử dụng mức nén cao nhất (từ 1 đến 9).
- `-z`: Nén tệp tin (mặc định).

## Ví dụ phổ biến
1. Nén một tệp tin:
   ```bash
   xz file.txt
   ```

2. Giải nén một tệp tin đã nén:
   ```bash
   xz -d file.txt.xz
   ```

3. Nén tệp tin và giữ lại tệp gốc:
   ```bash
   xz -k file.txt
   ```

4. Nén với mức nén cao nhất:
   ```bash
   xz -9 file.txt
   ```

5. Giải nén tất cả các tệp `.xz` trong thư mục hiện tại:
   ```bash
   xz -d *.xz
   ```

## Mẹo
- Sử dụng tùy chọn `-k` nếu bạn muốn giữ lại tệp gốc sau khi nén, điều này rất hữu ích khi bạn cần kiểm tra nội dung của tệp gốc.
- Khi làm việc với nhiều tệp, bạn có thể nén chúng thành một tệp `.tar.xz` bằng cách sử dụng lệnh `tar` kết hợp với `xz`.
- Để tiết kiệm thời gian, hãy cân nhắc sử dụng mức nén thấp hơn nếu không cần thiết phải nén tối đa, vì mức nén cao hơn có thể tốn nhiều thời gian hơn.