# [Linux] Bash tee cách sử dụng: Ghi và hiển thị đầu ra đồng thời

## Overview
Lệnh `tee` trong Bash được sử dụng để đọc từ đầu vào chuẩn và ghi vào cả đầu ra chuẩn và một hoặc nhiều tệp. Điều này cho phép bạn xem dữ liệu trong khi cũng lưu trữ nó cho các mục đích sử dụng sau.

## Usage
Cú pháp cơ bản của lệnh `tee` như sau:
```bash
tee [options] [arguments]
```

## Common Options
- `-a`, `--append`: Ghi thêm vào tệp thay vì ghi đè.
- `-i`, `--ignore-interrupts`: Bỏ qua các tín hiệu ngắt.
- `-p`, `--output-error`: Chỉ định cách xử lý lỗi đầu ra.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `tee`:

1. Ghi đầu ra của lệnh `echo` vào tệp:
   ```bash
   echo "Hello, World!" | tee output.txt
   ```

2. Ghi đầu ra vào nhiều tệp:
   ```bash
   echo "Logging data" | tee file1.txt file2.txt
   ```

3. Ghi thêm vào tệp thay vì ghi đè:
   ```bash
   echo "Appending this line" | tee -a output.txt
   ```

4. Sử dụng với lệnh `cat` để xem nội dung tệp và lưu lại:
   ```bash
   cat input.txt | tee output.txt
   ```

## Tips
- Sử dụng tùy chọn `-a` khi bạn muốn thêm dữ liệu vào tệp mà không làm mất dữ liệu cũ.
- Kết hợp `tee` với các lệnh khác trong pipeline để theo dõi và lưu trữ đầu ra một cách hiệu quả.
- Kiểm tra quyền ghi vào tệp trước khi sử dụng `tee` để tránh lỗi không mong muốn.