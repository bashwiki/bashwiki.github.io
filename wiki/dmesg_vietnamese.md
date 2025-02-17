# [Linux] Bash dmesg Cách sử dụng: Xem thông tin log kernel

## Overview
Lệnh `dmesg` được sử dụng để hiển thị thông tin log từ kernel của hệ điều hành Linux. Nó cho phép người dùng xem các thông báo khởi động, thông tin về phần cứng và các sự kiện khác liên quan đến hệ thống.

## Usage
Cú pháp cơ bản của lệnh `dmesg` như sau:

```bash
dmesg [options] [arguments]
```

## Common Options
- `-C`: Xóa thông báo hiện tại trong buffer.
- `-c`: Xóa thông báo và hiển thị chúng một lần.
- `-n level`: Thiết lập mức độ thông báo mà bạn muốn hiển thị.
- `-T`: Hiển thị thời gian theo định dạng dễ đọc.
- `-f facility`: Lọc thông báo theo loại (facility).

## Common Examples
1. **Xem toàn bộ thông báo kernel:**
   ```bash
   dmesg
   ```

2. **Xem thông báo với thời gian dễ đọc:**
   ```bash
   dmesg -T
   ```

3. **Lọc thông báo theo mức độ nghiêm trọng:**
   ```bash
   dmesg -n 1
   ```

4. **Xóa thông báo hiện tại và hiển thị chúng:**
   ```bash
   dmesg -c
   ```

5. **Lọc thông báo theo loại:**
   ```bash
   dmesg -f kern
   ```

## Tips
- Sử dụng `dmesg | less` để dễ dàng cuộn qua các thông báo dài.
- Kết hợp `dmesg` với `grep` để tìm kiếm thông báo cụ thể, ví dụ: `dmesg | grep error`.
- Thường xuyên kiểm tra `dmesg` sau khi khởi động lại hệ thống để phát hiện các vấn đề phần cứng.