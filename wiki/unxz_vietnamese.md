# [Linux] Bash unxz: Giải nén tệp tin .xz

## Overview
Lệnh `unxz` được sử dụng để giải nén các tệp tin có định dạng .xz. Đây là một công cụ hữu ích trong việc xử lý các tệp nén, giúp tiết kiệm không gian lưu trữ và dễ dàng truyền tải dữ liệu.

## Usage
Cú pháp cơ bản của lệnh `unxz` như sau:
```
unxz [options] [arguments]
```

## Common Options
- `-k`, `--keep`: Giữ lại tệp tin gốc sau khi giải nén.
- `-f`, `--force`: Buộc ghi đè lên tệp tin đã tồn tại mà không cần xác nhận.
- `-v`, `--verbose`: Hiển thị thông tin chi tiết trong quá trình giải nén.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `unxz`:

1. Giải nén một tệp tin .xz:
   ```bash
   unxz file.xz
   ```

2. Giải nén và giữ lại tệp tin gốc:
   ```bash
   unxz -k file.xz
   ```

3. Giải nén một tệp tin và ghi đè lên tệp tin đã tồn tại:
   ```bash
   unxz -f file.xz
   ```

4. Giải nén và hiển thị thông tin chi tiết:
   ```bash
   unxz -v file.xz
   ```

## Tips
- Luôn kiểm tra dung lượng ổ đĩa trước khi giải nén, vì tệp tin sau khi giải nén có thể chiếm nhiều không gian hơn.
- Sử dụng tùy chọn `-k` nếu bạn không muốn mất tệp tin gốc trong quá trình giải nén.
- Nếu bạn gặp phải tệp tin đã tồn tại, hãy cân nhắc sử dụng tùy chọn `-f` để tránh phải xác nhận từng lần.