# [Linux] Bash suspend lệnh: Tạm dừng tiến trình

## Overview
Lệnh `suspend` trong Bash được sử dụng để tạm dừng một tiến trình đang chạy trong terminal. Khi tiến trình bị tạm dừng, bạn có thể quay lại và tiếp tục nó sau đó mà không mất dữ liệu.

## Usage
Cú pháp cơ bản của lệnh `suspend` như sau:

```bash
suspend
```

Lưu ý rằng lệnh này thường được sử dụng trong bối cảnh của một tiến trình đang chạy trong shell.

## Common Options
Lệnh `suspend` không có nhiều tùy chọn, nhưng dưới đây là một số thông tin hữu ích:

- Không có tùy chọn: Lệnh này không yêu cầu bất kỳ tùy chọn nào và chỉ đơn giản là tạm dừng tiến trình hiện tại.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `suspend`:

1. **Tạm dừng một tiến trình đang chạy:**
   Khi bạn đang chạy một lệnh trong terminal, bạn có thể tạm dừng nó bằng cách nhấn `Ctrl + Z`. Điều này sẽ đưa tiến trình vào trạng thái tạm dừng.

   ```bash
   # Giả sử bạn đang chạy một lệnh như:
   sleep 100
   # Nhấn Ctrl + Z để tạm dừng
   ```

2. **Tiếp tục một tiến trình đã tạm dừng:**
   Sau khi tạm dừng, bạn có thể tiếp tục tiến trình bằng lệnh `fg` (foreground).

   ```bash
   fg
   ```

## Tips
- **Sử dụng `jobs`:** Sau khi tạm dừng một tiến trình, bạn có thể sử dụng lệnh `jobs` để xem danh sách các tiến trình đang chạy và tạm dừng.
  
- **Quản lý tiến trình:** Hãy nhớ rằng bạn có thể tạm dừng nhiều tiến trình và tiếp tục chúng bằng cách chỉ định số thứ tự của tiến trình với lệnh `fg %n`, trong đó `n` là số thứ tự của tiến trình.

- **Tránh mất dữ liệu:** Trước khi tạm dừng một tiến trình, hãy đảm bảo rằng bạn không đang thực hiện các thao tác quan trọng để tránh mất dữ liệu.