# [Linux] Bash fg Cách sử dụng: Khôi phục tiến trình nền

## Overview
Lệnh `fg` trong Bash được sử dụng để đưa một tiến trình đang chạy ở chế độ nền (background) trở lại chế độ nền (foreground). Điều này cho phép người dùng tương tác trực tiếp với tiến trình đó.

## Usage
Cú pháp cơ bản của lệnh `fg` như sau:

```bash
fg [options] [job_spec]
```

## Common Options
- `job_spec`: Chỉ định tiến trình cụ thể mà bạn muốn đưa về chế độ foreground. Bạn có thể sử dụng số thứ tự của tiến trình hoặc ký hiệu `%` theo sau là số hoặc tên của tiến trình.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `fg`:

1. **Đưa tiến trình cuối cùng về foreground**:
   ```bash
   fg
   ```

2. **Đưa tiến trình thứ hai trong danh sách tiến trình về foreground**:
   ```bash
   fg %2
   ```

3. **Đưa một tiến trình cụ thể bằng tên về foreground**:
   ```bash
   fg %my_process
   ```

4. **Khi có nhiều tiến trình đang chạy, bạn có thể xem danh sách và đưa một tiến trình cụ thể về foreground**:
   ```bash
   jobs
   fg %1
   ```

## Tips
- Sử dụng lệnh `jobs` để xem danh sách các tiến trình đang chạy ở chế độ nền trước khi sử dụng `fg`.
- Nếu bạn không chỉ định `job_spec`, lệnh `fg` sẽ tự động đưa tiến trình cuối cùng được đưa vào nền về foreground.
- Đảm bảo rằng bạn đã sử dụng lệnh `bg` để chạy tiến trình ở chế độ nền trước khi sử dụng `fg` để đưa nó trở lại foreground.