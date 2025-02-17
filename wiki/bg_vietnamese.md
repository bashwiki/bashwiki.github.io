# [Linux] Bash bg Cách sử dụng: Chuyển tiến trình sang chế độ nền

## Overview
Lệnh `bg` trong Bash được sử dụng để chuyển một tiến trình đang chạy trong chế độ nền. Khi bạn chạy một lệnh trong terminal và muốn tiếp tục sử dụng terminal mà không dừng tiến trình đó, bạn có thể sử dụng lệnh `bg` để đưa tiến trình đó vào nền.

## Usage
Cú pháp cơ bản của lệnh `bg` như sau:

```bash
bg [options] [job_spec]
```

## Common Options
- `job_spec`: Chỉ định tiến trình mà bạn muốn đưa vào chế độ nền. Bạn có thể sử dụng số thứ tự của tiến trình hoặc ký hiệu `%` theo sau là số thứ tự.
- `-l`: Hiển thị danh sách các tiến trình đang chạy trong nền.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `bg`:

1. **Chuyển tiến trình đang chạy sang chế độ nền**:
   ```bash
   sleep 100
   ```
   Nhấn `Ctrl + Z` để dừng tiến trình, sau đó chạy:
   ```bash
   bg
   ```

2. **Chuyển một tiến trình cụ thể sang chế độ nền**:
   ```bash
   sleep 100 &
   ```
   Sau đó, nếu bạn muốn chuyển tiến trình đó sang nền:
   ```bash
   jobs
   bg %1
   ```

3. **Chuyển tiến trình thứ hai trong danh sách sang chế độ nền**:
   ```bash
   bg %2
   ```

## Tips
- Sử dụng lệnh `jobs` để xem danh sách các tiến trình đang chạy và tiến trình nào có thể được chuyển sang chế độ nền.
- Hãy chắc chắn rằng bạn đã dừng tiến trình bằng `Ctrl + Z` trước khi sử dụng `bg`.
- Bạn có thể kết hợp `bg` với các lệnh khác như `fg` để chuyển tiến trình từ nền trở lại chế độ foreground khi cần thiết.