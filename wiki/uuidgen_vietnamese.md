# [Linux] Bash uuidgen cách sử dụng: Tạo UUID ngẫu nhiên

## Tổng quan
Lệnh `uuidgen` được sử dụng để tạo ra các UUID (Universally Unique Identifier) ngẫu nhiên. UUID là một định danh duy nhất toàn cầu, thường được sử dụng trong các ứng dụng để xác định một đối tượng mà không cần phải lo lắng về sự trùng lặp.

## Cách sử dụng
Cú pháp cơ bản của lệnh `uuidgen` như sau:
```
uuidgen [options] [arguments]
```

## Các tùy chọn phổ biến
- `-r`, `--random`: Tạo UUID ngẫu nhiên.
- `-t`, `--time`: Tạo UUID dựa trên thời gian.
- `-h`, `--help`: Hiển thị thông tin trợ giúp về lệnh.

## Ví dụ thường gặp
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `uuidgen`:

1. Tạo một UUID ngẫu nhiên:
   ```bash
   uuidgen
   ```

2. Tạo nhiều UUID ngẫu nhiên:
   ```bash
   uuidgen uuidgen uuidgen
   ```

3. Tạo một UUID dựa trên thời gian:
   ```bash
   uuidgen -t
   ```

4. Hiển thị thông tin trợ giúp:
   ```bash
   uuidgen --help
   ```

## Mẹo
- Sử dụng UUID trong cơ sở dữ liệu để đảm bảo rằng các khóa chính là duy nhất.
- Khi tạo UUID cho các đối tượng trong ứng dụng, hãy sử dụng tùy chọn ngẫu nhiên để giảm khả năng trùng lặp.
- Lưu ý rằng UUID có kích thước lớn, vì vậy hãy cân nhắc khi sử dụng trong các hệ thống có giới hạn về dung lượng lưu trữ.