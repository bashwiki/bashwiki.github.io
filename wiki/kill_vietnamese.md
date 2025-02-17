# [Linux] Bash kill Cách sử dụng: Giết tiến trình

## Overview
Lệnh `kill` trong Bash được sử dụng để gửi tín hiệu đến một hoặc nhiều tiến trình. Tín hiệu này thường được sử dụng để yêu cầu tiến trình dừng lại hoặc thoát.

## Usage
Cú pháp cơ bản của lệnh `kill` như sau:

```bash
kill [options] [arguments]
```

## Common Options
- `-l`: Liệt kê tất cả các tín hiệu có sẵn.
- `-s SIGNAL`: Gửi tín hiệu cụ thể đến tiến trình.
- `-n NUMBER`: Gửi tín hiệu theo số thứ tự của tín hiệu.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `kill`:

1. **Giết một tiến trình bằng PID**:
   ```bash
   kill 1234
   ```
   (Trong đó `1234` là ID của tiến trình bạn muốn dừng.)

2. **Gửi tín hiệu SIGKILL đến một tiến trình**:
   ```bash
   kill -9 1234
   ```
   (Sử dụng `-9` để buộc tiến trình dừng lại ngay lập tức.)

3. **Liệt kê tất cả các tín hiệu có sẵn**:
   ```bash
   kill -l
   ```

4. **Gửi tín hiệu SIGTERM đến một tiến trình**:
   ```bash
   kill -15 1234
   ```
   (Sử dụng `-15` để yêu cầu tiến trình dừng lại một cách lịch sự.)

## Tips
- Hãy cẩn thận khi sử dụng `kill -9`, vì nó không cho phép tiến trình thực hiện các thao tác dọn dẹp trước khi dừng.
- Sử dụng `ps` để tìm PID của tiến trình trước khi sử dụng lệnh `kill`.
- Thay vì giết từng tiến trình một, bạn có thể sử dụng `killall` để giết tất cả các tiến trình cùng tên.